from pydantic import BaseModel
from typing import Literal


class Document(BaseModel):
    text: str
    source: str
    filename: str
    type: Literal["pdf", "md"]
