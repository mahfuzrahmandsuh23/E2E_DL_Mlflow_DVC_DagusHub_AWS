# Use updated base image
FROM python:3.10-slim

# Install required tools (e.g. awscli)
RUN apt update -y && apt install -y awscli

# Set working directory inside the container
WORKDIR /app

# Copy project files into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run your application
CMD ["python3", "app.py"]
