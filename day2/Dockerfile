# Use a base image (e.g., Python)
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

ENV FLASK_APP=app1.py
ENV FLASK_RUN_HOST=0.0.0.0

# Copy the current directory into /app inside the container
COPY . /app

# Install the required packages from requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
# Run the application
CMD ["python", "app1.py"]
