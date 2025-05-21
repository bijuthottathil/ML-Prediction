![image](https://github.com/user-attachments/assets/fd64560a-dc3d-4162-90a7-fbde778b4c0d)


# Here’s a complete Python ML example that predicts housing price based on:
	•	'Rooms'
	•	'Bathroom'
	•	'Landsize'
	•	'Lattitude'
	•	'Longtitude'
Using scikit-learn to train a regression model and make predictions. 

1. Data ![image](https://github.com/user-attachments/assets/a2b3453a-53de-4b55-9885-6f48f492fbe7)
2. Created pickle file successfully ![image](https://github.com/user-attachments/assets/d8e38548-2294-44e9-a1fa-5c89b7a902b1)
3. Consuming the model in a Flask API ![image](https://github.com/user-attachments/assets/a2f0dbb9-1a09-4cd2-a3b7-2d7c1c1d1f18)
4. Run API ![image](https://github.com/user-attachments/assets/eeaa79d3-36c9-45f2-a445-167f86335ca8)
5. I am using postman to access this service and submit data to get prediciton ![image](https://github.com/user-attachments/assets/00075628-58b6-4f1d-bde9-f88905ab7cdc)
6. You can see prediction is generated here

   In this example , I provide data for 2 houses like below

   {"data":[[2, 1, 156, 100, 1990, -37.8079, 144.9934], [3, 2, 200, 120, 2000, -37.9, 145.0]]}

      Rooms  Bathroom  Landsize  Lattitude  Longtitude
1      2       1.0     156.0   -37.8079    144.9934
2      3       2.0     134.0   -37.8093    144.9944


Response recieved  

  # Cost for 1st house- 910000.0
  # Cost for 2nd house - 1177000.0




