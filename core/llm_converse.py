from config import GEMINIAPIKEY
from google import genai
from google.genai import types
from agent import sys_prompt

client = genai.Client(api_key=GEMINIAPIKEY)
model = "gemini-3-flash-preview"
config = types.GenerateContentConfig(
    system_instruction=sys_prompt.SYSTEM_PROMPT, response_mime_type="application/json"
)


def call_model(user_query: str) -> str:
    try:
        response = client.models.generate_content(
            model=model, contents=user_query, config=config
        )
        return response.text or ""
    except Exception as e:
        return f'{{"action": "answer", "data": "Model error: {str(e)}"}}'


def get_embeddings(text: str):
    # currently placeholder
    embeds = text
    return embeds
