from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd

# Load the trained model
model = joblib.load("car_price_model.pkl")

app = FastAPI()

# Add CORS middleware for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update to specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the input schema
class CarFeatures(BaseModel):
    Make: str
    Model: str
    Engine_Fuel_Type: str
    Transmission_Type: str
    Driven_Wheels: str
    Market_Category: str
    Vehicle_Size: str
    Vehicle_Style: str
    Year: str  # Assuming input as string
    Engine_HP: str  # Assuming input as string
    Engine_Cylinders: str  # Assuming input as string
    Number_of_Doors: str  # Assuming input as string
    highway_MPG: str  # Assuming input as string
    city_mpg: str  # Assuming input as string
    Popularity: str  # Assuming input as string

# Define the prediction endpoint
@app.post("/predict")
async def predict_price(features: CarFeatures):
    try:
        # Convert string inputs to appropriate types
        input_data = pd.DataFrame([{
            "Make": features.Make,
            "Model": features.Model,
            "Engine Fuel Type": features.Engine_Fuel_Type,
            "Transmission Type": features.Transmission_Type,
            "Driven_Wheels": features.Driven_Wheels,
            "Market Category": features.Market_Category,
            "Vehicle Size": features.Vehicle_Size,
            "Vehicle Style": features.Vehicle_Style,
            "Year": int(features.Year),
            "Engine HP": float(features.Engine_HP),
            "Engine Cylinders": float(features.Engine_Cylinders),
            "Number of Doors": float(features.Number_of_Doors),
            "highway MPG": int(features.highway_MPG),
            "city mpg": int(features.city_mpg),
            "Popularity": int(features.Popularity)
        }])

        # Predict using the loaded model
        prediction = model.predict(input_data)[0]

        # Return the prediction
        return {"predicted_price": round(prediction, 2)}
    except ValueError as e:
        return {"error": f"Value conversion error: {str(e)}"}
    except Exception as e:
        return {"error": str(e)}
