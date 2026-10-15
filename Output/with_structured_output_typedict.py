from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated
load_dotenv()



model=ChatOpenAI(model="gpt-4o-mini")

class Review(TypedDict):
    summary:Annotated[str,'A brief summary of the review']
    sentiment:Annotated[str,'Return sentiment of the review either -ve or +ve']

structured_model=model.with_structured_output(Review)
result=structured_model.invoke("The headphones have excellent sound quality and comfortable ear cushions. The battery life is also impressive, but the microphone quality could be better. Overall, I am happy with the product and think it offers good value for money.")
print(result)