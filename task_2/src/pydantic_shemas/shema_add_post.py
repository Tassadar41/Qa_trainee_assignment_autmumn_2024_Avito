from pydantic import BaseModel

class AddPost(BaseModel):
    status: str
