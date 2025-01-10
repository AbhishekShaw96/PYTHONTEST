# Use the official Python image as the base
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose port 8000 for the Django development server
EXPOSE 8000

# Set the default command to run the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
