# app.py
import json
import numpy as np
import os
import joblib
import pandas as pd
from flask import Flask, request, jsonify
import sys # Import sys for logging to stderr

app = Flask(__name__)

# Global variable for the model
model = None
model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model.pkl')

# Load the model when the app starts
try:
    model = joblib.load(model_path)
    print("Model loaded successfully.", file=sys.stderr) # Log to stderr for visibility in container logs
except FileNotFoundError:
    print(f"Error: Model file not found at {model_path}. Exiting.", file=sys.stderr)
    sys.exit(1) # Exit if model not found, Kubernetes will restart
except Exception as e:
    print(f"Error loading model: {e}. Exiting.", file=sys.stderr)
    sys.exit(1) # Exit for other loading errors

# Define the prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            raw_data = request.json['data']
            # Ensure the order and names of features match your training data
            feature_names = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude']
            df = pd.DataFrame(raw_data, columns=feature_names)

            predictions = model.predict(df).tolist()
            return jsonify({"predictions": predictions})
        except Exception as e:
            # Log the error for debugging
            print(f"Error during prediction: {e}", file=sys.stderr)
            return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
