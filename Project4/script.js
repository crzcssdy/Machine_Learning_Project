document.getElementById('predict-form').addEventListener('submit', async (e) => {
    e.preventDefault();
  
    // Collect form data
    const formData = new FormData(e.target);
    const data = {};
    formData.forEach((value, key) => {
      data[key] = value;
    });
  
    // Convert data to JSON
    const jsonData = {
      Age: Number(data.Age),
      Height: Number(data.Height),
      Weight: Number(data.Weight),
      BMI: Number(data.BMI),
      Gender_Male: Number(data.Gender_Male),
      family_history_with_overweight_yes: Number(data.family_history_with_overweight_yes),
      FAVC_yes: Number(data.FAVC_yes),
      // Add other fields here
    };
  
    console.log("Data being sent:", jsonData);
  
    // Send POST request to Flask API
    try {
      const response = await fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(jsonData),
      });
  
      if (!response.ok) {
        throw new Error("Error fetching prediction");
      }
  
      const result = await response.json();
      document.getElementById('result').innerText = `Predicted Obesity Class: ${result.Obesity_Class}`;
    } catch (error) {
      console.error(error);
      document.getElementById('result').innerText = 'An error occurred. Please try again.';
    }
  });
  