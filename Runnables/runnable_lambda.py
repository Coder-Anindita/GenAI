from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda
from dotenv import load_dotenv

load_dotenv()

prompt1=PromptTemplate(
    template="Generate a joke on {topic}",
    input_variables=["topic"]
)   
prompt2=PromptTemplate(
    template="Generate a explanation of the joke {joke}", 
    input_variables=["joke"]
)

model=ChatOpenAI(model="gpt-4o-mini")
parser=StrOutputParser()
def word_count(text):
    return len(text.split())

joke_genchain=RunnableSequence(prompt1,model,parser)
parallel_chain=RunnableParallel(
    { 
        
        "joke":RunnablePassthrough(),
        "word_count":RunnableLambda(word_count)
        

    }
)
final_chain=RunnableSequence(joke_genchain,parallel_chain)
result=final_chain.invoke({"topic":"AI"})
print(result["joke"])
print("-----------------------------------------------------------")
print(result["word_count"])