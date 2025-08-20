# Use the official Python image as a base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the working directory
COPY requirements.txt .

# Install the necessary dependencies
# The --no-cache-dir flag is used to prevent pip from caching packages, which reduces the image size.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Django project into the container
# This copies everything from the current directory on your machine to the /app directory in the container
COPY . .

# Expose the port that the Django app will run on
# This lets Docker know that the container will listen on this port at runtime
EXPOSE 8000

# Run the Django server
# The 0.0.0.0 address is used to make the server accessible from outside the container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
