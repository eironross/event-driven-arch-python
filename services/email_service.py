class EmailService:
    async def handle_event(self, event_type, data):
        if event_type == "UserCreated":
            print(f"Sending notifcation to the user that the email was created: {data}")
            return 1
        print("Sending unsuccessfull creation of the account")