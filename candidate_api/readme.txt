# 🚀 Candidate Management API

A simple backend API built using **FastAPI** to manage candidates in a recruitment system.

---

## 🎯 Problem Statement

This project allows recruiters to:

* Add candidates
* View candidates
* Update candidate status

---

## 🛠️ Tech Stack

* **Python**
* **FastAPI**
* **SQLAlchemy**
* **SQLite**
* **Pydantic**

---

## ⚙️ Features

### 1️⃣ Create Candidate

* Endpoint: `POST /candidates`
* Validates:

  * Email format
  * Status must be one of:

    * `applied`
    * `interview`
    * `selected`
    * `rejected`

---

### 2️⃣ Get All Candidates

* Endpoint: `GET /candidates`
* Optional filter:

  * `?status=interview`

---

### 3️⃣ Update Candidate Status

* Endpoint: `PUT /candidates/{id}/status`

---

## 📁 Project Structure

```
candidate_api/
│── main.py
│── models.py
│── schemas.py
│── database.py
│── crud.py
│── requirements.txt
```

---

## 🧪 Setup Instructions

### 1. Clone the repository

```
git clone <your-repo-link>
cd candidate_api
```

---

### 2. Create virtual environment

```
python -m venv venv
```

---

### 3. Activate virtual environment

**Windows:**

```
venv\Scripts\activate
```

**Mac/Linux:**

```
source venv/bin/activate
```

---

### 4. Install dependencies

```
pip install -r requirements.txt
```

---

### 5. Run the server

```
uvicorn main:app --reload
```

---

## 🌐 API Testing

### Swagger UI (Interactive Docs)

```
http://127.0.0.1:8000/docs
```

### ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## 📌 Example Requests

### Create Candidate

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "skill": "Python",
  "status": "applied"
}
```

---

### Update Status

```json
{
  "status": "interview"
}
```

---

## 🧠 Design Decisions

* Used **FastAPI** for high performance and automatic API documentation
* Used **SQLAlchemy** for ORM-based database interaction
* Used **Pydantic** for request validation
* SQLite used for simplicity and quick setup

---

## 🚀 Future Improvements

* Add authentication (JWT)
* Add pagination
* Add search functionality
* Dockerize the application
* Add unit & integration tests

---

## 👨‍💻 Author

**Sachin Verma**

---

## ✅ Submission Note

This project was implemented as part of a backend assignment.
Focus was on clean structure, validation, and RESTful design.

---
