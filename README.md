# 🧠 Intelligent Document Assistant

A powerful AI-driven assistant that enables intelligent querying and summarization over your documents using **LangChain**, **OpenAI's LLM & embeddings**, and a **FAISS**-powered local vector store.

## 🚀 Features

- 🔍 **Semantic Search** over large document sets  
- 🤖 **Question Answering** powered by OpenAI LLMs  
- 🧠 **Contextual Retrieval** using RAG (Retrieval-Augmented Generation)  
- 📚 Supports PDF, DOCX (customizable document loaders)  
- ⚡ Local **FAISS** vector store for fast similarity search  
- 🛠️ Modular, extensible, and easy to integrate with other apps  

## 📦 Tech Stack

- LangChain  
- OpenAI API  
- FAISS (Facebook AI Similarity Search)  
- Python  
- Streamlit *(frontend)*  

## ⚙️ Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/navaneethsanil/Intelligent-Document-Assistant.git
cd intelligent-document-assistant
```

2. **Create virtual enviornment**

```bash
python -m venv env
source env/scripts/activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```


4. **Run the Application**

```bash
streamlit run app.py
```

## 🧠 How It Works

1. **Load Documents**: Upload PDF, or DOCX files for processing.
2. **Text Chunking & Embedding**: Documents are split into chunks and embedded using OpenAI's `text-embedding-3-small`.
3. **Vector Storage**: The embeddings are stored in a FAISS index for local retrieval.
4. **Query Processing**: User questions are matched with top-k relevant chunks and passed through OpenAI's LLM to generate answers.

## 🖼️ Use Cases

- Summarize lengthy PDFs or reports  
- Extract key points from legal or technical documents  
- Search and answer questions over your personal knowledge base  
- Chat with uploaded research papers or manuals  


## 🙌 Acknowledgments
- **LangChain for enabling the RAG pipeline**

- **OpenAI for their powerful LLMs and embedding models**

- **FAISS for efficient vector similarity search**

- **Streamlit for seamless UI development**

