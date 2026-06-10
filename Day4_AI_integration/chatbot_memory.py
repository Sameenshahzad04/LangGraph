import os
from typing import List, TypedDict,Union
from langchain_core.messages import HumanMessage,AIMessage #lanchain category of messages, we will use HumanMessage to pass the human message to the LLM and get a response.    
#a sort of datatype in langchain
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph,START,END
from dotenv import load_dotenv

#state of the chatbot:State is a dictionary that holds all the data flowing through your graph.
class AgentState(TypedDict):
    
    message:List[Union[HumanMessage,AIMessage]]
   

llm = ChatOllama(model="llama3", temperature=0)

#node
def process(state:AgentState) -> AgentState:
    
    """ this node will solve the req you input

    """
    response = llm.invoke(state["message"])
    print(f"\nAI:{response.content}\n\n")
    state["message"].append(AIMessage(content=response.content))
    
    return state


graph=StateGraph(AgentState)
graph.add_node("process",process)
graph.add_edge(START,"process") 
graph.add_edge("process",END)
agent=graph.compile()






conversation_history=[]
user_input=input("Enter:")

while user_input!="exit":
 
 conversation_history.append(HumanMessage(content =user_input))

 result=agent.invoke({"message":conversation_history})
 print(result["message"])
 conversation_history=result["message"]

 user_input=input("Enter:")



#problem:doesnot remember the state if i run the file again

# save state in db for practice in textfile

with open("logging.txt","w")as file:
   file.write("your conversation log:\n")
   
   for message in conversation_history:
        if isinstance(message,HumanMessage):
         file.write(f"you:{message.content}\n")
        elif isinstance(message,AIMessage):
           file.write(f"AI:{message.content}\n\n")
   file.write("End of conversation")

print("conversation save to logging.txt")