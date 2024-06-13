# Use the official Python base image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Command to run the chatbot
CMD ["python", "chatbot.py"]

# Install NLTK data
RUN python -m nltk.downloader stopwords wordnet averaged_perceptron_tagger
