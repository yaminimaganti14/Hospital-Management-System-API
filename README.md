# 🏥 Hospital Management System (FastAPI + MySQL + MongoDB)

## 📌 Overview

This project is a backend-based **Hospital Management System** built using FastAPI. It manages core hospital operations such as patients, doctors, appointments, medical records, and billing.

The system demonstrates a **hybrid database architecture**:

* **MySQL** → structured data (patients, doctors, appointments, billing)
* **MongoDB** → unstructured data (medical history)

---

## 🚀 Features

* 👨‍⚕️ Patient Management (Add & View)
* 🩺 Doctor Management
* 📅 Appointment Booking System
* 📂 Medical Records (stored in MongoDB)
* 💰 Billing System
* ⚡ Fast REST APIs with FastAPI
* 🔄 Hybrid Database Integration (SQL + NoSQL)

---

## 🛠️ Tech Stack

* **Backend Framework:** FastAPI
* **Language:** Python
* **Database 1:** MySQL
* **Database 2:** MongoDB
* **Server:** Uvicorn

---

## 📂 Project Structure

```
hospital-management-system/
│
├── main.py              # Complete application (API + DB + Models)
├── requirements.txt     # Dependencies
├── README.md            # Documentation
└── .gitignore           # Ignored files
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```
git clone https://github.com/your-username/hospital-management-system.git
cd hospital-management-system
```

---

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Setup Databases

#### MySQL

Create database:

```
CREATE DATABASE hospital;
```

Create tables:

```
CREATE TABLE patients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10)
);

CREATE TABLE doctors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    specialization VARCHAR(100)
);

CREATE TABLE appointments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    doctor_id INT,
    date VARCHAR(20)
);

CREATE TABLE billing (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    amount INT
);
```

---

#### MongoDB

* Install MongoDB
* Database used: `hospital_db`
* Collection: `medical_records`

---

### 4️⃣ Run the Application

```
uvicorn main:app --reload
```

---

### 5️⃣ Access API Docs

```
http://127.0.0.1:8000/docs
```

---

## 📡 API Endpoints

### 👨‍⚕️ Patients

* `POST /patients` → Add patient
* `GET /patients` → Get all patients

### 🩺 Doctors

* `POST /doctors` → Add doctor
* `GET /doctors` → Get doctors

### 📅 Appointments

* `POST /appointments` → Book appointment
* `GET /appointments` → View appointments

### 📂 Medical Records (MongoDB)

* `POST /medical-records` → Add medical history
* `GET /medical-records/{patient_id}` → View history

### 💰 Billing

* `POST /billing` → Add bill

---

## 🔄 System Workflow

1. Client sends request (Postman / Browser)
2. FastAPI handles request
3. Data validated using Pydantic models
4. Data stored in:

   * MySQL → structured entities
   * MongoDB → medical history
5. JSON response returned

---

## 📷 Screenshots

👉 Add Swagger UI screenshots here (`/docs` page)

---

## 🔐 Future Enhancements

* JWT Authentication & Authorization
* Role-based access (Admin, Doctor, Patient)
* Frontend using React
* Docker deployment
* Cloud hosting (AWS / Render)

---

## ⚠️ Limitations

* Single-file structure (not scalable for large applications)
* No authentication/security layer
* Basic error handling

---

## 🌟 Learning Outcomes

* Built REST APIs using FastAPI
* Integrated MySQL and MongoDB
* Designed hybrid database architecture
* Practiced backend development best practices

---

## 👩‍💻 Author

**Yamini Maganti**
📧 [magantiyamini832yam@gmail.com](mailto:magantiyamini832yam@gmail.com)
🔗 LinkedIn: https://www.linkedin.com/

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

---
