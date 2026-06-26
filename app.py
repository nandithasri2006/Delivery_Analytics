from fastapi import FastAPI, HTTPException
from database import engine, SessionLocal
from models import Base
from schemas import Webhook
from crud import (
    create_event,
    event_exists,
    count_events,
    VALID_EVENTS,
)

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Delivery Analytics API")


@app.get("/")
def home():
    return {"message": "Welcome to Delivery Analytics API"}


@app.post("/webhook")
def receive_webhook(data: Webhook):

    if data.event.lower() not in VALID_EVENTS:
        raise HTTPException(status_code=400, detail="Invalid event type")

    db = SessionLocal()

    if event_exists(db, data.event_id):
        db.close()
        raise HTTPException(status_code=400, detail="Duplicate Event")

    create_event(db, data)

    db.close()

    return {"message": "Webhook stored successfully"}


@app.get("/analytics")
def analytics():

    db = SessionLocal()

    email_sent = count_events(db, "sent")
    delivered = count_events(db, "delivered")
    opened = count_events(db, "opened")
    clicked = count_events(db, "clicked")
    bounced = count_events(db, "bounced")

    # Avoid division by zero
    if email_sent == 0:
        delivery_rate = 0
        open_rate = 0
        click_rate = 0
        bounce_rate = 0
    else:
        delivery_rate = round((delivered / email_sent) * 100, 2)
        open_rate = round((opened / delivered) * 100, 2) if delivered else 0
        click_rate = round((clicked / opened) * 100, 2) if opened else 0
        bounce_rate = round((bounced / email_sent) * 100, 2)

    db.close()

    return {
        "email_sent": email_sent,
        "delivered": delivered,
        "delivery_rate": f"{delivery_rate}%",
        "opened": opened,
        "open_rate": f"{open_rate}%",
        "clicked": clicked,
        "click_rate": f"{click_rate}%",
        "bounced": bounced,
        "bounce_rate": f"{bounce_rate}%"
    }