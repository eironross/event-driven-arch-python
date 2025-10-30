from event_bus import EventBus

# publisher
class UserService:
    async def create_user(self, username: str, email: str):
        
        print(f"Created a new user: {username}, w/ {email}")
        
        await EventBus.publish("UserCreated", {"username": username, "email": email})
        
        return {"message": f"User {username} created successfully!"}