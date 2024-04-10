# Use a Python image as the base
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY app.py /app

# Declare the port the container should expose
EXPOSE 9090

# Command to run the application
CMD ["python", "app.py"]

# Specify the maintainer
MAINTAINER Dionisauce  

# Version of the Dockerfile
LABEL version="1.0"
