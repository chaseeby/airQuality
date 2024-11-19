# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y gcc

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Update pip and install the dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Define the command to run the app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]