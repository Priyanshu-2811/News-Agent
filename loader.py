from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

pdf_dir = "data/"
pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith(".pdf")]

all_docs = []
for file in pdf_files:
    loader = PyPDFLoader(os.path.join(pdf_dir, file))
    docs = loader.load()
    all_docs.extend(docs)

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_documents(all_docs)

vectordb = Chroma.from_documents(
    documents=chunks,
    embedding=embedding,
    persist_directory="chroma_db"
)
vectordb.persist()

print("PDFs embedded and stored in ChromaDB.")
