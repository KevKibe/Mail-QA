from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from conversation import ConversationChain 
app = FastAPI()
chatbot = ConversationChain()  

class UserInput(BaseModel):
    prompt: str

@app.post("/chat")
async def chat_with_bot(user_input: UserInput):
    response = chatbot.run_chat(user_input.prompt)  
    return {"response": response}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
