# Dockerfile
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install pip dependencies (PyYAML required by the project)
RUN pip install --no-cache-dir pyyaml

# Copy project files into the image
COPY . /app

# Default command to run the main script
CMD ["python", "main.py"]
