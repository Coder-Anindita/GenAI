from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

load_dotenv()
prompt1=PromptTemplate(
    template="write a joke on {topic}",
    input_variables=["topic"]
)
prompt2=PromptTemplate(
    template="Explain the joke {joke}",
    input_variables=["joke"]
)
model=ChatOpenAI(model="gpt-4o-mini")
parser=StrOutputParser()

chain=RunnableSequence(prompt1,model,parser,prompt2,model,parser)
result=chain.invoke({"topic":"AI"})
print(result)
