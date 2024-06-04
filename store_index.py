from src.helper import text_split,load_pdf,download_hugging_face_embedding
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os

load_dotenv()

extracted_data=load_pdf(r"../data/")

text_chunks= text_split(extracted_data)

embeddings=download_hugging_face_embedding()

index_name="medical-chatbot"

# creating embeddings for each of the chunk and storing
docsearch=PineconeVectorStore.from_texts([t.page_content for t in text_chunks],embeddings,index_name=index_name)