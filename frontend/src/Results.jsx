import React from "react";

const Results = ({ price }) => {
  return (
    <div className="mt-4 bg-green-100 p-4 rounded">
      <h2 className="text-lg font-bold">Predicted Price: ${price}</h2>
    </div>
  );
};

export default Results;
