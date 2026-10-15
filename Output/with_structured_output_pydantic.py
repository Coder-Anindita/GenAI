from pydantic import BaseModel,EmailStr
from typing import Optional
class Student(BaseModel):
    name: str="Anny"
    age: Optional[int]=None
    email:EmailStr

new_student = Student(age="34", email="abs@gmail.com")

print(new_student.name)