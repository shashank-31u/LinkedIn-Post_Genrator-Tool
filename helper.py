from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

load_dotenv()

llm = ChatGroq(temperature=0, model_name="llama-3.3-70b-versatile",groq_api_key=os.getenv("GROQ_API_KEY"))

if __name__== "__main__":
    re=llm.invoke("What is the capital of India?")
    print(re)