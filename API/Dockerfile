FROM python:3.11
# Set the working directory in the container
WORKDIR /API

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Start the application
CMD ["uvicorn", "api:app", "--host", "0.0.0.0"]
