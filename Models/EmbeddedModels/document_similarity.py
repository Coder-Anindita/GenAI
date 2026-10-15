from langchain_openai import OpenAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from dotenv import load_dotenv
load_dotenv()
embedding_Model=OpenAIEmbeddings(model="text-embedding-3-large",dimensions=300)
documents=[
    "Rohit Sharma is a right-handed Indian batsman.",
    "Virat Kohli is a right-handed Indian batsman.",
    "Jasprit Bumrah is an Indian fast bowler.",
    "Ravindra Jadeja is an Indian all-rounder.",
    "KL Rahul is an Indian wicketkeeper-batsman.",
    "Hardik Pandya is an Indian all-rounder.",
    "Shubman Gill is an Indian opening batsman.",
    "Rishabh Pant is an Indian wicketkeeper-batsman.",
    "Mohammed Siraj is an Indian fast bowler.",
    "Kuldeep Yadav is an Indian left-arm wrist spinner."
]
query="Tell me about Rohit."
doc_embedding=embedding_Model.embed_documents(documents)
query_embedding=embedding_Model.embed_query(query)
similar=(cosine_similarity([query_embedding],doc_embedding))
index,score=sorted(list(enumerate(similar[0])),key=lambda x:x[1])[-1]
print(query)
print(documents[index])
print("similarity score is:",score)



