# 🧠 Intelligent Document Assistant

A powerful AI-driven assistant that enables intelligent querying and summarization over your documents using **LangChain**, **Mistral AI's LLM & embeddings**, and a **FAISS**-powered local vector store.

## 🚀 Features

- 🔍 **Semantic Search** over large document sets  
- 🤖 **Question Answering** powered by Mistral AI LLMs  
- 🧠 **Contextual Retrieval** using RAG (Retrieval-Augmented Generation)  
- 📚 Supports PDF, DOCX (customizable document loaders)  
- ⚡ Local **FAISS** vector store for fast similarity search  
- 🛠️ Modular, extensible, and easy to integrate with other apps  

## 📦 Tech Stack

- LangChain  
- Mistral AI API  
- FAISS (Facebook AI Similarity Search)  
- Python  
- Streamlit *(frontend)*  

## ⚙️ Setup Instructions

### Prerequisites

- **Python 3.10+** installed ([python.org](https://www.python.org/downloads/) or your package manager).  
- A **Mistral AI API key** from [console.mistral.ai](https://console.mistral.ai/) (you enter it in the app when you run it).

### 1. Clone the repository

```bash
git clone https://github.com/navaneethsanil/Intelligent-Document-Assistant.git
cd Intelligent-Document-Assistant
```

### 2. Create a virtual environment

**macOS / Linux (Terminal):**

```bash
python3 -m venv env
```


**Windows (Command Prompt or PowerShell):**

```bash
python -m venv env
```

If `python` is not found on Windows, try `py -m venv env`.

### 3. Activate the virtual environment

**macOS / Linux:**

```bash
source env/bin/activate
```

**Git Bash**
```bash
source env/Scripts/activate
```

**Windows — Command Prompt:**

```bash
env\Scripts\activate.bat
```

**Windows — PowerShell:**

```powershell
env\Scripts\Activate.ps1
```

If PowerShell blocks the script, run once as Administrator:  
`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

On macOS/Linux, use `pip3` if your system only exposes that name.

### 5. Run the application

```bash
streamlit run app.py
```

Your browser should open the app. Paste your **Mistral API key**, upload a PDF or DOCX, then use the chat screen to ask questions about the document.

## 🧠 How It Works

1. **Load Documents**: Upload PDF, or DOCX files for processing.
2. **Text Chunking & Embedding**: Documents are split into chunks and embedded using Mistral's `mistral-embed`.
3. **Vector Storage**: The embeddings are stored in a FAISS index for local retrieval.
4. **Query Processing**: User questions are matched with top-k relevant chunks and passed through a Mistral chat model to generate answers.

## 🖼️ Use Cases

- Summarize lengthy PDFs or reports  
- Extract key points from legal or technical documents  
- Search and answer questions over your personal knowledge base  
- Chat with uploaded research papers or manuals  


## 🙌 Acknowledgments
- **LangChain for enabling the RAG pipeline**

- **Mistral AI for their LLMs and embedding models**

- **FAISS for efficient vector similarity search**

- **Streamlit for seamless UI development**

