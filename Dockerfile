FROM python:3.13.0a3

# Maintainer info
LABEL maintainer="batumanav@gmail.com"

# Make working directories
RUN  mkdir -p  /captcha-recognition-api
WORKDIR  /captcha-recognition-api

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

# Upgrade pip with no cache
RUN pip install --no-cache-dir -U pip

# Copy application requirements file to the created working directory
COPY requirements.txt .

# Install application dependencies from the requirements file
RUN pip install -r requirements.txt

# Copy the rest of the application files
COPY . .

# Start the application
CMD ["python", "server.py"]