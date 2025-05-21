# train_model.py
import pandas as pd
import joblib
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# --- Data Loading and Preprocessing ---
# Assuming melb_data.csv is in the same directory as this script
melbourne_file_path = 'house_data.csv'
try:
    melbourne_data = pd.read_csv(melbourne_file_path)
except FileNotFoundError:
    print(f"Error: '{melbourne_file_path}' not found. Please ensure the data file is in the same directory.")
    # Create a dummy dataframe for demonstration if file not found
    data = {
        'Rooms': [2, 3, 4, 2, 3],
        'Bathroom': [1, 2, 2, 1, 1],
        'Landsize': [150, 200, 300, 180, 220],
        'BuildingArea': [100, 120, 150, 110, 130],
        'YearBuilt': [1990, 2000, 1985, 2010, 1995],
        'Lattitude': [-37.8, -37.9, -37.7, -37.8, -37.9],
        'Longtitude': [144.9, 145.0, 144.8, 144.9, 145.0],
        'Price': [300000, 450000, 600000, 350000, 480000]
    }
    melbourne_data = pd.DataFrame(data)
    print("Using dummy data for demonstration.")


# Drop rows with missing values for simplicity in this example
melbourne_data = melbourne_data.dropna(axis=0)

# Select target and features
y = melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]

# --- Model Training ---
# Split data into training and validation sets
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)

# Define and train a Decision Tree Regressor model
model = DecisionTreeRegressor(random_state=1)
model.fit(train_X, train_y)

# Make predictions on validation data
val_predictions = model.predict(val_X)
print(f"Mean Absolute Error: {mean_absolute_error(val_y, val_predictions)}")

# Save the trained model
joblib.dump(model, 'model.pkl')
print("Model 'model.pkl' created successfully.")
