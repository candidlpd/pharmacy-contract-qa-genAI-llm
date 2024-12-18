
# **Contract QA System**

This repository contains a **Contract QA (Question-Answering) System** designed to process hundreds of PDF contracts, extract critical information, and answer user queries using a natural language model. The system uses **OpenAI embeddings** and stores the data in **Pinecone** for efficient retrieval and querying.

---

## **Project Goals**

- **PDF Text Extraction**: Load and process large volumes of PDF contracts to extract text.
- **Chunking**: Break long contract texts into manageable 500-character chunks.
- **Embeddings Generation**: Generate text embeddings using OpenAI's API.
- **Vector Storage**: Store embeddings in Pinecone for efficient querying.
- **Natural Language Querying**: Use GPT-4 to answer questions contextually about contract details.
- **Scalability**: Process hundreds of PDFs without performance degradation.

---

## **Tech Stack**

| **Technology**    | **Purpose**                                     |
|-------------------|-------------------------------------------------|
| **Python 3.11+**   | Core programming language                      |
| **PyPDF2**         | Extract and process text data from PDF files   |
| **LangChain**      | Framework to build LLM-powered workflows       |
| **OpenAI GPT-4**   | Language model for generating answers          |
| **Pinecone**       | Vector database for fast storage and retrieval |
| **Azure**          | Cloud-hosting support for Pinecone services    |

---

## **Project Structure**

```plaintext
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
├── embeddings/                      # (Optional) Directory for local embeddings
├── models/                          # (Optional) Pre-trained model files
├── README.md                        # Project documentation
└── requirements.txt                 # Dependencies for the project

### Workflow Overview

Text Extraction & Chunking

Extract text from PDFs.
Split text into manageable chunks for efficient embedding generation.
Embeddings Generation

Use OpenAI's API to generate embeddings for text chunks.
Store embeddings in Pinecone for retrieval.
Querying the Contracts

Ask questions in natural language (e.g., "Contract amount and end date for Contract 7?").
GPT-4 retrieves relevant data from Pinecone and provides answers.
### Example Query

Input Question:  "What is the Contract Amount and End Date of Contract 7?"

Output Answer:  "The Contract Amount for Contract 7 is $100,000, and the End Date is 2026-12-31."

### How to Run the Project

Install Dependencies

Bash

pip install -r requirements.txt
Process PDF Contracts

Bash

python src/contract_qa_100PDF.py
Modify Query

Update the query in the script to match your question.

Python

query = "What is the Contract Amount and End Date of Contract 7?"
View Results

The system will output the most relevant answer to your query.

### Git Workflow

Initial Push

Bash

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
Adding New Files

Bash

# Check current branch
git status
git branch

# Ensure you're on the 'feature' branch
git checkout feature

# Add new files and changes
git add src/contract_qa_100PDF.py data/contracts/* README.md

# Commit changes with a descriptive message
git commit -m "Added new file and updated contract data"

# Pull and rebase to prevent conflicts
git pull origin feature --rebase

# Push changes
git push origin feature
### Scalability for 100+ PDFs

contract_qa_100PDF.py is optimized for large datasets with features like:
Batch processing
Dynamic chunking
Optional parallel