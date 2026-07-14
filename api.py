from fastapi import FastAPI
from pydantic import BaseModel
app_api = FastAPI()
class ChatRequest(BaseModel):
    message: str


@app_api.post("/chat")
def chat(request: ChatRequest):

    response = tool_agent({
        "message": request.message
    })

    return {
        "response": response["response"],
        "form_data": {
            "hcp_name": state.hcp_name,
            "date": state.date,
            "product": state.product,
            "sentiment": state.sentiment,
            "materials_shared": state.materials_shared,
            "notes": state.notes
        }
    }


print("Chat API created successfully")