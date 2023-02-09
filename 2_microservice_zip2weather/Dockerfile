# Use an official Python runtime as the base image
FROM python:3.9-slim-buster

# Set the working directory
WORKDIR /app

# Copy the app code to the working directory
COPY app.py .

# Install Flask
RUN pip install Flask

# Expose port 8000 for the microservice
EXPOSE 5000

# Set the command to run when the container starts
CMD ["python", "app.py"]
