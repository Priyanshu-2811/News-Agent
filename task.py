"""
📋 AI News Agent - Task Definitions
This file defines what work each AI agent needs to do:
1. Research Task - Find and analyze information about the topic
2. Writing Task - Create an engaging article based on the research

The tasks run sequentially: research first, then writing.
"""

from crewai import Task
from tools import tool, rag_tool
from agents import news_research_agent, news_writer_agent

# TASK 1: Research Task
# Assigned to the Research Agent to find comprehensive information
research_task = Task(
    description=(
        "Research comprehensive information about {topic}. "
        "SEARCH STRATEGY: Use knowledge base search to find foundational research, then supplement with current web information if needed. "
        "Focus on: key developments, applications, benefits, challenges, and future prospects. "
        "Provide a balanced analysis with both established research and current trends."
    ),
    
    expected_output="A comprehensive 3 paragraphs research summary covering established research and current developments.",
    tools=[rag_tool, tool],  # Both tools available - knowledge base first, web as supplement
    agent=news_research_agent,
)

# TASK 2: Writing Task  
# Assigned to the Writer Agent to create the final article
write_task = Task(
    description=(
        "Create an engaging article about {topic} based on the research provided. "
        "DO NOT perform additional searches unless absolutely necessary for current statistics. "
        "Focus on transforming the research into an accessible, positive, and informative article. "
        "Use the research findings as your primary source."
    ),
    expected_output="A 4 paragraph article on {topic} advancements formatted as markdown.",
    tools=[],  # No tools - rely on research task output to avoid duplication
    agent=news_writer_agent,
    async_execution=False,
    output_file='newsblog.md'
)
