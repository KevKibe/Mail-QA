from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from conversation import ConversationChain

app = FastAPI()
chatbot = ConversationChain()

class UserInput(BaseModel):
    prompt: str

@app.post("/chat")
async def chat_with_bot(user_input: UserInput):
    try:
        response = chatbot.run_chat(user_input.prompt)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Chatbot error: {str(e)}")

if __name__ == "__main__":
    import uvicorn

    try:
        uvicorn.run(app, host="0.0.0.0", port=8000)
    except Exception as e:
        print(f"Uvicorn error: {str(e)}")
