# Use the official Python image from the Docker Hub as a base
FROM python:3.9-slim as compiler

# Set the working directory in the container
WORKDIR /app

# Create a virtual environment and install necessary packages
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -Ur requirements.txt

# Use another stage to copy necessary files and setup environment
FROM python:3.9-slim as runner

# Set the working directory in the container
WORKDIR /app

# Copy the virtual environment from the previous stage
COPY --from=compiler /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy the application files
COPY . .

# Move the Scores.txt file to the root directory
RUN mv Scores.txt /Scores.txt

# Expose the necessary port
EXPOSE 8777

# Command to run on container startup
CMD ["flask", "run", "--host=0.0.0.0", "--port=8777"]
