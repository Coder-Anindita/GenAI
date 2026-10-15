from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Literal

load_dotenv()
model=ChatOpenAI(model="gpt-4o-mini")
class Feedback(BaseModel):
    sentiment:Literal['positive','negative']=Field(description="Give the sentiment of the feedback")

parser=StrOutputParser()
parser2=PydanticOutputParser(pydantic_object=Feedback)

prompt1=PromptTemplate(
    template="Classify the sentiment of the following feedback {feedback} as either positive or negative.\n {format_instructions}",
    input_variables=["feedback"],
    partial_variables={"format_instructions":parser2.get_format_instructions()}

)
prompt2=PromptTemplate(
    template="Write an appropriate response to the following positive feedback {feedback}.",
    input_variables=["feedback"],
    
)
prompt3=PromptTemplate(
    template="Write an appropriate response to the following negative feedback {feedback}.",
    input_variables=["feedback"],
    

)

classification_chain=prompt1 | model | parser2

branch_chain=RunnableBranch(
    (lambda x:x.sentiment=="positive",prompt2 | model | parser),
    (lambda x:x.sentiment=="negative",prompt3 | model | parser),
    RunnableLambda(lambda x: "Invalid sentiment")

)
chain=classification_chain | branch_chain
result=chain.invoke({"feedback":"The product is bad and I am not satisfied with it."})
print(result)

