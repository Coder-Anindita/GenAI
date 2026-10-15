from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
url='https://medium.com/@ragulnath255/all-you-need-to-know-about-dbms-c45258ca3b0a'
loader=WebBaseLoader(url)
docs=loader.load()

print(docs[0].page_content)