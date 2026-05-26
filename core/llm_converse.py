from core.config import GEMINIAPIKEY, EMBEDDINGKEY
from google import genai
from google.genai import types
from agent.sys_prompt import SYSTEM_PROMPT
from schema.agent_json import ResponseSchema

# Generative model
client = genai.Client(api_key=GEMINIAPIKEY)
model = "gemini-3-flash-preview"
config = types.GenerateContentConfig(
    system_instruction=SYSTEM_PROMPT,
    response_mime_type="application/json",
    response_schema=ResponseSchema,
)


def call_model(user_query: str) -> ResponseSchema:
    try:
        response = client.models.generate_content(
            model=model, contents=user_query, config=config
        )
        return ResponseSchema.model_validate_json(response.text)
    except Exception as e:
        return f'{{"action": "answer", "data": "Model error: {str(e)}"}}'


# embedding model
embed_client = genai.Client(api_key=EMBEDDINGKEY)
embedding_model = "gemini-embedding-2"


def get_embeddings(text: str):
    try:
        embeds = embed_client.models.embed_content(model=embedding_model, contents=text)
        return embeds.embeddings[0].values
    except Exception as e:
        raise RuntimeError(f"Embedding error: {e}")
