
import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [exercise, setExercise] = useState([]);
  const [feedback, setFeedback] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/daily?level=1')
      .then(res => setExercise(res.data));
  }, []);

  const handleSubmit = () => {
    axios.post('http://localhost:5000/check', { chords: exercise })
      .then(res => setFeedback(res.data.feedback));
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>Daily SATB Writing</h2>
      <div>{exercise.join(" - ")}</div>
      <button onClick={handleSubmit}>Check My Work</button>
      <div>
        <h3>Feedback:</h3>
        <ul>{feedback.map((f, i) => <li key={i}>{f}</li>)}</ul>
      </div>
    </div>
  );
}

export default App;
