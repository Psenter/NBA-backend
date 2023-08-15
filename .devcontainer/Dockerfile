# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set Python to run in unbuffered mode
ENV PYTHONUNBUFFERED 1

# Install any needed packages specified in requirements.txt
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir psycopg2-binary




