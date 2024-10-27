from pydantic import BaseModel

class ModelSurl(BaseModel):
    origin: str 
    surl: str