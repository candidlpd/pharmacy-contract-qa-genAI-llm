import os
from PyPDF2 import PdfReader
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import Pinecone as PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec

# Configuration
DATA_FOLDER = "data/contracts"
PINECONE_API_KEY = "pcsk_4ECwoe_HeWcQ4aEkw2cx3Z6mEeeWpFbdvihaQjf6JEKCYaX2wYQq3BKFAphema1XYG7cWa"
PINECONE_ENV = "eastus2"
PINECONE_INDEX_NAME = "contracts-index"
OPENAI_API_KEY = "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"
MODEL_NAME = "gpt-4"
CHUNK_SIZE = 500
BATCH_SIZE = 100

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
    
    # Use PineconeVectorStore properly as a retriever
    retriever = PineconeVectorStore(index=pinecone_index, embedding=embeddings_model, text_key="text")
    llm = ChatOpenAI(model_name=MODEL_NAME, openai_api_key=OPENAI_API_KEY)
    
    # RetrievalQA requires retriever input
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever.as_retriever(),  # Ensure the retriever is valid
        chain_type="stuff"
    )
    return qa.run(query)

# Main execution
if __name__ == "__main__":
    # Step 1: Load and chunk PDFs
    print("\n### Processing all client contracts ###")
    all_chunks = load_and_chunk_pdfs(DATA_FOLDER, CHUNK_SIZE)
    print(f"Total chunks processed: {len(all_chunks)}")

    # Step 2: Generate embeddings and upsert to Pinecone
    embeddings_model = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    pinecone_client = initialize_pinecone(PINECONE_API_KEY)
    upsert_embeddings(pinecone_client, PINECONE_INDEX_NAME, all_chunks, embeddings_model)

    # Step 3: Query Pinecone index
    query = "What is the Contract Amount and End Date of Contract 7?"
    print(f"\nQuerying: {query}")
    answer = query_pinecone(pinecone_client, PINECONE_INDEX_NAME, embeddings_model, query)
    print("\nAnswer:", answer)



# *******************************************************************Exlanation of results**************************************

# Observations:
# 1. Successful Execution:
# The program processed 15 PDF files and successfully created embeddings, stored them in Pinecone, and queried the index.

#-------------------------
# 2. Correct Query Output:
# The answer was accurate:
# The Contract Amount for Contract 7 is $100,000 and the End Date is 2026-12-31.

#-------------------------
# 3. PDF Processing:

# Files Loaded: The script identified all PDF files in data/contracts (15 total).
# Text Extraction: Text content was extracted page by page using PyPDF2.
# Chunking: The text was split into manageable chunks of 500 characters each.
# Total Chunks: A total of 724 chunks were generated from the 15 files.
#---------------------------

# 4. Pinecone Initialization:
# Successfully initialized Pinecone with the provided API key and environment.

#-----------------
# 5. Upserting Vectors:
# Embeddings for the 724 text chunks were generated using OpenAI's GPT-4 embedding model.
# The embeddings were uploaded to Pinecone in batches of 100 vectors each for efficiency.

#------------------------------
# 6. Query Execution:
# The query "What is the Contract Amount and End Date of Contract 7?" was passed.
# Pinecone retrieved the most relevant document chunks using cosine similarity.
# The LangChain RetrievalQA chain invoked GPT-4 to synthesize a precise answer.

#-------------------------
# 7. Final Answer:
# Pinecone + GPT-4 provided the final output:
# "The Contract Amount for Contract 7 is $100,000 and the End Date is 2026-12-31."

