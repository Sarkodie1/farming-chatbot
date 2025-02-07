import logging
from fastapi import FastAPI
from routers import chat

# Configure basic logging
logging.basicConfig(level=logging.INFO)

app = FastAPI(
    title="Farming Assistant Chatbot",
    description="An advanced chatbot designed to assist farmers with all aspects of farming.",
    version="1.0.0",
)

# Include the chat router under the /api prefix.
app.include_router(chat.router, prefix="/api")

# Root endpoint for health check
@app.get("/")
async def root():
    return {"message": "Farming Assistant Chatbot API is running!"}
