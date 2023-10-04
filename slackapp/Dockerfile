FROM python:3.11
# Set the working directory in the container
WORKDIR /slackapp

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

EXPOSE 81

# Start the application
CMD ["python", "slack_app.py"]