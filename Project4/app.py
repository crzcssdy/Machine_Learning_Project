from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

# Load the trained model
model = joblib.load('obesity_classifier_model.pkl')

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    # Render an input form for the user
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract user input from form
        user_data = request.form

        # Parse numerical inputs
        age = float(user_data['Age'])
        height = float(user_data['Height'])  # in meters
        weight = float(user_data['Weight'])  # in kilograms

        # Calculate BMI
        bmi = weight / (height ** 2)

        # Parse categorical inputs (convert to expected format)
        features = {
            'Age': age,
            'Height': height,
            'Weight': weight,
            'BMI': bmi,
            'FCVC': float(user_data['FCVC']),
            'NCP': float(user_data['NCP']),
            'CH2O': float(user_data['CH2O']),
            'FAF': float(user_data['FAF']),
            'TUE': float(user_data['TUE']),
            'Gender_Male': 1 if user_data['Gender'] == 'Male' else 0,
            'family_history_with_overweight_yes': 1 if user_data['Family_History'] == 'Yes' else 0,
            'FAVC_yes': 1 if user_data['FAVC'] == 'Yes' else 0,
            'CAEC_Frequently': 1 if user_data['CAEC'] == 'Frequently' else 0,
            'CAEC_Sometimes': 1 if user_data['CAEC'] == 'Sometimes' else 0,
            'CAEC_no': 1 if user_data['CAEC'] == 'No' else 0,
            'SMOKE_yes': 1 if user_data['Smoke'] == 'Yes' else 0,
            'SCC_yes': 1 if user_data['SCC'] == 'Yes' else 0,
            'CALC_Frequently': 1 if user_data['CALC'] == 'Frequently' else 0,
            'CALC_Sometimes': 1 if user_data['CALC'] == 'Sometimes' else 0,
            'CALC_no': 1 if user_data['CALC'] == 'No' else 0,
            'MTRANS_Bike': 1 if user_data['MTRANS'] == 'Bike' else 0,
            'MTRANS_Motorbike': 1 if user_data['MTRANS'] == 'Motorbike' else 0,
            'MTRANS_Public_Transportation': 1 if user_data['MTRANS'] == 'Public_Transportation' else 0,
            'MTRANS_Walking': 1 if user_data['MTRANS'] == 'Walking' else 0,
        }

        # Create a DataFrame with the correct structure
        import pandas as pd
        input_data = pd.DataFrame([features])

        # Make prediction
        prediction = model.predict(input_data)[0]

        # Return BMI and prediction result
        return jsonify({
            'BMI': round(bmi, 2),
            'Obesity Class': prediction
        })

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
