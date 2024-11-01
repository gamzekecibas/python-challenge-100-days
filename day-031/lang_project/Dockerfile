# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Install X11 utilities
RUN apt-get update && apt-get install -y \
    x11-apps

# Copy requirements.txt into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container at /app
COPY . /app/

# Allow X11 forwarding and set the display
ENV DISPLAY=host.docker.internal:0

# Run main.py of Chinese-English projectdocker build -t lang_project . when the container launches
CMD ["python", "main.py"]
