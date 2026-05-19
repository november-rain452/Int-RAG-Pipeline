import json


def parse_response(response: str):
    try:
        return json.loads(response)

    except:
        return {"action": "answer", "data": "Parsing failed."}
