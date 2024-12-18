import os
from PyPDF2 import PdfReader
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA
from langchain_pinecone import PineconeVectorStore  # Updated PineconeVectorStore import
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration
DATA_FOLDER = os.getenv("DATA_FOLDER", "data/contracts")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = os.getenv("PINECONE_ENV", "eastus2")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME", "contracts-index")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4")
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 500))
BATCH_SIZE = int(os.getenv("BATCH_SIZE", 100))

# Initialize Pinecone client
def initialize_pinecone(api_key):
    print("Initializing Pinecone...")
    try:
        client = Pinecone(api_key=api_key)
        print("Pinecone initialized successfully.")
        return client
    except Exception as e:
        print(f"Failed to initialize Pinecone: {e}")
        exit()

# Function to load and chunk PDFs
def load_and_chunk_pdfs(pdf_folder_path, chunk_size):
    chunks = []
    for file in os.listdir(pdf_folder_path):
        if file.endswith(".pdf") and not file.startswith("~$"):
            file_path = os.path.join(pdf_folder_path, file)
            try:
                reader = PdfReader(file_path)
                text = "".join(page.extract_text() or "" for page in reader.pages)
                file_chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
                chunks.extend(file_chunks)
                print(f"Processed: {file_path}, Chunks: {len(file_chunks)}")
            except Exception as e:
                print(f"Error reading {file}: {e}")
    return chunks

# Function to upsert embeddings into Pinecone
def upsert_embeddings(pinecone_client, index_name, chunks, embeddings_model):
    print("Upserting vectors in batches...")
    if index_name not in pinecone_client.list_indexes().names():
        pinecone_client.create_index(
            name=index_name,
            dimension=1536,
            metric="cosine",
            spec=ServerlessSpec(cloud="azure", region=PINECONE_ENV),
        )
    index = pinecone_client.Index(index_name)
    embeddings = embeddings_model.embed_documents(chunks)
    for i in range(0, len(chunks), BATCH_SIZE):
        batch = [
            {"id": f"chunk_{j}", "values": embeddings[j], "metadata": {"text": chunks[j]}}
            for j in range(i, min(i + BATCH_SIZE, len(chunks)))
        ]
        index.upsert(vectors=batch)
        print(f"Upserted batch {i // BATCH_SIZE + 1}")
    print("Embeddings stored successfully.")

# Function to query Pinecone index
def query_pinecone(pinecone_client, index_name, embeddings_model, query):
    print("Querying Pinecone index...")
    pinecone_index = pinecone_client.Index(index_name)
    retriever = PineconeVectorStore(index=pinecone_index, embedding=embeddings_model, text_key="text").as_retriever()
    llm = ChatOpenAI(model_name=MODEL_NAME, openai_api_key=OPENAI_API_KEY)

    # Use RetrievalQA chain with the retriever
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff"  # Combines all retrieved documents into one input
    )
    response = qa_chain.invoke({"query": query})
    return response

# Main execution
if __name__ == "__main__":
    print("\n### Processing all client contracts ###")
    all_chunks = load_and_chunk_pdfs(DATA_FOLDER, CHUNK_SIZE)
    print(f"Total chunks processed: {len(all_chunks)}")

    embeddings_model = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    pinecone_client = initialize_pinecone(PINECONE_API_KEY)
    upsert_embeddings(pinecone_client, PINECONE_INDEX_NAME, all_chunks, embeddings_model)

    while True:
        query = input("\nEnter your query (or type 'exit' to quit): ")
        if query.lower() == "exit":
            print("Exiting program. Goodbye!")
            break
        print(f"\nQuerying: {query}")
        answer = query_pinecone(pinecone_client, PINECONE_INDEX_NAME, embeddings_model, query)
        print("\nAnswer:", answer)

