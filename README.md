# 🤖 AI News Agent# 🤖 AI News Agent# 🤖 AI News Agent - Beginner's Guide

Multi-agent system that generates professional articles using local knowledge (RAG) + web search.An intelligent multi-agent system that generates professional news articles by combining local knowledge base (RAG) with real-time web search.A simple AI-powered news article generator that combines local knowledge with web search to create engaging healthcare articles.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)## 🚀 Quick Start

![Streamlit](https://img.shields.io/badge/Streamlit-1.45+-red.svg)

![CrewAI](https://img.shields.io/badge/CrewAI-Latest-orange.svg)![Streamlit](https://img.shields.io/badge/Streamlit-1.45+-red.svg)

## ✨ Features![CrewAI](https://img.shields.io/badge/CrewAI-Latest-orange.svg)### 1. Install Requirements

- 🔍 **Dual Search**: Local PDFs (RAG) + Web (Serper API)## ✨ Features```bash

- 🤖 **Multi-Agent**: Researcher + Writer working together

- 🌐 **Web UI**: ChatGPT-like Streamlit interfacepip install -r requirements.txt

- 📝 **Output**: Professional Markdown articles

- 🔍 **Dual Search System**: Local knowledge base (RAG) + Web search (Serper API)```

## 🚀 Quick Start

- 🤖 **Multi-Agent Architecture**: Research and Writer agents working collaboratively

### 1. Installation

- 🌐 **Web Interface**: Clean Streamlit UI similar to ChatGPT/Gemini### 2. Set Up API Keys

`````bash

# Clone and setup- 📚 **Knowledge Base**: ChromaDB vector database for local document search

git clone https://github.com/Priyanshu-2811/News-Agent.git

cd News-Agent- 📝 **Markdown Output**: Professional articles ready to publishCreate a `.env` file in this directory with your API keys:



# Create virtual environment## 🚀 Quick Start```

python -m venv venv

venv\Scripts\activate  # WindowsGOOGLE_API_KEY=your_google_api_key_here

# source venv/bin/activate  # macOS/Linux

### PrerequisitesSERPER_API_KEY=your_serper_api_key_here

# Install dependencies

pip install -r requirements.txt````

`````

- Python 3.8 or higher

### 2. Configure API Keys

- Google AI API key (Gemini)**Get API Keys:**

Create `.env` file:

```env- Serper API key (for web search)

GOOGLE_API_KEY=your_google_api_key

SERPER_API_KEY=your_serper_api_key- **Google API Key**: Go to [Google AI Studio](https://aistudio.google.com/app/apikey) and create a free API key

```

### Installation- **Serper API Key**: Go to [Serper.dev](https://serper.dev/) and get a free API key (100 free searches)

**Get Keys:**

- [Google AI Studio](https://aistudio.google.com/app/apikey) - Free Gemini API

- [Serper.dev](https://serper.dev/) - 100 free searches

1. **Clone the repository**### 3. Set Up Knowledge Base

### 3. Setup Knowledge Base

`````bash

```bash

# Add PDF files to data/ folder, then:   git clone https://github.com/yourusername/ai-news-agent.git```bash

python loader.py

```   cd ai-news-agentpython loader.py



### 4. Run Application````



```bash2. **Create virtual environment**This will process the PDF files in the `data/` folder and create a searchable database.

streamlit run streamlit_app.py

```   ````bash

Open: `http://localhost:8501`

python -m venv venv### 4. Run the Application

## 📁 Structure

# Windows

`````

News-Agent/ venv\Scripts\activate**Option A: Streamlit Web Interface (Recommended for beginners)**

├── streamlit_app.py # Web interface

├── crew.py # Agent orchestrator # macOS/Linux

├── agents.py # Agent definitions

├── task.py # Task configs source venv/bin/activate```bash

├── tools.py # RAG + Web search

├── loader.py # Knowledge base setup ```streamlit run streamlit_app.py

├── data/ # Your PDF files ````

└── newsblog.md # Generated articles

````````



## 🎯 How It Works3. **Install dependencies**



1. **Input** → User enters topic   ```bash**Option B: Command Line**

2. **Research Agent** → Searches PDFs + Web

3. **Writer Agent** → Creates article   pip install -r requirements.txt

4. **Output** → Displays + saves Markdown

   ``````bash

## 🛠️ Tech Stack

python crew.py

- **CrewAI** - Multi-agent framework

- **Streamlit** - Web UI4. **Set up environment variables**```

- **Google Gemini** - LLM

- **ChromaDB** - Vector database

- **Serper** - Web search

- **LangChain** - Document processing   Create a `.env` file in the root directory:## 📁 Project Structure



## 🤝 Contributing   ```env



1. Fork the repo   GOOGLE_API_KEY=your_google_api_key_here```

2. Create feature branch (`git checkout -b feature/NewFeature`)

3. Commit changes (`git commit -m 'Add NewFeature'`)   SERPER_API_KEY=your_serper_api_key_here├── README.md                 # This guide

4. Push (`git push origin feature/NewFeature`)

5. Open Pull Request   ```├── requirements.txt          # Required Python packages



## 🐛 Troubleshooting├── .env                     # Your API keys (create this)



| Issue | Solution |   **Get API Keys:**├── streamlit_app.py         # Web interface

|-------|----------|

| Import errors | `pip install -r requirements.txt` |   - **Google AI (Gemini)**: [Google AI Studio](https://aistudio.google.com/app/apikey) - Free tier available├── crew.py                  # Main crew coordinator

| API errors | Check `.env` file and key quotas |

| No knowledge base | Run `python loader.py` |   - **Serper**: [Serper.dev](https://serper.dev/) - 100 free searches├── agents.py                # AI agent definitions

| ChromaDB warnings | Normal deprecation warnings - ignore |

├── task.py                  # Task definitions

## 📝 License

5. **Set up knowledge base**├── tools.py                 # Search tools

MIT License - see LICENSE file

   ├── loader.py                # Knowledge base setup

---

   Add your PDF files to the `data/` folder, then run:├── data/                    # PDF files to search

⭐ Star this repo if you find it helpful!

   ```bash├── chroma_db/              # Knowledge base (created by loader.py)

Made with ❤️ using CrewAI and Streamlit

   python loader.py└── newsblog.md             # Generated articles

```````

6. **Launch the application**## 🔧 How It Works

   ````bash

   streamlit run streamlit_app.py1. **🔍 Research Agent** searches local PDFs first, then web if needed

   ```2. **✍️ Writer Agent** creates engaging articles from the research

   ````

7. **📄 Output** is saved as a markdown file and displayed in the web interface

   The app will open in your browser at `http://localhost:8501`

## 🛠️ Troubleshooting

## 📁 Project Structure

**Import Errors**: Make sure all packages are installed with `pip install -r requirements.txt`

```

ai-news-agent/**API Key Errors**: Check your `.env` file has valid API keys

├── streamlit_app.py      # Streamlit web interface

├── crew.py               # CrewAI orchestrator**No Knowledge Base**: Run `python loader.py` to create the database from PDFs

├── agents.py             # Agent definitions (Researcher & Writer)

├── task.py               # Task configurations**ChromaDB Warnings**: These are normal deprecation warnings and don't affect functionality

├── tools.py              # Search tools (RAG + Web)

├── loader.py             # Knowledge base loader## 📚 For Beginners

├── retriever.py          # Vector database retriever

├── requirements.txt      # Python dependencies- **agents.py**: Defines the AI "workers" that do the research and writing

├── .env                  # API keys (create this)- **task.py**: Defines what jobs each agent needs to do

├── .gitignore           # Git ignore rules- **tools.py**: Contains the search functions (local PDFs + web search)

├── README.md            # Documentation- **crew.py**: Coordinates everything together

├── data/                # PDF files for knowledge base- **streamlit_app.py**: Creates the user-friendly web interface

├── chroma_db/           # Vector database (auto-generated)

└── newsblog.md          # Generated articles## 🎯 Customization

```

- Add more PDFs to the `data/` folder and run `loader.py` again

## 🎯 How It Works- Modify agent roles and tasks in `agents.py` and `task.py`

- Adjust rate limiting in `tools.py` if you have premium API access

1. **User Input**: Enter a topic in the Streamlit interface- Change topics in the Streamlit interface or `crew.py`

2. **Research Agent**:

   - Searches local knowledge base (PDFs) using RAG## 🆘 Support

   - Supplements with web search via Serper API

   - Analyzes and consolidates findingsIf you run into issues:

3. **Writer Agent**:

   - Transforms research into engaging article1. Check the terminal output for specific error messages

   - Structures content professionally2. Verify your API keys are valid and have quota remaining

   - Outputs as Markdown3. Ensure all required files are present in the project directory

4. **Output**: Article displayed in UI and saved to `newsblog.md`4. Try running `python -c "import streamlit; print('Streamlit works!')"` to test installations

## 🛠️ Configuration

### Agent Settings (agents.py)

- Modify agent roles, goals, and backstories
- Adjust LLM model and temperature

### Task Settings (task.py)

- Customize research and writing instructions
- Set output formats and requirements

### Tools Settings (tools.py)

- Configure ChromaDB settings
- Adjust search result limits
- Modify rate limiting

## 📚 Usage Examples

### Via Streamlit UI

1. Open `http://localhost:8501`
2. Enter your topic (e.g., "AI in Healthcare")
3. Click "Generate Article"
4. Download or copy the generated article

### Via Command Line

```python
from crew import crew

# Generate article
result = crew.kickoff({"topic": "Your Topic Here"})
print(result)
```

## 🧪 Technologies Used

- **CrewAI**: Multi-agent orchestration framework
- **Streamlit**: Web application framework
- **Google Gemini**: Large language model
- **ChromaDB**: Vector database for RAG
- **Serper API**: Web search integration
- **LangChain**: Document processing and embeddings

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- CrewAI for the multi-agent framework
- Google for Gemini API
- Serper for web search API
- Streamlit for the amazing UI framework

## 📧 Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter)

Project Link: [https://github.com/yourusername/ai-news-agent](https://github.com/yourusername/ai-news-agent)

## 🐛 Troubleshooting

**Import Errors**

- Ensure all packages are installed: `pip install -r requirements.txt`

**API Key Errors**

- Verify `.env` file exists with valid keys
- Check API key quotas and limits

**No Knowledge Base**

- Run `python loader.py` to create the database
- Ensure PDF files exist in `data/` folder

**ChromaDB Warnings**

- Deprecation warnings are normal and don't affect functionality

---

Made with ❤️ using CrewAI and Streamlit
````````
