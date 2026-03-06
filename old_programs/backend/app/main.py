from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Схема для запроса
class UserRegister(BaseModel):
    email: str
    password: str

@app.post("/register")
def user_create(user: UserRegister):
    return {"status": "user created", "email": user.email}
