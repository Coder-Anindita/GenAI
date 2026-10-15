from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

prompt1 = PromptTemplate(
    template="Generate short notes for the following text:\n{text}",
    input_variables=["text"]
)

prompt2 = PromptTemplate(
    template="Make a quiz for this given text: {text} in MCQ format",
    input_variables=["text"]
)

prompt3 = PromptTemplate(
    template="Merge the provided notes and quiz into a single document.\n\n"
              "Notes:\n{notes}\n\n"
              "Quiz:\n{quiz}",
    input_variables=["notes", "quiz"]
)

model1 = ChatOpenAI(model="gpt-4o-mini")
model2 = ChatOpenAI(model="gpt-4o-mini")

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "notes": prompt1 | model1 | parser,
    "quiz": prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

result = chain.invoke({
    "text": """Newton’s Second Law of Motion

Newton’s Second Law of Motion is one of the fundamental laws of classical mechanics. It explains how the motion of an object changes when a force is applied to it. The law establishes a relationship between the force acting on an object, its mass, and the acceleration produced.

According to Newton’s Second Law of Motion, the rate of change of momentum of an object is directly proportional to the external force applied to it and takes place in the direction of the applied force.

For an object having constant mass:

F = ma

where F represents force, m represents mass, and a represents acceleration.

If the force increases while mass remains constant, acceleration increases. If the same force is applied to objects with different masses, the object with smaller mass experiences greater acceleration.

The SI unit of force is the newton (N).

1 N = 1 kg × 1 m/s²

Newton’s Second Law has many practical applications in everyday life and engineering. It helps explain the motion of vehicles, aircraft, machines, and sports equipment."""
})

print(result)

chain.get_graph().print_ascii()