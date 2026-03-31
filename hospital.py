from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector
from pymongo import MongoClient

app = FastAPI()

# ================= DB CONNECTION =================
def get_sql_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="yamini",
        database="hospital"
    )

def get_mongo_connection():
    client = MongoClient("mongodb://localhost:27017/")
    return client["hospital_db"]

# ================= REQUEST MODELS =================
class Patient(BaseModel):
    name: str
    age: int
    gender: str

class Doctor(BaseModel):
    name: str
    specialization: str

class Appointment(BaseModel):
    patient_id: int
    doctor_id: int
    date: str

class MedicalRecord(BaseModel):
    patient_id: int
    diagnosis: str
    medicine: str
    date: str

class Bill(BaseModel):
    patient_id: int
    amount: int

# ================= SERVICE =================
class HospitalService:

    def __init__(self):
        self.sql_conn = get_sql_connection()
        self.cursor = self.sql_conn.cursor(dictionary=True)
        self.mongo_db = get_mongo_connection()
        self.records = self.mongo_db["medical_records"]

service = HospitalService()

# ================= PATIENT =================
@app.post("/patients")
def add_patient(data: Patient):
    service.cursor.execute(
        "INSERT INTO patients(name, age, gender) VALUES(%s,%s,%s)",
        (data.name, data.age, data.gender)
    )
    service.sql_conn.commit()
    return {"message": "Patient added"}

@app.get("/patients")
def get_patients():
    service.cursor.execute("SELECT * FROM patients")
    return service.cursor.fetchall()

# ================= DOCTOR =================
@app.post("/doctors")
def add_doctor(data: Doctor):
    service.cursor.execute(
        "INSERT INTO doctors(name, specialization) VALUES(%s,%s)",
        (data.name, data.specialization)
    )
    service.sql_conn.commit()
    return {"message": "Doctor added"}

@app.get("/doctors")
def get_doctors():
    service.cursor.execute("SELECT * FROM doctors")
    return service.cursor.fetchall()

# ================= APPOINTMENT =================
@app.post("/appointments")
def book_appointment(data: Appointment):
    service.cursor.execute(
        "INSERT INTO appointments(patient_id, doctor_id, date) VALUES(%s,%s,%s)",
        (data.patient_id, data.doctor_id, data.date)
    )
    service.sql_conn.commit()
    return {"message": "Appointment booked"}

@app.get("/appointments")
def get_appointments():
    service.cursor.execute("SELECT * FROM appointments")
    return service.cursor.fetchall()

# ================= MEDICAL RECORD =================
@app.post("/medical-records")
def add_medical_record(data: MedicalRecord):
    visit = {
        "date": data.date,
        "diagnosis": data.diagnosis,
        "medicine": data.medicine
    }

    service.records.update_one(
        {"patient_id": data.patient_id},
        {"$push": {"history": visit}},
        upsert=True
    )

    return {"message": "Medical record added"}

@app.get("/medical-records/{patient_id}")
def view_history(patient_id: int):
    data = service.records.find_one({"patient_id": patient_id})

    if data:
        return data["history"]
    return {"message": "No history found"}

# ================= BILLING =================
@app.post("/billing")
def add_bill(data: Bill):
    service.cursor.execute(
        "INSERT INTO billing(patient_id, amount) VALUES(%s,%s)",
        (data.patient_id, data.amount)
    )
    service.sql_conn.commit()
    return {"message": "Bill added"}