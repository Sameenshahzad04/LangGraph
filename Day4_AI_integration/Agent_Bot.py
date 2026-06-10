from typing import TypedDict,List
from langchain_core.messages import HumanMessage #lanchain category of messages, we will use HumanMessage to pass the human message to the LLM and get a response.
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph,START,END
from dotenv import load_dotenv


# 2. Initialize ChatOllama (No .env or API key required!)
llm = ChatOllama(model="llama3", temperature=0)

class AgentState(TypedDict):
    message: List[HumanMessage]
    
def process(state:AgentState) -> AgentState:
   
   #pass human message to the LLM and get a response
   response = llm.invoke(state["message"])
   print(f"\nAI:{response.content}\n")

   return state

#creating graph

graph=StateGraph(AgentState)
graph.add_node("process",process)
graph.add_edge(START,"process")
graph.add_edge("process",END)   
agent=graph.compile()

# user_input = input("Enter your message: ")
# agent.invoke({"message":[HumanMessage(content=user_input)]})

# if we want that LLM work like chatbot -multiple human input


user_input=input("Enter:")
while user_input!="exit":

    agent.invoke({"message":[HumanMessage(content=user_input)]})
    user_input=input("Enter:")
#to run Python filename