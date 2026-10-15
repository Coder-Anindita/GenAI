from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
chatModel=ChatOpenAI(model="gpt-4o-mini")
result=chatModel.invoke("What is the capital of india?",temperature=2)
print(result.content)
