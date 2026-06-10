from langgraph.graph import StateGraph
from langgraph.graph import START, END

from state import ChatState
from langgraph.checkpoint.memory import InMemorySaver

memory = InMemorySaver()

from llm import llm
# node adding
def mentor(state: ChatState):

    response = llm.invoke(
        state["messages"]
    )

    return {
        "messages": [response]
    }
# graph construction
builder = StateGraph(ChatState)

builder.add_node("mentor", mentor)

builder.add_edge(START, "mentor")

builder.add_edge("mentor", END)

graph = builder.compile(checkpointer=memory)