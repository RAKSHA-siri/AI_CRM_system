from langgraph.graph import StateGraph, END


# Create agent graph
workflow = StateGraph(dict)


# Agent node
def ai_agent(state):

    user_message = state.get("message", "")

    return {
        "response": f"AI received: {user_message}"
    }


# Add node
workflow.add_node("agent", ai_agent)


# Set starting point
workflow.set_entry_point("agent")


# End point
workflow.add_edge("agent", END)


# Compile agent
app = workflow.compile()

print("LangGraph Agent created successfully")