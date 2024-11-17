from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np
model = joblib.load("car_price_model.h5")

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[" http://localhost:5173/"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CarFeatures(BaseModel):
    make: str
    model: str
    year: int
    fuel_type: str
    transmission: str
    driven_wheels: str
    engine_hp: float
    engine_cylinders: int
    highway_mpg: int
    city_mpg: int

@app.post("/predict")
async def predict_price(features: CarFeatures):
    input_data = np.array([[
        features.make, features.model, features.year, features.fuel_type,
        features.transmission, features.driven_wheels, features.engine_hp,
        features.engine_cylinders, features.highway_mpg, features.city_mpg
    ]])

    prediction = model.predict(input_data)[0]
    return {"predicted_price": round(prediction, 2)}
