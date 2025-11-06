"""
🤖 AI News Agent - Simple Streamlit Interface
Generate AI-powered news articles with local knowledge and web search
"""

import streamlit as st
import os
import time
from datetime import datetime

# Import our AI crew
try:
    from crew import crew
    from dotenv import load_dotenv
    load_dotenv()
except ImportError as e:
    st.error(f"❌ Import Error: {e}")
    st.stop()

# Configure the page
st.set_page_config(
    page_title="🤖 AI News Agent",
    page_icon="📰",
    layout="wide"
)

def check_setup():
    """Check if all required components are available"""
    issues = []
    
    # Check API keys
    if not os.getenv("GOOGLE_API_KEY"):
        issues.append("❌ Missing GOOGLE_API_KEY in .env file")
    if not os.getenv("SERPER_API_KEY"):
        issues.append("❌ Missing SERPER_API_KEY in .env file")
    
    # Check knowledge base
    if not os.path.exists("chroma_db"):
        issues.append("❌ Knowledge base not found - please run loader.py first")
    
    return issues

def generate_article(topic):
    """Generate an article using our AI crew"""
    
    # Create progress indicators
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    try:
        # Step 1: Initialize
        status_text.text("🔄 Initializing AI agents...")
        progress_bar.progress(20)
        time.sleep(1)
        
        # Step 2: Research
        status_text.text("🔍 Research agent searching for information...")
        progress_bar.progress(40)
        time.sleep(1)
        
        # Step 3: Writing
        status_text.text("✍️ Writer agent creating the article...")
        progress_bar.progress(70)
        
        # Execute the crew with the topic
        result = crew.kickoff({"topic": topic})
        
        # Step 4: Complete
        progress_bar.progress(100)
        status_text.text("✅ Article generated successfully!")
        
        # Show success message
        st.success("🎉 Article generated and saved to newsblog.md!")
        
        # Set flag to show the article was just generated
        st.session_state.article_generated = True
        st.session_state.current_topic = topic
        
        # Clear progress indicators
        progress_bar.empty()
        status_text.empty()
        
        # Rerun to refresh the page and show the article
        st.rerun()
            
    except Exception as e:
        progress_bar.progress(0)
        status_text.text("")
        st.error(f"❌ Error generating article: {str(e)}")
        
        with st.expander("🔍 Error Details"):
            st.code(str(e))

def main():
    """Main Streamlit application"""
    
    # Initialize session state
    if 'article_generated' not in st.session_state:
        st.session_state.article_generated = False
    if 'current_topic' not in st.session_state:
        st.session_state.current_topic = ""
    
    # Header
    st.title("🤖 AI News Agent")
    st.markdown("Generates professional news articles using AI agents with RAG and SERPER web search.")
    
    # Check system setup
    issues = check_setup()
    
    if issues:
        st.error("⚠️ Setup Issues Found:")
        for issue in issues:
            st.write(issue)
        
        st.info("""
        **Setup Instructions:**
        1. Create a `.env` file with your API keys:
           - GOOGLE_API_KEY=your_google_api_key
           - SERPER_API_KEY=your_serper_api_key
        2. Run `python loader.py` to set up the knowledge base
        """)
        return
    
    # Show setup is good
    st.success("✅ System ready to generate articles!")
    
    # Input section
    st.markdown("## 📝 Article Generation")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        topic = st.text_input(
            "What topic would you like to write about?", 
            value="AI in Healthcare",
            help="Enter any topic you'd like the AI agents to research and write about"
        )
    
    with col2:
        st.write("")  # Spacing
        st.write("")  # Spacing
        generate_button = st.button("🚀 Generate Article", type="primary", use_container_width=True)
      # Generate article when button is clicked
    if generate_button:
        if topic.strip():
            # Reset the article_generated flag when generating new article
            st.session_state.article_generated = False
            generate_article(topic)
        else:
            st.warning("⚠️ Please enter a topic first!")
    
    # Show article ONLY after user has generated one (like ChatGPT/Gemini)
    if st.session_state.article_generated and os.path.exists("newsblog.md"):
        st.markdown("---")
        
        # Read the article content
        with open("newsblog.md", "r", encoding="utf-8") as f:
            content = f.read()
        
        # Show generated article with topic
        st.markdown(f"## 📰 Generated Article: {st.session_state.current_topic}")
        st.success("🎉 Article successfully generated!")
        
        # Display the article content
        st.markdown(content)
        
        # Download button
        st.download_button(
            label="📥 Download Article",
            data=content,
            file_name=f"article_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
            mime="text/markdown",
            use_container_width=True
        )

if __name__ == "__main__":
    main()
