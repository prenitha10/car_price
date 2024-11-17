import React, { useState } from "react";

const InputForm = ({ onPredict }) => {
  const [formData, setFormData] = useState({
    make: "",
    model: "",
    year: "",
    fuel_type: "",
    transmission: "",
    driven_wheels: "",
    engine_hp: "",
    engine_cylinders: "",
    highway_mpg: "",
    city_mpg: "",
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
          name="make"
          placeholder="Make"
          onChange={handleChange}
          className="border p-2 rounded"
        />
        <input
          type="text"
          name="model"
          placeholder="Model"
          onChange={handleChange}
          className="border p-2 rounded"
        />
        <input
          type="number"
          name="year"
          placeholder="Year"
          onChange={handleChange}
          className="border p-2 rounded"
        />
        <input
          type="text"
          name="fuel_type"
          placeholder="Fuel Type"
          onChange={handleChange}
          className="border p-2 rounded"
        />
        <input
          type="text"
          name="transmission"
          placeholder="Transmission"
          onChange={handleChange}
          className="border p-2 rounded"
        />
        <input
          type="text"
          name="driven_wheels"
          placeholder="Driven Wheels"
          onChange={handleChange}
          className="border p-2 rounded"
        />
        <input
          type="number"
          name="engine_hp"
          placeholder="Engine HP"
          onChange={handleChange}
          className="border p-2 rounded"
        />
        <input
          type="number"
          name="engine_cylinders"
          placeholder="Engine Cylinders"
          onChange={handleChange}
          className="border p-2 rounded"
        />
        <input
          type="number"
          name="highway_mpg"
          placeholder="Highway MPG"
          onChange={handleChange}
          className="border p-2 rounded"
        />
        <input
          type="number"
          name="city_mpg"
          placeholder="City MPG"
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
