from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Load vector store
vectordb = Chroma(persist_directory="chroma_db", embedding_function=embedding)

def retrieve_from_rag(query):
    results = vectordb.similarity_search(query, k=3)
    return "\n\n".join([doc.page_content for doc in results])
