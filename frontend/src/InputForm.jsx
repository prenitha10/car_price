import React, { useState } from "react";

const InputForm = ({ onPredict }) => {
  const [formData, setFormData] = useState({
    Make: "",
    Model: "",
    Year: "",
    "Engine_Fuel_Type": "",
    "Transmission_Type": "",
    "Driven_Wheels": "",
    "Market_Category": "",
    "Vehicle_Size": "",
    "Vehicle_Style": "",
    "Engine_HP": "",
    "Engine_Cylinders": "",
    "Number_of_Doors": "",
    "highway_MPG": "",
    "city_mpg": "",
    Popularity: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onPredict(formData);
  };

  return (
    <form onSubmit={handleSubmit} className="bg-white p-6 rounded-lg shadow-md">
      <div className="grid grid-cols-2 gap-4">
        <input
          type="text"
          name="Make"
          placeholder="Make"
          onChange={handleChange}
          className="border p-2 rounded"
        />
        <input
          type="text"
          name="Model"
          placeholder="Model"
          onChange={handleChange}
          className="border p-2 rounded"
        />
        <input
          type="number"
          name="Year"
          placeholder="Year"
          onChange={handleChange}
          className="border p-2 rounded"
        />
        <input
          type="text"
          name="Engine Fuel Type"
          placeholder="Fuel Type"
          onChange={handleChange}
          className="border p-2 rounded"
        />
        <input
          type="text"
          name="Transmission Type"
          placeholder="Transmission"
          onChange={handleChange}
          className="border p-2 rounded"
        />
        <input
          type="text"
          name="Driven_Wheels"
          placeholder="Driven Wheels"
          onChange={handleChange}
          className="border p-2 rounded"
        />
        <input
          type="text"
          name="Market Category"
          placeholder="Market Category"
          onChange={handleChange}
          className="border p-2 rounded"
        />
        <input
          type="text"
          name="Vehicle Size"
          placeholder="Vehicle Size"
          onChange={handleChange}
          className="border p-2 rounded"
        />
        <input
          type="text"
          name="Vehicle Style"
          placeholder="Vehicle Style"
          onChange={handleChange}
          className="border p-2 rounded"
        />
        <input
          type="number"
          name="Engine HP"
          placeholder="Engine HP"
          onChange={handleChange}
          className="border p-2 rounded"
        />
        <input
          type="number"
          name="Engine Cylinders"
          placeholder="Engine Cylinders"
          onChange={handleChange}
          className="border p-2 rounded"
        />
        <input
          type="number"
          name="Number of Doors"
          placeholder="Number of Doors"
          onChange={handleChange}
          className="border p-2 rounded"
        />
        <input
          type="number"
          name="highway MPG"
          placeholder="Highway MPG"
          onChange={handleChange}
          className="border p-2 rounded"
        />
        <input
          type="number"
          name="city mpg"
          placeholder="City MPG"
          onChange={handleChange}
          className="border p-2 rounded"
        />
        <input
          type="number"
          name="Popularity"
          placeholder="Popularity"
          onChange={handleChange}
          className="border p-2 rounded"
        />
      </div>
      <button type="submit" className="mt-4 bg-blue-500 text-white px-4 py-2 rounded">
        Predict Price
      </button>
    </form>
  );
};

export default InputForm;
