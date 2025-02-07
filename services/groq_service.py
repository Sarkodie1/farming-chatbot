import logging
from groq import Groq
from config import GROQ_API_KEY, GROQ_MODEL
from utils.response_formatter import format_response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class GroqService:
    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)
        self.model = GROQ_MODEL
        # Enhanced system prompt with explicit formatting instructions
        self.system_prompt = (
            "You are an advanced chatbot assistant specialized in farming. "
            "Your role is to provide detailed, accurate, and practical advice on all aspects of farming, "
            "including crop management, weather forecasting, pest control, irrigation, sustainable practices, "
            "and market trends. Format your responses in clear markdown with the following structure:\n\n"
            "1. **Summary:** A brief overview.\n"
            "2. **Detailed Insights:** In-depth information and analysis.\n"
            "3. **Actionable Recommendations:** Bullet-pointed list of steps or advice.\n\n"
            "Ensure that your advice is accurate, easy to understand, and tailored to farmers."
        )

    def get_chat_completion(self, user_message: str) -> str:
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_message},
        ]
        try:
            logger.info("Sending request to Groq API with message: %s", user_message)
            chat_completion = self.client.chat.completions.create(
                messages=messages,
                model=self.model,
            )
            raw_reply = chat_completion.choices[0].message.content
            logger.info("Received raw response from Groq API.")
            # Optionally, format or validate the response
            formatted_reply = format_response(raw_reply)
            return formatted_reply
        except Exception as e:
            logger.error("Error communicating with Groq API: %s", e)
            raise Exception(f"Error communicating with Groq API: {e}")
