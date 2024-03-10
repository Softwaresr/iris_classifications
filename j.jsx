import React, { useState } from 'react';
import './styles.css'; // Import the CSS file

function IrisPrediction() {
  const [sepalLength, setSepalLength] = useState('');
  const [prediction, setPrediction] = useState('');

  const predictSpecies = () => {
    // Perform prediction (always setosa for demonstration)
    setPrediction('setosa');
  };

  return (
    <div className="container">
      <h2>Iris Species Prediction</h2>
      <div className="input-container">
        <label htmlFor="sepalLength">Sepal Length:</label>
        <div className="input-group">
          <input 
            type="number" 
            id="sepalLength" 
            value={sepalLength} 
            onChange={e => setSepalLength(e.target.value)} 
            step="0.1" 
          />
          <span className="unit">cm</span>
        </div>
      </div>
      <button onClick={predictSpecies}>Predict</button>
      {prediction && (
        <div className="result">
          <p>Prediction:</p>
          <p className="species">{prediction}</p>
        </div>
      )}
    </div>
  );
}

export default IrisPrediction;
