from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from conversation import ConversationChain
from token_fetch import fetch_access_token

app = FastAPI()

class InputData(BaseModel):
    email: str
    user_input: str

@app.post("/get_response/")
async def get_response(data: InputData):
    try:
        access_token = fetch_access_token(data.email)
        chatbot = ConversationChain(access_token)
        response = chatbot.run_chat(data.user_input)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
