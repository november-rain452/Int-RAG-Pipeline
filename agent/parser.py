import json
from schema.agent_json import ResponseSchema


def parse_response(response: str):
    try:
        validated_data = ResponseSchema.model_validate_json(response)
        return validated_data.model_dump()

    except:
        return {"action": "answer", "data": "Parsing failed."}
