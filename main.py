from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Farming Assistant Chatbot API",
    description="An API to assist farmers with farming insights.",
    version="1.0.0"
)

# Root endpoint for basic info
@app.get("/")
async def root():
    return {"message": "Farming Assistant Chatbot API is running"}

# Health check endpoint (used by Render)
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Define the data model for chat requests
class ChatRequest(BaseModel):
    message: str

# Chat endpoint: process user queries
@app.post("/chat")
async def chat_interaction(request: ChatRequest):
    user_message = request.message
    # For demonstration, we check a sample query.
    # In a real app, you could call your Groq service here.
    if user_message.lower() == "how do i improve soil fertility?":
        return {"response": "To improve soil fertility, add compost and rotate your crops."}
    else:
        return {"response": "I'm here to help with your farming questions."}
