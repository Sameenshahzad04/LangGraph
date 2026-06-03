#%%
from typing import Dict, TypedDict
from langgraph.graph import StateGraph
#framework  that help you to design and manage the flow oftasks in your applicatio using graph structure

# to view graph
from  IPython.display import display,Image



# we now create an AgentState- shared state that can be
#  accessed and modified by all tasks in the graph.
#  This allows us to maintain a consistent state across
#  different tasks and enables communication between them.
#state schema

#%%
class AgentState(TypedDict):
    messages: str
    
# defining a node:a step in the graph that represents a specific task or action.in general python function can be a node in the graph, but we can also define custom nodes that encapsulate specific logic or behavior.

def greeting_node(state: AgentState) -> AgentState:

    """Simple node that adds a greeting message to the state"""

    state['messages'] = "hey"+state['messages']+" how are you doing?   "
    return state

# %%
#create a graph
graph = StateGraph(AgentState)

# add the greeting node to the graph(name of node, action it performs)
graph.add_node("greeter", greeting_node)

#in workflow we have start-node-end nodes.The start node is the entry point
#  of the graph, where the execution begins. 
# The end node is the exit point of the graph, where the execution ends.
#  We can define the flow of tasks by connecting nodes together, specifying
#  the order in which they should be executed.

graph.set_entry_point("greeter")
graph.set_finish_point("greeter")

app=graph.compile()

# Generate and display the PNG graph structure
# %%
try:
    display(Image(app.get_graph().draw_mermaid_png()))
except Exception as e:
    print(f"Could not render image: {e}")
    # Fallback: Print the raw mermaid text if PNG rendering fails
    print(app.get_graph().draw_mermaid())
# %%
