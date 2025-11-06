"""
🤖 AI News Agent - Agent Definitions
This file creates the two AI agents that work together:
1. Research Agent - Finds and analyzes information from multiple sources
2. Writer Agent - Creates engaging, accessible articles

Both agents use Google's Gemini AI model as their "brain"
"""

from crewai import Agent, LLM
from tools import tool, rag_tool
from dotenv import load_dotenv
import os

load_dotenv()

# Create a Google Gemini agent using CrewAI's LLM with optimized settings
llm = LLM(
    model="gemini/gemini-1.5-flash",    # Google's fast, efficient model
    api_key=os.getenv("GOOGLE_API_KEY"), # Your API key from .env file
    temperature=0.5,                    # Controls creativity (0=factual, 1=creative)
    max_tokens=1000                     # Limit output length to manage costs
)

print("🤖 Initializing AI Agents...")

# AGENT 1: Research Agent
# This agent finds information by searching local knowledge base first, then web
news_research_agent = Agent(
    role="Healthcare AI Researcher",
    goal='Uncover the latest advancements in {topic}. First search local knowledge base, then supplement with web search if needed.',
    verbose=True,
    memory=True,
    backstory=(
        "You are an expert AI researcher specializing in healthcare technology. "
        "You always start by searching the local knowledge base first, then use web search "
        "to find the most current information. You avoid repeating searches and focus on "
        "providing comprehensive insights efficiently."
    ),
    tools=[rag_tool, tool],  # RAG tool first to prioritize local search
    llm=llm,
    allow_delegation=False,  # Prevent infinite delegation loops
    max_iter=3,  # Limit iterations to prevent loops
    max_execution_time=300  # 5-minute timeout
)

# AGENT 2: Writer Agent
# This agent creates engaging articles based on the research findings
news_writer_agent = Agent(
    role="Healthcare Content Writer",
    goal="Create a well-structured, engaging article based on research findings. Focus on clarity and accessibility.",
    backstory=(
        "You are a skilled healthcare content writer who specializes in making complex "
        "AI and medical topics accessible to general audiences. You create comprehensive "
        "articles based on research findings without needing to do additional searches."
    ),
    verbose=True,
    memory=True,
    llm=llm,
    allow_delegation=False,  # Prevent delegation loops
    max_iter=2,  # Limit iterations for writing tasks
    max_execution_time=240  # 4-minute timeout
)
