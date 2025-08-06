# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port Flask runs on
EXPOSE 5050

# Run the app
CMD ["python", "app.py"]
