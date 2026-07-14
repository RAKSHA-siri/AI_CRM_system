def chat_with_ai(message):

    result = tool_agent({
        "message": message
    })

    return result["response"]


response = chat_with_ai(
    "Today I met Dr. Smith and discussed Product X efficiency. Sentiment was positive and I shared brochures."
)

print(response)

print("\nCurrent Form Data:")
print(state)