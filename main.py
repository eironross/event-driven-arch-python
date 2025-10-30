from fastapi import FastAPI
from event_bus import EventBus
from services.user_service import UserService
from services.email_service import EmailService
from services.analytics_service import AnalyticsService
from pydantic import BaseModel

app = FastAPI()
user_service = UserService()

EventBus.subscriber("UserCreated", EmailService())
EventBus.subscriber("UserCreated", AnalyticsService())


class User(BaseModel):
    username: str
    email: str

@app.get("/")
async def home():
    return {
        "message": "Hello, World!"
    }

@app.post("/created_account")
async def create(user: User):
    
    result = await user_service.create_user(username=user.username, email=user.email)
    return result

