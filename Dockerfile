# Use the official Python image as a base
FROM python:3.10-slim

# Set the working directory
WORKDIR /usr/src/app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set environment variables for Django
ENV PYTHONUNBUFFERED=1
ENV PORT=8000

# Collect static files for production (you may need to run this command in a Django management command)
RUN python manage.py collectstatic --noinput

# Expose the port that the app will run on
EXPOSE 8000

# Run the application with Gunicorn, pointing to your WSGI application
CMD ["gunicorn", "capstone.wsgi:application", "--bind", "0.0.0.0:8000"]
