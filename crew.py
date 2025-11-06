"""
🎬 AI News Agent - Crew Director
This file brings together the agents and tasks to create the final AI crew.
Think of it as a movie director coordinating actors (agents) to perform scenes (tasks).

The crew executes tasks sequentially:
1. Research Agent finds information
2. Writer Agent creates the article
"""

from crewai import Crew, Process
from task import research_task, write_task
from agents import news_research_agent, news_writer_agent

# Create the AI crew with optimized settings for beginners
crew = Crew(
    agents=[news_research_agent, news_writer_agent],  # Our two AI agents
    tasks=[research_task, write_task],                # Their tasks to complete
    process=Process.sequential,                       # Run tasks one after another
    verbose=False,                                    # Reduced logging for cleaner output
    max_rpm=10                                        # Rate limit: 10 requests per minute
)

# Example execution (commented out so it doesn't run automatically)
# To run the crew, use: results = crew.kickoff({"topic": "AI in Healthcare"})
if __name__ == "__main__":
    print("🎬 AI News Crew is ready!")
    print("   To run: results = crew.kickoff({'topic': 'Your Topic Here'})")
    print("   Or use the Streamlit interface: streamlit run streamlit_app.py")

