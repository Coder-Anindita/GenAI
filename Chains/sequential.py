from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

prompt1=PromptTemplate(
    template="Generate a detailed article on {topic}",
    input_variables=["topic"]
)
model=ChatOpenAI(model="gpt-4o-mini")

prompt2=PromptTemplate(
    template="summarize the article on {article} in just 3 lines",
    input_variables=["article"]
)

parser=StrOutputParser()
chain=prompt1 | model | parser | prompt2 | model | parser
result=chain.invoke({"topic":"black hole"})
print(result)
chain.get_graph().print_ascii()