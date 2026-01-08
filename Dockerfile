# Use Python 3.9 slim image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY scripts/ ./scripts/
COPY data/ ./data/
COPY outputs/ ./outputs/

# Create outputs directory if not exists
RUN mkdir -p outputs/csv outputs/parquet

# Copy run script
COPY run.sh .
RUN chmod +x run.sh

# Run the scripts
CMD ["./run.sh"]