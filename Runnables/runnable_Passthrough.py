from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough
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

joke_genchain=RunnableSequence(prompt1,model,parser)
parallel_chain=RunnableParallel(
    {
        "joke":RunnablePassthrough(),
        "explanation":RunnableSequence(prompt2,model,parser)
    }
)
chain=RunnableSequence(joke_genchain,parallel_chain)

result=chain.invoke({"topic":"AI"})
print(result["joke"])
print("-----------------------------------------------------------")
print(result["explanation"])
