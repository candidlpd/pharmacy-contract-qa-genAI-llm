# **Contract QA System**

The **Contract QA System** is designed to process hundreds of PDF contracts, extract critical details, and answer user queries using a natural language model (GPT-4). It efficiently processes large volumes of contracts using OpenAI embeddings stored in **Pinecone**, enabling quick and scalable information retrieval.

---

## **Project Goals**

1. 🚀 **PDF Text Extraction**: Load and process large volumes of PDF files to extract text data.  
2. 🔍 **Chunking**: Break long texts into manageable chunks to generate embeddings efficiently.  
3. 📊 **Embeddings Generation**: Use OpenAI's API to convert text chunks into embeddings.  
4. 🗃️ **Vector Storage**: Store embeddings in **Pinecone** for fast, efficient vector search.  
5. 🤖 **Natural Language Querying**: Use GPT-4 to answer user queries contextually based on the contract data.  
6. ⚡ **Scalability**: Handle hundreds of PDFs and millions of text chunks with seamless performance.

---

## **Tech Stack**

| **Technology**       | **Purpose**                                             |
|-----------------------|---------------------------------------------------------|
| **Python 3.11+**      | Core programming language.                             |
| **PyPDF2**            | Extract and process text data from PDF files.          |
| **LangChain**         | Framework for building and orchestrating LLM applications. |
| **OpenAI GPT-4**      | Provides contextual and accurate answers to queries.   |
| **Pinecone**          | Vector database for storing and querying embeddings.   |
| **Azure**             | Cloud-hosting support for Pinecone services.           |

---

## **Project Structure**

```plaintext
contract_qa_project/
│
├── data/
│   └── contracts/          # Folder containing PDF contract files (100+ PDFs)
│
├── src/
│   ├── contract_qa_local.py        # Script for processing and querying PDFs
│   ├── contract_qa_100PDF.py       # Optimized script for 100+ PDFs
│   └── test.py                     # Test script for QA queries
│
├── embeddings/                     # (Optional) Directory for local embeddings
├── models/                         # (Optional) Pre-trained model files
├── README.md                       # Project documentation
└── requirements.txt                # Dependencies for the project



Workflow Overview
1. Text Extraction & Chunking
Extracts text from PDF contracts.
Splits text into 500-character chunks for efficient embedding generation.
2. Embeddings Generation
OpenAI's API generates embeddings for the text chunks.
Pinecone stores these embeddings for retrieval.
3. Querying the Contracts
Users ask questions in natural language, e.g.:
"What is the contract amount and end date for Contract 7?"
GPT-4 retrieves relevant data from Pinecone and provides precise answers.
Example Query
Input Question:

"What is the Contract Amount and End Date of Contract 7?"

Output Answer:

"The Contract Amount for Contract 7 is $100,000, and the End Date is 2026-12-31."

How to Run the Project
1. Install Dependencies
Run the following command to install required libraries:

bash
Copy code
pip install -r requirements.txt
2. Process PDF Contracts
Run the main script to process all PDFs:

bash
Copy code
python src/contract_qa_100PDF.py
3. Modify Query
Update the query in the script to suit your question:

python
Copy code
query = "What is the Contract Amount and End Date of Contract 7?"
4. View Results
The system will output the most relevant answer to your query, e.g.:

plaintext
Copy code
"The Contract Amount for Contract 7 is $100,000, and the End Date is 2026-12-31."
Git Workflow
Initial Push
To push the project for the first time to GitHub:

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
Adding New Files
To add and push new files or updates:

bash
Copy code
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
Scalability for 100+ PDFs
The contract_qa_100PDF.py script is optimized to handle hundreds of PDFs with the following features:

Batch Processing:

Processes PDFs in batches to optimize memory usage and prevent overloading.
Dynamic Chunking:

Automatically adjusts text chunk sizes for different contract lengths.
Parallel Processing (Optional):

Use multiprocessing to extract text from multiple PDFs simultaneously.
Efficient Upserts:

Vectors are upserted to Pinecone in batches of 100 to avoid API throttling.
Future Enhancements
🌟 Interactive GUI: Add a graphical interface for uploading PDFs and querying interactively.
⚡ Parallel Processing: Use multiprocessing for faster PDF processing.
📝 Detailed Logging: Add logging for monitoring and debugging the pipeline.
☁️ Cloud Storage: Integrate AWS S3 or Azure Blob for contract storage.
🔎 Analytics: Provide analytical insights into contract data.
Contributors
Lal Dangal - candidlpd
License
This project is licensed under the MIT License.

✨ Thank you for checking out the Contract QA System! ✨

🚀 Feel free to raise an issue or contribute to make this project even better!