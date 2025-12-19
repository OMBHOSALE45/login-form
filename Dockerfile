FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install Flask
RUN pip install flask

# Expose Flask port
EXPOSE 5000

# Run Flask app
CMD ["python", "app.py"]
