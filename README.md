# Delivery Analytics API

## Problem Statement

Develop a RESTful API that receives email delivery webhook events from an email service provider, stores them in a SQLite database, prevents duplicate events, validates incoming requests, and provides analytics to measure notification effectiveness.

The API tracks the following email lifecycle events:

* Sent
* Delivered
* Opened
* Clicked
* Bounced

It also calculates delivery performance metrics such as delivery rate, open rate, click rate, and bounce rate.

---

# Features

* FastAPI-based REST API
* Receive email webhook events
* Store events in SQLite database
* SQLAlchemy ORM integration
* Pydantic request validation
* Duplicate event detection using `event_id`
* Analytics generation
* Delivery/Open/Click/Bounce rate calculation
* Proper HTTP status code handling
* Interactive Swagger documentation

---

# Technologies Used

| Technology   | Purpose                      |
| ------------ | ---------------------------- |
| Python 3.12  | Backend programming language |
| FastAPI      | REST API development         |
| SQLite       | Database                     |
| SQLAlchemy   | ORM                          |
| Pydantic     | Request validation           |
| Uvicorn      | ASGI server                  |
| Git & GitHub | Version control              |
| Swagger UI   | API testing                  |

---

# Project Structure

```text
Delivery_Analytics/
│
├── app.py
├── crud.py
├── database.py
├── models.py
├── schemas.py
├── generate_data.py
├── requirements.txt
├── README.md
└── delivery.db
```

---

# Installation

## 1. Clone the repository

```bash
git clone https://github.com/nandithasri2006/Delivery_Analytics.git
```

## 2. Move into the project

```bash
cd Delivery_Analytics
```

## 3. Create a virtual environment

```bash
python -m venv venv
```

## 4. Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## 5. Install dependencies

```bash
pip install -r requirements.txt
```

## 6. Run the application

```bash
python -m uvicorn app:app --reload
```

---

# API Endpoints

## GET /

Returns a welcome message.

### Response

```json
{
  "message": "Welcome to Delivery Analytics API"
}
```

---

## POST /webhook

Stores an email webhook event.

### Sample Request

```json
{
  "event_id": "1001",
  "email": "abc@gmail.com",
  "event": "delivered",
  "timestamp": "2026-06-26 10:00:00"
}
```

### Success Response

```json
{
  "message": "Webhook stored successfully"
}
```

---

## GET /analytics

Returns email delivery analytics.

### Sample Response

```json
{
  "email_sent": 200,
  "delivered": 195,
  "delivery_rate": "97.5%",
  "opened": 140,
  "open_rate": "71.79%",
  "clicked": 80,
  "click_rate": "57.14%",
  "bounced": 5,
  "bounce_rate": "2.5%"
}
```

> **Note:** The above response was generated after inserting a sample dataset using `generate_data.py`, containing:
>
> * 200 Sent events
> * 195 Delivered events
> * 140 Opened events
> * 80 Clicked events
> * 5 Bounced events

---

# Architecture Workflow

```text
Email Provider
      │
      ▼
POST /webhook
      │
      ▼
Validate Request
      │
      ▼
Duplicate Check
      │
      ▼
Store in SQLite
      │
      ▼
GET /analytics
      │
      ▼
Calculate Counts & Rates
      │
      ▼
JSON Response
```

---

# Edge Cases Handled

| Scenario                | HTTP Status              |
| ----------------------- | ------------------------ |
| Valid webhook event     | 200 OK                   |
| Duplicate event         | 400 Bad Request          |
| Invalid event type      | 400 Bad Request          |
| Missing required fields | 422 Unprocessable Entity |

---

# Testing

The application was tested using:

* Swagger UI
* FastAPI Interactive Documentation
* Manual API Testing

Verified scenarios include:

* Successful webhook insertion
* Duplicate event detection
* Invalid event type handling
* Missing required field validation
* Analytics generation

---

# Challenges Addressed

* Duplicate webhook event prevention
* Invalid event validation
* Division-by-zero handling
* Virtual environment package configuration

---

# Future Enhancements

* Campaign-wise analytics
* Recipient-level tracking
* Time-based analytics
* Email format validation
* Automated testing using `pytest`
* Docker deployment
* PostgreSQL support

---

# GitHub Repository

https://github.com/nandithasri2006/Delivery_Analytics

---

# Author

**Nandhitha Maraka**

Internship Project – Delivery Analytics API
