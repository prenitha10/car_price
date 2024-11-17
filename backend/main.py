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
        # Ensure all inputs are non-empty and handle missing values
        input_data = pd.DataFrame([{
            "Make": features.Make or "Unknown",
            "Model": features.Model or "Unknown",
            "Engine Fuel Type": features.Engine_Fuel_Type or "Unknown",
            "Transmission Type": features.Transmission_Type or "Unknown",
            "Driven_Wheels": features.Driven_Wheels or "Unknown",
            "Market Category": features.Market_Category or "Unknown",
            "Vehicle Size": features.Vehicle_Size or "Unknown",
            "Vehicle Style": features.Vehicle_Style or "Unknown",
            "Year": int(features.Year) if features.Year else 2000,  # Default to 2000 if empty
            "Engine HP": float(features.Engine_HP) if features.Engine_HP else 100.0,  # Default to 100.0
            "Engine Cylinders": float(features.Engine_Cylinders) if features.Engine_Cylinders else 4.0,  # Default to 4.0
            "Number of Doors": float(features.Number_of_Doors) if features.Number_of_Doors else 4.0,  # Default to 4.0
            "highway MPG": int(features.highway_MPG) if features.highway_MPG else 25,  # Default to 25
            "city mpg": int(features.city_mpg) if features.city_mpg else 20,  # Default to 20
            "Popularity": int(features.Popularity) if features.Popularity else 1000  # Default to 1000
        }])

        # Predict using the loaded model
        prediction = model.predict(input_data)[0]

        # Return the prediction
        return {"predicted_price": round(prediction, 2)}
    except ValueError as e:
        return {"error": f"Value conversion error: {str(e)}"}
    except Exception as e:
        return {"error": str(e)}
