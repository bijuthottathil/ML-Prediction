# Dockerfile
# Use a slim Python base image
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the trained model and the application code
COPY model.pkl .
COPY app.py .

# Expose the port the Flask app runs on
EXPOSE 5000

# Command to run the application using Gunicorn (a production-ready WSGI server)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]