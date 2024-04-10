# Use python image as base
FROM python:3.9

# Copy requirement.txt to /app/requirements.txt
COPY requirements.txt /app/requirements.txt

# Set working directory to /app
WORKDIR /app

# Install python dependencies
RUN pip install -r requirements.txt

# Copy app.py to /app
COPY app.py /app

# Expose port 9090
EXPOSE 9090

# Specify maintainer
LABEL maintainer="Anna DIAW <annadiaw2000@gmail.com>"

# Specify version
LABEL version="1.0"

# Command to run the application
CMD ["python", "app.py"]