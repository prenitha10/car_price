from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd

model = joblib.load("car_price_model.pkl")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CarFeatures(BaseModel):
    Make: str
    Model: str
    Engine_Fuel_Type: str
    Transmission_Type: str
    Driven_Wheels: str
    Market_Category: str
    Vehicle_Size: str
    Vehicle_Style: str
    Year: int
    Engine_HP: float
    Engine_Cylinders: float
    Number_of_Doors: float
    highway_MPG: int
    city_mpg: int
    Popularity: int

@app.post("/predict")
async def predict_price(features: CarFeatures):
    try:
        input_data = pd.DataFrame([{
            "Make": features.Make,
            "Model": features.Model,
            "Engine Fuel Type": features.Engine_Fuel_Type,
            "Transmission Type": features.Transmission_Type,
            "Driven_Wheels": features.Driven_Wheels,
            "Market Category": features.Market_Category,
            "Vehicle Size": features.Vehicle_Size,
            "Vehicle Style": features.Vehicle_Style,
            "Year": features.Year,
            "Engine HP": features.Engine_HP,
            "Engine Cylinders": features.Engine_Cylinders,
            "Number of Doors": features.Number_of_Doors,
            "highway MPG": features.highway_MPG,
            "city mpg": features.city_mpg,
            "Popularity": features.Popularity
        }])

        prediction = model.predict(input_data)[0]

        return {"predicted_price": round(prediction, 2)}
    except Exception as e:
        return {"error": str(e)}
