"""
📚 AI News Agent - Search Tools
This file contains two main tools for finding information:
1. KnowledgeBaseTool - Searches our local PDF database (ChromaDB)
2. WebSearchTool - Searches the internet for current information

The tools work together: local knowledge first, then web search if needed.
"""

from crewai_tools import SerperDevTool
from crewai.tools import BaseTool
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from typing import Type
from pydantic import BaseModel, Field
import os
import time
import warnings

# Suppress deprecation warnings for cleaner output
warnings.filterwarnings("ignore", category=DeprecationWarning)

load_dotenv()
os.environ['SERPER_API_KEY'] = os.getenv("SERPER_API_KEY")

# Rate limiting variables
last_google_api_call = 0
last_serper_api_call = 0
GOOGLE_API_DELAY = 2  # 2 seconds between Google API calls
SERPER_API_DELAY = 3  # 3 seconds between Serper API calls

# Simple ChromaDB search function
def search_knowledge_base(query: str) -> str:
    """Search the local ChromaDB for relevant health information"""
    global last_google_api_call
    print(f"🔍 Searching knowledge base for: {query[:50]}...")
    
    try:
        # Rate limit Google API calls
        current_time = time.time()
        time_since_last_call = current_time - last_google_api_call
        if time_since_last_call < GOOGLE_API_DELAY:
            sleep_time = GOOGLE_API_DELAY - time_since_last_call
            time.sleep(sleep_time)
        
        # Initialize embeddings
        embeddings = GoogleGenerativeAIEmbeddings(
            model="models/embedding-001",
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )
        last_google_api_call = time.time()
        
        # Connect to existing ChromaDB
        vectorstore = Chroma(
            persist_directory="chroma_db",
            embedding_function=embeddings
        )
        
        # Search for relevant documents
        docs = vectorstore.similarity_search(query, k=3)
        
        if not docs:
            print("❌ No relevant information found in knowledge base.")
            return "No relevant information found in knowledge base."
        
        # Get unique sources for better reporting
        sources = set()
        for doc in docs:
            source_path = doc.metadata.get('source', '')
            if source_path:
                source_file = source_path.split('/')[-1]
                sources.add(source_file)
        
        sources_list = list(sources)
        print(f"✅ Found {len(docs)} chunks from: {', '.join(sources_list)}")
        
        # Format results more concisely
        results = []
        for i, doc in enumerate(docs, 1):
            content = doc.page_content[:400] + "..." if len(doc.page_content) > 400 else doc.page_content
            source = doc.metadata.get('source', 'Unknown').split('/')[-1]
            results.append(f"[{source}] {content}")
        
        return "\n\n".join(results)
        
    except Exception as e:
        print(f"❌ Knowledge base error: {str(e)}")
        return f"Error accessing knowledge base: {str(e)}"

# Simple web search function
def web_search(query: str) -> str:
    """Search the web for current information"""
    global last_serper_api_call
    print(f"🌐 Searching web for: {query[:50]}...")
    
    try:
        # Rate limit Serper API calls
        current_time = time.time()
        time_since_last_call = current_time - last_serper_api_call
        if time_since_last_call < SERPER_API_DELAY:
            sleep_time = SERPER_API_DELAY - time_since_last_call
            time.sleep(sleep_time)
        
        # Use SerperDevTool correctly
        serper = SerperDevTool()
        result = serper._run(query=query)
        last_serper_api_call = time.time()
        print("✅ Web search completed!")
        return result
    except Exception as e:
        print(f"❌ Web search failed: {str(e)}")
        return f"Web search error: {str(e)}"

# Input schemas for the tools
class SearchInput(BaseModel):
    """Input for search tools"""
    query: str = Field(..., description="The search query")

# ChromaDB search tool
class KnowledgeBaseTool(BaseTool):
    name: str = "Knowledge Base Search"
    description: str = "Search local health articles database for relevant information. Use this FIRST before web search."
    args_schema: Type[BaseModel] = SearchInput

    def _run(self, query: str) -> str:
        # Handle both string and dict inputs gracefully
        if isinstance(query, dict):
            if 'query' in query:
                actual_query = query['query']
            elif 'description' in query:
                actual_query = query['description']
            else:
                actual_query = str(query)
        else:
            actual_query = str(query)
        
        return search_knowledge_base(actual_query)

# Web search tool  
class WebSearchTool(BaseTool):
    name: str = "Web Search"
    description: str = "Search the web for current news and information. Use this ONLY if knowledge base search doesn't provide enough information."
    args_schema: Type[BaseModel] = SearchInput

    def _run(self, query: str) -> str:
        # Handle both string and dict inputs gracefully
        if isinstance(query, dict):
            if 'query' in query:
                actual_query = query['query']
            elif 'description' in query:
                actual_query = query['description']
            else:
                actual_query = str(query)
        else:
            actual_query = str(query)
        
        return web_search(actual_query)

# Create tool instances
rag_tool = KnowledgeBaseTool()
tool = WebSearchTool()

print("✅ Tools initialized successfully. RAG functionality active")
