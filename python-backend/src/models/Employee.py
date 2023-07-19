from pydantic import BaseModel


class Employee(BaseModel):
    first_name:str
    last_name:str
    b_date:str
    gender:str
    dept_id:int