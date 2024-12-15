FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Create directories for sample images and output
RUN mkdir -p /app/sample_images /app/output

# Set working directory
WORKDIR /app

# Expose port
EXPOSE 5001

# Run the application
CMD ["python", "app.py"]