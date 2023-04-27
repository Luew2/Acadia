# Use the official Python 3.10 image as a base image
FROM python:3.10-slim

# Install system dependencies required by OpenCV
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt into the container
COPY requirements.txt /app/requirements.txt

# Set the working directory
WORKDIR /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Expose the port your app runs on
EXPOSE 8080

# Start your application
CMD ["gunicorn", "-b", ":8080", "api:app"]
