from pydantic import BaseModel

class Webhook(BaseModel):
    event_id: str
    email: str
    event: str
    timestamp: str