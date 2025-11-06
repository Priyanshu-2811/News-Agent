# 🤖 AI News Agent

An intelligent multi-agent system that generates professional news articles by combining local knowledge base (RAG) with real-time web search. The system uses specialized AI agents - a Research Agent for gathering information and a Writer Agent for creating engaging content.

**Perfect for:** Content creators, journalists, researchers, and anyone needing well-researched articles on any topic.

## 🚀 Quick Setup

```bash
pip install -r requirements.txt
python loader.py
streamlit run streamlit_app.py
```

## 🔑 API Keys Required

Create `.env` file:

```
GOOGLE_API_KEY=your_key
SERPER_API_KEY=your_key
```

Get keys: [Google AI](https://aistudio.google.com/app/apikey) | [Serper](https://serper.dev/)

## ✨ How It Works

The system operates using a sophisticated multi-agent workflow:

1. **Research Agent** → Searches your local PDF knowledge base first, then supplements with current web information
2. **Writer Agent** → Transforms research findings into well-structured, engaging articles with proper formatting
3. **Output** → Generates professional markdown articles ready for publishing

**Key Benefits:**

- Combines authoritative local sources with up-to-date web information
- Reduces hallucinations by grounding content in real documents
- Creates consistent, professional writing style
- Provides real-time progress tracking

## 📁 Project Structure

- `streamlit_app.py` - Clean web interface with ChatGPT-like experience
- `crew.py` - Orchestrates the multi-agent workflow
- `agents.py` - Defines Research and Writer AI agents with specific roles
- `tools.py` - RAG search for PDFs + Serper web search integration
- `loader.py` - Sets up ChromaDB vector database from your documents
- `data/` - Place your PDF knowledge base files here

**Technologies:** CrewAI framework, Streamlit UI, Google Gemini LLM, ChromaDB vector database, Serper web search

---

Made by [Priyanshu]
