FROM python:3.11-slim

WORKDIR /app

# Install system dependencies if any
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Ensure start script is executable
RUN chmod +x start.sh

# Expose ports for both backend and frontend
EXPOSE 8000
EXPOSE 8501

# Run the unified start script
CMD ["./start.sh"]
