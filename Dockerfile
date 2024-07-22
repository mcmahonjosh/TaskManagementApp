# Use the Python 3.10 slim image as the base
FROM python:3.10-slim

# Set working directory
WORKDIR /app


# Install system dependencies
RUN apt-get update && \
    apt-get install -y \
    pkg-config \
    libcairo2-dev \
    gcc \
    g++ \
    make \
    build-essential \
    python3-dev \
    libffi-dev \
    libssl-dev \
    libsystemd-dev \
    libgirepository1.0-dev \
    libdbus-1-dev \
    libcairo2-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt .

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the application port
EXPOSE 8000

# Define the command to run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--timeout", "120", "config.wsgi:application"]

