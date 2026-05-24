from pydantic import BaseModel
from typing import Literal


class FileLoaderResponse(BaseModel):
    text: str
    source: str
    type: Literal["pdf", "md"]
