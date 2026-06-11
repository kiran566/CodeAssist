from langgraph.graph import StateGraph
from langgraph.graph import START, END
from langgraph.prebuilt import ToolNode
from langgraph.prebuilt import tools_condition

# importing the tools
from tools.complexity import analyze_complexity
from tools.debugger import debug_code
from tools.hints import give_hint
from tools.retrivertool import retrieve_context
from state import ChatState
from langgraph.checkpoint.memory import InMemorySaver

# tool list
tools = [analyze_complexity, debug_code, give_hint, retrieve_context]
memory = InMemorySaver()

from llm import llm
# bind llm with tools
llm_with_tools = llm.bind_tools(tools)
# context limit
def trim_messages(messages, max_last=4):
    return messages[-max_last:]

# node adding
def mentor(state: ChatState):

    response = llm_with_tools.invoke(trim_messages(state["messages"]))    

    return {
        "messages": [response]
    }
# tool node
tool_node = ToolNode(tools)
# graph construction
builder = StateGraph(ChatState)
builder.add_node("mentor", mentor)
builder.add_node(
    "tools",
    tool_node
)

builder.add_edge(START, "mentor")

builder.add_conditional_edges(
    "mentor",
    tools_condition
)
builder.add_edge("tools", "mentor")
builder.add_edge("tools", END)

graph = builder.compile(checkpointer=memory)