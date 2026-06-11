# using TyoedDict  defining the state of the chat,
# where this  sharedmemory having elemts used and updated by various nodes  in the workflow
from typing import Annotated
from typing_extensions import TypedDict
# reducer
from langgraph.graph.message import add_messages

class ChatState(TypedDict):
    messages: Annotated[list, add_messages]
