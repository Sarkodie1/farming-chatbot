from fastapi import FastAPI

app = FastAPI(
    title="Farming Assistant Chatbot API",
    description="An API to assist farmers with farming insights.",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "Farming Assistant Chatbot API is running"}

# Add a health check endpoint that returns a 200 OK
@app.get("/health")
async def health_check():
    return {"status": "healthy"}
