from pydantic import BaseModel


class Department(BaseModel):
    name:str
    manager_id:int
