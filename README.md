Contract QA System
This repository contains a Contract QA (Question-Answering) System designed to process hundreds of PDF contracts, extract critical information, and answer user queries using a natural language model. The system uses OpenAI embeddings and stores the data in Pinecone for efficient retrieval and querying.

Project Goals
PDF Text Extraction: Load and process large volumes of contract PDF files to extract textual data.
Chunking: Break long contract texts into manageable chunks for embedding generation.
Embeddings Generation: Generate text embeddings using OpenAI's API to transform chunks into vector representations.
Vector Storage: Use Pinecone as a vector database to efficiently store and retrieve embeddings.
Natural Language Querying: Use GPT-4 to answer questions contextually, enabling quick contract insights for the user.
Scalability: Handle hundreds of PDF files (or more) without performance degradation.
Tech Stack
Python 3.11+: Core programming language.
PyPDF2: Extract and process text data from PDF files.
LangChain: Framework for building and orchestrating LLM-powered applications.
OpenAI GPT-4: Language model to provide contextual answers to queries.
Pinecone: Vector database for storing and querying embeddings at scale.
Azure: Cloud-hosting support for Pinecone services.
Project Structure
plaintext
Copy code
contract_qa_project/
│
├── data/
│   └── contracts/           # Folder containing PDF contract files (100+ PDFs)
│
├── src/
│   ├── contract_qa_local.py         # Script to process and query contracts
│   ├── contract_qa_100PDF.py        # Optimized script for 100+ PDFs
│   └── test.py                      # Testing script for QA queries
│
├── embeddings/                      # Folder to store local embeddings if needed
└── README.md                        # Project documentation
Workflow Overview
1. Text Extraction & Chunking
Extracts textual data from PDF contracts and splits it into chunks of 500 characters for efficient processing.
2. Embeddings Generation
OpenAI's API generates embeddings for each text chunk.
3. Vector Upsertion
Embeddings are stored in Pinecone for fast retrieval.
Chunks are upserted in batches (e.g., batch size of 100).
4. Querying the Contracts
Users can query contract details (e.g., "What is the contract amount and end date for Contract 7?").
GPT-4 answers the queries by retrieving relevant chunks from Pinecone.
Example Query
Sample Question:

"What is the Contract Amount and End Date of Contract 7?"

Sample Answer:

"The Contract Amount for Contract 7 is $100,000, and the End Date is 2026-12-31."

Git Workflow: Initial Push
To push the project for the first time to a GitHub repository:

bash
Copy code
# Navigate to your project directory
cd H:\Lilly_Projects\contract_qa_project

# Initialize Git
git init

# Add remote origin
git remote add origin https://github.com/candidlpd/contract_qa_project.git

# Create and switch to feature branch
git checkout -b feature

# Stage and commit files
git add .
git commit -m "Initial commit: Added Contract QA Project"

# Push to remote
git push -u origin feature
Git Workflow: Adding New Files
To add and push new or updated files (e.g., contract_qa_100PDF.py and new contract PDFs):

bash
Copy code
# Check current branch
git status
git branch

# Ensure you're on the 'feature' branch
git checkout feature

# Add new files and updates
git add src/contract_qa_100PDF.py data/contracts/* README.md

# Commit changes with a descriptive message
git commit -m "Added contract_qa_100PDF.py and updated contract data files"

# Pull and rebase to avoid conflicts
git pull origin feature --rebase

# Push changes to remote repository
git push origin feature
Scalability for 100+ PDFs
The contract_qa_100PDF.py script has been optimized to handle hundreds of PDF files efficiently. Key optimizations include:

Batch Processing:
Process text extraction and embedding in batches to optimize memory and performance.
Parallel Execution (Optional):
Text extraction can be parallelized using libraries like multiprocessing for faster processing of PDFs.
Dynamic Chunking:
Flexible chunk sizes ensure compatibility with varying text lengths.
Efficient Upserts:
Vectors are upserted to Pinecone in batches to prevent API throttling.
How to Run the Project
Ensure all dependencies are installed:

bash
Copy code
pip install -r requirements.txt
Run the script to process PDFs and query:

bash
Copy code
python src/contract_qa_100PDF.py
Modify the query in the script for your question:

python
Copy code
query = "What is the Contract Amount and End Date of Contract 7?"
Output:
The script will output the most relevant and contextual answer to your query.

Future Enhancements
Add GUI: Develop a user interface to upload PDFs and ask queries interactively.
Parallel Processing: Use multiprocessing or job queues for faster batch processing.
Logging: Add detailed logging for better debugging and monitoring.
Cloud Storage: Integrate with cloud storage systems (e.g., AWS S3, Azure Blob) to manage PDF contracts.
Contributors
Lal Dangal (candidlpd)


With this updated README.md, the documentation is comprehensive, contextual, and well-structured for a project involving 100+ PDFs. Copy and paste this into your file, and it should work seamlessly. 🚀