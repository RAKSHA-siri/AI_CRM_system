tools = {
    "log_interaction": log_interaction,
    "edit_interaction": edit_interaction,
    "search_hcp": search_hcp,
    "generate_followup": generate_followup,
    "interaction_analysis": interaction_analysis
}


def tool_agent(state):

    message = state.get("message", "").lower()

    if "edit" in message or "change" in message:
        result = edit_interaction(
            hcp_name="Dr. John",
            sentiment="Negative"
        )

    elif "search" in message or "find" in message:
        result = search_hcp("Dr. Smith")

    elif "follow" in message:
        result = generate_followup(
            state.sentiment if hasattr(state, "sentiment") else "Positive",
            state.product if hasattr(state, "product") else "Product X"
        )

    elif "analyze" in message:
        result = interaction_analysis()

    else:
        result = log_interaction(
            "Dr. Smith",
            "Today",
            "Product X",
            "Positive",
            "Brochures",
            message
        )

    return {"response": result}


print("Tools connected to agent")