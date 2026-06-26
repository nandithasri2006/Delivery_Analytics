from sqlalchemy.orm import Session
from models import EmailEvent

VALID_EVENTS = [
    "sent",
    "delivered",
    "opened",
    "clicked",
    "bounced"
]


def event_exists(db: Session, event_id: str):
    return db.query(EmailEvent).filter(
        EmailEvent.event_id == event_id
    ).first()


def create_event(db: Session, data):

    event = EmailEvent(
        event_id=data.event_id,
        email=data.email,
        event=data.event,
        timestamp=data.timestamp
    )

    db.add(event)
    db.commit()
    db.refresh(event)

    return event


def count_events(db: Session, event_name: str):

    return db.query(EmailEvent).filter(
        EmailEvent.event == event_name
    ).count()


def total_events(db: Session):

    return db.query(EmailEvent).count()