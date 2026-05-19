from pydantic import BaseModel
from typing import Literal


class ResponseSchema(BaseModel):
    action: Literal["answer", "rag_tool"]
    data: str
