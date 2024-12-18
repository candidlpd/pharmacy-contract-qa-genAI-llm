# Contract QA System

This repository contains a **Contract QA (Question-Answering) System** designed to process hundreds of PDF contracts, extract critical information, and answer user queries using a natural language model. The system uses OpenAI embeddings and stores the data in Pinecone for efficient retrieval and querying.

---

## Project Goals

1. **PDF Text Extraction**
   - Load and process large volumes of PDF contracts to extract text.

2. **Chunking**
   - Split long contract texts into smaller, 500-character chunks for efficient processing.

3. **Embeddings Generation**
   - Use OpenAI's API to generate embeddings for the text chunks.
   - Store the embeddings in Pinecone for efficient retrieval.

4. **Natural Language Querying**
   - Use GPT-4 to answer user queries in natural language based on the stored embeddings.

5. **Scalability**
   - Process hundreds of PDFs efficiently using optimized batch processing and parallel execution.

---

## Tech Stack

| Technology       | Purpose                                    |
|-------------------|--------------------------------------------|
| Python 3.11+      | Core programming language                 |
| PyPDF2            | Extract and process text data from PDF files |
| LangChain         | Framework to build LLM-powered workflows  |
| OpenAI GPT-4      | Language model for generating answers      |
| Pinecone          | Vector database for fast storage and retrieval |
| Azure             | Cloud-hosting support for Pinecone services |

---

## Project Structure

```plaintext
CONTRACT_QA_PROJECT/
│
├── .vscode/               # VS Code configuration files
├── config/                # Configuration files for the project
├── data/                  # Folder to store PDF files and datasets
├── embeddings/            # Directory to manage embeddings
├── models/                # Model checkpoints or custom models
├── notebooks/             # Jupyter notebooks for experiments
├── src/                   # Source code for the project
│   ├── contract_qa_local_100PDF.py  # Main script for processing 100+ PDFs
│   ├── contract_qa_local.py         # Local script for querying contracts
│   └── test.py                      # Script for testing the workflow
├── .env                   # Environment variables (e.g., API keys)
├── .gitignore             # Ignore files (e.g., .env, cache, models)
└── README.md              # Documentation of the project

```

---
### Workflow Overview
1. **Text Extraction & Chunking**
* Extracts text from PDF contracts.
* Splits text into 500-character chunks for efficient embedding generation.
2. **Embeddings Generation**
* OpenAI's API generates embeddings for the text chunks.
* Pinecone stores these embeddings for retrieval.
3. **Querying the Contracts**
* Users ask questions in natural language, e.g.:
**"What is the contract amount and end date for Contract 7?"**
* GPT-4 retrieves relevant data from Pinecone and provides precise answers.


### Example Query
**Input Question**
"What is the Contract Amount and End Date of Contract 7?"

**Output Answer**
"The Contract Amount for Contract 7 is $100,000, and the End Date is 2026-12-31."

## How to Run the Project
1. **Install Dependencies**
Run the following command to install all required libraries:

pip install -r requirements.txt

2. **Process PDFs and Query Contracts**
Run the script to process PDF files and query contract data:


python src/contract_qa_local.py
3. **Modify Query**
To change the query, update the following line in the script:

query = "What is the Contract Amount and End Date of Contract 7?"


# Git Workflow
## Initial Push to Remote Repository

### Navigate to your project directory
cd H:\Lilly_Projects\contract_qa_project

### Initialize Git and add the remote repository
git init
git remote add origin https://github.com/candidlpd/contract_qa_project.git

### Create and switch to the 'feature' branch
git checkout -b feature

### Stage and commit all files
git add .
git commit -m "Initial commit: Added Contract QA Project"

### Push to the remote repository
git push -u origin feature


## Adding New Files or Updates
To add and push new files like contract_qa_100PDF.py and updated data:


### Check current branch
git status
git branch

### Ensure you're on the 'feature' branch
git checkout feature

### Add new files and updates
git add src/contract_qa_100PDF.py data/contracts/* README.md

### Commit changes with a descriptive message
git commit -m "Added contract_qa_100PDF.py and updated contract data files"

### Pull and rebase to avoid conflicts
git pull origin feature --rebase

### Push changes to remote repository
git push origin feature


## Scalability for 100+ PDFs
The contract_qa_100PDF.py script is optimized for handling large volumes of PDF files efficiently. Key features include:

* **Batch Processing:** Process text extraction and embeddings in manageable batches.
* **Parallel Execution:** Optional use of Python's multiprocessing for faster processing.
* **Dynamic Chunking:** Handles varying text lengths dynamically.
* **Efficient Upserts:** Avoid API throttling by upserting vectors to Pinecone in small batches.


## Future Enhancements
* 1. **Add GUI:** Develop a user-friendly interface for uploading PDFs and asking queries interactively.
* 2. **Parallel Processing:** Use job queues or multiprocessing for faster text extraction and embeddings.
* 3. **Logging:** Add detailed logging for better debugging and monitoring.
* 4. **Cloud Storage Integration:** Integrate with services like AWS S3 or Azure Blob Storage to manage PDFs.


### Contributors
**Lal Dangal** (GitHub: @candidlpd)

**✨ Thank you for using the Contract QA System! 🚀**
For any questions or contributions, feel free to open an issue or submit a pull request.









