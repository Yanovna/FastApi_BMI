from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class PatientData(BaseModel):
    weight: float  # кг
    height: float  # см


@app.get("/")
async def welcome():
    return {"message": "Медицинский API для расчета ИМТ"}


@app.post("/calculate/bmi")
async def calculate_bmi(patient: PatientData):
    bmi = patient.weight / ((patient.height / 100) ** 2)

    interpretation = (
        "Недостаточный вес" if bmi < 18.5 else
        "Норма" if 18.5 <= bmi < 25 else
        "Избыточный вес" if 25 <= bmi < 30 else
        "Ожирение"
    )

    return {
        "bmi": round(bmi, 2),
        "interpretation": interpretation
    }