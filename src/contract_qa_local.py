import os
from PyPDF2 import PdfReader
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain_pinecone import Pinecone as PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec

# Configuration
DATA_FOLDER = "data/contracts"
PINECONE_API_KEY = "pcsk_4ECwoe_HeWcQ4aEkw2cx3Z6mEeeWpFbdvihaQjf6JEKCYaX2wYQq3BKFAphema1XYG7cWa"
PINECONE_ENV = "eastus2"
PINECONE_INDEX_NAME = "contracts-index"
OPENAI_API_KEY = "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"
MODEL_NAME = "gpt-4"
CHUNK_SIZE = 500

# Function to load and chunk PDFs
def load_and_chunk_pdfs(pdf_folder_path, chunk_size):
    chunks = []
    for file in os.listdir(pdf_folder_path):
        if file.endswith(".pdf") and not file.startswith("~$"):
            file_path = os.path.join(pdf_folder_path, file)
            try:
                reader = PdfReader(file_path)
                text = ""
                for page in reader.pages:
                    text += page.extract_text() or ""
                chunks.extend([text[i:i + chunk_size] for i in range(0, len(text), chunk_size)])
                print(f"Processed file: {file}, Chunks: {len(chunks)}")
            except Exception as e:
                print(f"Error reading {file}: {e}")
    return chunks



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
    batch_size = 100
    for i in range(0, len(chunks), batch_size):
        batch = [
            {"id": f"chunk_{j}", "values": embeddings[j], "metadata": {"text": chunks[j]}}
            for j in range(i, min(i + batch_size, len(chunks)))
        ]
        index.upsert(vectors=batch)
        print(f"Upserted batch {i // batch_size + 1}")
    print("Embeddings stored successfully.")

# Function to create Pinecone retriever
def create_pinecone_retriever(pinecone_client, index_name, embeddings_model):
    print("Initializing Pinecone retriever...")
    pinecone_index = pinecone_client.Index(index_name)
    return PineconeVectorStore(index=pinecone_index, embedding=embeddings_model, text_key="text")

# Main execution
if __name__ == "__main__":
    # Step 1: Load and chunk PDFs
    print("Loading PDFs and processing text...")
    chunks = load_and_chunk_pdfs(DATA_FOLDER, CHUNK_SIZE)
    if not chunks:
        print("No valid PDFs found. Exiting...")
        exit()

    # Step 2: Generate embeddings and store in Pinecone
    embeddings_model = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    pinecone_client = initialize_pinecone(PINECONE_API_KEY)
    upsert_embeddings(pinecone_client, PINECONE_INDEX_NAME, chunks, embeddings_model)

    # Step 3: Create retriever and query
    retriever = create_pinecone_retriever(pinecone_client, PINECONE_INDEX_NAME, embeddings_model)
    llm = ChatOpenAI(model_name=MODEL_NAME, openai_api_key=OPENAI_API_KEY)

    # Querying the system
    query = "What is the validity of Contract_C?"
    print(f"\nQuerying: {query}")
    docs = retriever.similarity_search(query, k=1)  # Retrieve the most relevant document
    chain = load_qa_chain(llm, chain_type="stuff")
    result = chain.invoke({"input_documents": docs, "question": query})
    print("\nAnswer:", result["output_text"])
