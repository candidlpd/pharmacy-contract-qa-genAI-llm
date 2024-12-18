# contract_qa_project

# Contract QA System

This repository contains a **Contract QA (Question-Answering) System** that extracts information from PDF contracts, generates embeddings using OpenAI, and stores them in Pinecone for retrieval. It allows querying the stored data using a natural language model, such as GPT-4, to answer questions about contract details.

---

## Project Goals

1. **PDF Extraction**: Load and process text data from contract PDF files.
2. **Chunking**: Break long contract texts into smaller, manageable chunks.
3. **Embeddings Generation**: Use OpenAI's `embeddings` API to generate text embeddings.
4. **Vector Storage**: Store embeddings in Pinecone for efficient retrieval.
5. **Natural Language Query**: Use OpenAI's GPT-4 model to provide contextual answers to user queries about contracts.

---

## Tech Stack

- **Python 3.11+**
- **PyPDF2**: Extract text from PDF files.
- **LangChain**: Framework for building LLM-powered applications.
- **OpenAI GPT-4**: Language model for question-answering.
- **Pinecone**: Vector database for storing and retrieving embeddings.
- **Azure**: Cloud hosting region for Pinecone.

---

## Project Structure

```plaintext
contract_qa_project/
│
├── data/
│   └── contracts/           # Folder containing contract PDFs
│
├── src/
│   └── contract_qa_local.py # Main script for the project
│
└── README.md                # Documentation


## Git process very first to push. repo with same folder name should be created in remote and by sittiong on the top of same folder, process below code. 
cd H:\Lilly_Projects\contract_qa_project

git init
git remote add origin https://github.com/candidlpd/contract_qa_project.git
git remote -v
git checkout -b feature
git add .
git status
git commit -m "Initial commit: Added Contract QA Project"
git push -u origin feature
git pull origin feature --rebase
git status
 
git rebase --continue
git push -u origin feature --force
get-history




