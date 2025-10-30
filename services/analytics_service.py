class AnalyticsService:
    async def handle_event(self, event_type, data):
        if event_type == "UserCreated":
            print (f"Created an analysis to the user that was created: {data}")
            return 1 
        print("Sending unsuccessful creation of the account")