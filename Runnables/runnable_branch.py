from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda,RunnableBranch
from dotenv import load_dotenv

load_dotenv()
model=ChatOpenAI(model="gpt-4o-mini")
parser=StrOutputParser()

prompt1=PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)
prompt2=PromptTemplate(
    template="Write a summary of the report {report}", 
    input_variables=["report"]

)
def word_count(text):
    return len(text.split())



sequence_chain=RunnableSequence(prompt1,model,parser)
branch_chain=RunnableBranch(
    (lambda x: word_count(x) > 500, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)
chain=RunnableSequence(sequence_chain,branch_chain)
result=chain.invoke({"topic":"AI"})
print(result)
