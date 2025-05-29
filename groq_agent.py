from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import END, START
from langgraph.graph.state import StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode

from langchain_core.tools import tool
from langchain_core.messages import BaseMessage
from langchain_groq import ChatGroq

import os
from dotenv import load_dotenv

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

class State(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

model = ChatGroq(temperature=0, model="Qwen-Qwq-32b")

def make_alternative_graph():
    @tool
    def add(a: float, b: float):
        """Adds two numbers."""
        return a + b

    tool_node = ToolNode([add])
    model_with_tools = model.bind_tools([add])

    def call_model(state):
        return {"messages": [model_with_tools.invoke(state["messages"])]}

    def should_continue(state: State):
        last_message = state["messages"][-1]
        if getattr(last_message, "tool_calls", None):
            return "tools"
        return END

    graph_workflow = StateGraph(State)
    graph_workflow.add_node("agent", call_model)
    graph_workflow.add_node("tools", tool_node)
    graph_workflow.add_edge("tools", "agent")
    graph_workflow.add_edge(START, "agent")
    graph_workflow.add_edge("tools", "agent")
    graph_workflow.add_conditional_edges("agent", should_continue)

    return graph_workflow.compile()

agent = make_alternative_graph()
