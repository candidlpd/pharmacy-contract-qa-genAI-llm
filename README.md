<div class="markdown prose w-full break-words dark:prose-invert light"><p>Here's the complete content formatted to match the clean and consistent style you provided:</p><hr><h1><strong>Contract QA System</strong></h1><p>This repository contains a <strong>Contract QA (Question-Answering) System</strong> designed to process hundreds of PDF contracts, extract critical information, and answer user queries using a natural language model. The system uses <strong>OpenAI embeddings</strong> and stores the data in <strong>Pinecone</strong> for efficient retrieval and querying.</p><hr><h1><strong>Project Goals</strong></h1><h2>1. <strong>PDF Text Extraction</strong></h2><ul><li>Load and process large volumes of PDF contracts to extract text.</li></ul><h2>2. <strong>Chunking</strong></h2><ul><li>Split long contract texts into smaller, <strong>500-character chunks</strong> for efficient processing.</li></ul><h2>3. <strong>Embeddings Generation</strong></h2><ul><li>Use OpenAI's API to generate embeddings for the text chunks.</li><li>Store the embeddings in Pinecone for efficient retrieval.</li></ul><h2>4. <strong>Natural Language Querying</strong></h2><ul><li>Use GPT-4 to answer user queries in <strong>natural language</strong> based on the stored embeddings.</li></ul><h2>5. <strong>Scalability</strong></h2><ul><li>Process hundreds of PDFs efficiently using optimized batch processing and parallel execution.</li></ul><hr><h1><strong>Tech Stack</strong></h1><table><thead><tr><th><strong>Technology</strong></th><th><strong>Purpose</strong></th></tr></thead><tbody><tr><td><strong>Python 3.11+</strong></td><td>Core programming language</td></tr><tr><td><strong>PyPDF2</strong></td><td>Extract and process text data from PDF files</td></tr><tr><td><strong>LangChain</strong></td><td>Framework to build LLM-powered workflows</td></tr><tr><td><strong>OpenAI GPT-4</strong></td><td>Language model for generating answers</td></tr><tr><td><strong>Pinecone</strong></td><td>Vector database for fast storage and retrieval</td></tr><tr><td><strong>Azure</strong></td><td>Cloud-hosting support for Pinecone services</td></tr></tbody></table><hr><h1><strong>Project Structure</strong></h1><pre class="!overflow-visible"><div class="contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary dark:bg-gray-950"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none">plaintext</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-sidebar-surface-primary px-2 font-sans text-xs text-token-text-secondary dark:bg-token-main-surface-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center select-none py-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy code</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-plaintext">
# Project Structure: CONTRACT_QA_PROJECT

```plaintext
CONTRACT_QA_PROJECT/
│
├── .vscode/               # VS Code configuration files
│
├── config/                # Configuration files for the project
│
├── data/                  # Folder to store PDF files and datasets
│
├── embeddings/            # Directory to manage embeddings
│
├── models/                # Model checkpoints or custom models
│
├── notebooks/             # Jupyter notebooks for experiments
│
├── src/                   # Source code for the project
│   ├── contract_qa_local_100PDF.py  # Main script for processing 100+ PDFs
│   ├── contract_qa_local.py         # Local script for querying contracts
│   └── test.py                      # Script for testing the workflow
│
├── .env                   # Environment variables (e.g., API keys)
├── .gitignore             # Ignore files (e.g., .env, cache, models)
└── README.md              # Documentation of the project

</code></div></div></pre><hr><h1><strong>Workflow Overview</strong></h1><h2>1. <strong>Text Extraction &amp; Chunking</strong></h2><ul><li>Extracts text from PDF contracts.</li><li>Splits text into <strong>500-character chunks</strong> for efficient embedding generation.</li></ul><h2>2. <strong>Embeddings Generation</strong></h2><ul><li>OpenAI's API generates embeddings for the text chunks.</li><li>Pinecone stores these embeddings for retrieval.</li></ul><h2>3. <strong>Querying the Contracts</strong></h2><ul><li><p>Users ask questions in <strong>natural language</strong>, e.g.:</p><blockquote><p><strong>"What is the contract amount and end date for Contract 7?"</strong></p></blockquote></li><li><p>GPT-4 retrieves relevant data from Pinecone and provides precise answers.</p></li></ul><hr><h1><strong>Example Query</strong></h1><h2><strong>Input Question</strong></h2><pre class="!overflow-visible"><div class="contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary dark:bg-gray-950"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none">plaintext</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-sidebar-surface-primary px-2 font-sans text-xs text-token-text-secondary dark:bg-token-main-surface-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center select-none py-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy code</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-plaintext">"What is the Contract Amount and End Date of Contract 7?"
</code></div></div></pre><h2><strong>Output Answer</strong></h2><pre class="!overflow-visible"><div class="contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary dark:bg-gray-950"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none">plaintext</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-sidebar-surface-primary px-2 font-sans text-xs text-token-text-secondary dark:bg-token-main-surface-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center select-none py-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy code</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-plaintext">"The Contract Amount for Contract 7 is $100,000, and the End Date is 2026-12-31."
</code></div></div></pre><hr><h1><strong>How to Run the Project</strong></h1><h2>1. <strong>Install Dependencies</strong></h2><p>Run the following command to install all required libraries:</p><pre class="!overflow-visible"><div class="contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary dark:bg-gray-950"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none">bash</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-sidebar-surface-primary px-2 font-sans text-xs text-token-text-secondary dark:bg-token-main-surface-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center select-none py-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy code</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">pip install -r requirements.txt
</code></div></div></pre><h2>2. <strong>Process PDFs and Query Contracts</strong></h2><p>Run the script to process PDF files and query contract data:</p><pre class="!overflow-visible"><div class="contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary dark:bg-gray-950"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none">bash</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-sidebar-surface-primary px-2 font-sans text-xs text-token-text-secondary dark:bg-token-main-surface-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center select-none py-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy code</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">python src/contract_qa_100PDF.py
</code></div></div></pre><h2>3. <strong>Modify Query</strong></h2><p>To change the query, update the following line in the script:</p><pre class="!overflow-visible"><div class="contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary dark:bg-gray-950"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none">python</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-sidebar-surface-primary px-2 font-sans text-xs text-token-text-secondary dark:bg-token-main-surface-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center select-none py-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy code</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-python">query = <span class="hljs-string">"What is the Contract Amount and End Date of Contract 7?"</span>
</code></div></div></pre><hr><h1><strong>Git Workflow</strong></h1><h2><strong>Initial Push to Remote Repository</strong></h2><pre class="!overflow-visible"><div class="contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary dark:bg-gray-950"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none">bash</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-sidebar-surface-primary px-2 font-sans text-xs text-token-text-secondary dark:bg-token-main-surface-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center select-none py-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy code</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash"><span class="hljs-comment"># Navigate to your project directory</span>
<span class="hljs-built_in">cd</span> H:\Lilly_Projects\contract_qa_project

<span class="hljs-comment"># Initialize Git and add the remote repository</span>
git init
git remote add origin https://github.com/candidlpd/contract_qa_project.git

<span class="hljs-comment"># Create and switch to the 'feature' branch</span>
git checkout -b feature

<span class="hljs-comment"># Stage and commit all files</span>
git add .
git commit -m <span class="hljs-string">"Initial commit: Added Contract QA Project"</span>

<span class="hljs-comment"># Push to the remote repository</span>
git push -u origin feature
</code></div></div></pre><h2><strong>Adding New Files or Updates</strong></h2><p>To add and push new files like <code>contract_qa_100PDF.py</code> and updated data:</p><pre class="!overflow-visible"><div class="contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary dark:bg-gray-950"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none">bash</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-sidebar-surface-primary px-2 font-sans text-xs text-token-text-secondary dark:bg-token-main-surface-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center select-none py-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy code</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash"><span class="hljs-comment"># Check current branch</span>
git status
git branch

<span class="hljs-comment"># Ensure you're on the 'feature' branch</span>
git checkout feature

<span class="hljs-comment"># Add new files and updates</span>
git add src/contract_qa_100PDF.py data/contracts/* README.md

<span class="hljs-comment"># Commit changes with a descriptive message</span>
git commit -m <span class="hljs-string">"Added contract_qa_100PDF.py and updated contract data files"</span>

<span class="hljs-comment"># Pull and rebase to avoid conflicts</span>
git pull origin feature --rebase

<span class="hljs-comment"># Push changes to remote repository</span>
git push origin feature
</code></div></div></pre><hr><h1><strong>Scalability for 100+ PDFs</strong></h1><p>The <code>contract_qa_100PDF.py</code> script is optimized for handling large volumes of PDF files efficiently. Key features include:</p><ul><li><strong>Batch Processing</strong>: Process text extraction and embeddings in manageable batches.</li><li><strong>Parallel Execution</strong>: Optional use of Python's <code>multiprocessing</code> for faster processing.</li><li><strong>Dynamic Chunking</strong>: Handles varying text lengths dynamically.</li><li><strong>Efficient Upserts</strong>: Avoid API throttling by upserting vectors to Pinecone in small batches.</li></ul><hr><h1><strong>Future Enhancements</strong></h1><ol><li><strong>Add GUI</strong>: Develop a user-friendly interface for uploading PDFs and asking queries interactively.</li><li><strong>Parallel Processing</strong>: Use job queues or multiprocessing for faster text extraction and embeddings.</li><li><strong>Logging</strong>: Add detailed logging for better debugging and monitoring.</li><li><strong>Cloud Storage Integration</strong>: Integrate with services like <strong>AWS S3</strong> or <strong>Azure Blob Storage</strong> to manage PDFs.</li></ol><hr><h1><strong>Contributors</strong></h1><ul><li><strong>Lal Dangal</strong> (<a rel="noopener" target="_new" style="--streaming-animation-state: var(--batch-play-state-1); --animation-rate: var(--batch-play-rate-1);" href="https://github.com/candidlpd"><span style="--animation-count: 16; --streaming-animation-state: var(--batch-play-state-2);">@candidlpd</span></a>)</li></ul><hr><p>✨ <strong>Thank you for using the Contract QA System! 🚀</strong><br>For any questions or contributions, feel free to open an issue or submit a pull request.</p><hr><pre class="!overflow-visible"><div class="contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary dark:bg-gray-950"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none">markdown</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-sidebar-surface-primary px-2 font-sans text-xs text-token-text-secondary dark:bg-token-main-surface-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center select-none py-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy code</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-markdown">
<span class="hljs-section">### <span class="hljs-strong">**How to Use**</span></span>
<span class="hljs-bullet">1.</span> Copy the above content into your <span class="hljs-code">`README.md`</span> file.
<span class="hljs-bullet">2.</span> Save the file and push it to your remote repository.
<span class="hljs-bullet">3.</span> GitHub will render this with bullet points, highlights, and proper headings.

Let me know if you need additional formatting or changes! 🚀
</code></div></div></pre></div>