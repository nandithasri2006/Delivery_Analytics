# Delivery Analytics API

## Problem Statement

Build a FastAPI application that tracks email delivery events using provider webhooks. Store delivery events in a SQLite database and expose an API to summarize delivery analytics.

---

## Objective

Measure notification effectiveness and diagnose delivery issues by tracking:

- Email Sent
- Delivered
- Opened
- Clicked
- Bounced

---

## Technologies Used

- Python 3.12
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn
- Pydantic

---

## Project Structure

```
delivery_analytics/
│── app.py
│── database.py
│── models.py
│── schemas.py
│── crud.py
│── requirements.txt
│── README.md
│── delivery.db
```

---

## Installation Guide

### Clone the repository

```bash
git clone https://github.com/yourusername/delivery-analytics.git
cd delivery-analytics
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Server

```bash
python -m uvicorn app:app --reload
```

---

## API Endpoints

### GET /

Returns welcome message.

---

### POST /webhook

Stores an email event.

Sample Request

```json
{
  "event_id": "1001",
  "email": "abc@gmail.com",
  "event": "delivered",
  "timestamp": "2026-06-26 10:00"
}
```

Sample Response

```json
{
  "message": "Webhook stored successfully"
}
```

---

### GET /analytics

Returns delivery analytics.

Sample Response

```json
{
  "email_sent": 1,
  "delivered": 1,
  "opened": 1,
  "clicked": 1,
  "bounced": 1,
  "total_events": 5
}
```

---

## Testing

1. Start the FastAPI server.

2. Open

```
http://127.0.0.1:8000/docs
```

3. Use POST `/webhook` to add events.

4. Call GET `/analytics`.

5. Verify the counts returned by the API.

---

## Features

- Receive webhook events
- Store events in SQLite
- Validate event types
- Prevent duplicate webhook events
- Analytics summary API
- Automatic Swagger documentation

---

## Edge Cases Handled

- Duplicate Event ID
- Invalid Event Type
- Missing Required Fields
- Empty Database
- Invalid JSON Request

---

## Sample Output

```json
{
  "email_sent": 200,
  "delivered": 195,
  "opened": 140,
  "clicked": 80,
  "bounced": 5
}
```

---

## Acceptance Criteria

✔ Receive webhook events successfully

✔ Store events in SQLite

✔ Return analytics summary

✔ Handle duplicate events

✔ Handle invalid event types

✔ Tested using Swagger/Postman

✔ Ready for GitHub submission

---

## Future Improvements

- Integrate SendGrid or AWS SES webhooks
- Add authentication
- Add date-wise analytics
- Dashboard using Streamlit or React
- Export analytics as CSV
