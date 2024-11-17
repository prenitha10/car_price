import React, { useState } from "react";
import InputForm from "./InputForm";
import Results from "./Results";

const App = () => {
  const [result, setResult] = useState(null);

  const handlePrediction = async (data) => {
    const response = await fetch("https://car-price-piy5.onrender.com/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });
    const res = await response.json();
    setResult(res.predicted_price);
  };

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center">
      <h1 className="text-3xl font-bold mt-10">Car Price Predictor</h1>
      <InputForm onPredict={handlePrediction} />
      {result && <Results price={result} />}
    </div>
  );
};

export default App;
