from flask import Flask, request, render_template, jsonify
import pickle
import pandas as pd
import json

app = Flask(__name__)

# Load the pre-trained model
with open('HousingPrice_Prediction.pkl', 'rb') as file:
    pipe = pickle.load(file)

# Load the locations from JSON file
with open('static/locations.json', 'r') as f:
    locations = json.load(f)['locations']

@app.route('/')
def home():
    return render_template('form.html', locations=locations, prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    # Get the features from the HTML form
    input_data = {
        'location': request.form['location'],
        'total_sqft': float(request.form['total_sqft']),
        'bath': float(request.form['bath']),
        'bhk': float(request.form['bhk'])
    }

    # Convert to DataFrame
    df = pd.DataFrame([input_data])

    # Preprocess the data (scaling and one-hot encoding)
    X = pipe['preprocessor'].transform(df)

    # Make prediction
    prediction = pipe['Estimator'].predict(X)

    # Return the prediction result on the same page
    return jsonify({'prediction': prediction[0]})

if __name__ == "__main__":
    print("Starting Flask Server For House Price Prediction")
    app.run(debug=True)
