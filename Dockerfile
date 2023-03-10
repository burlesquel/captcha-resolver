FROM python:3.11.2

# Upgrade pip
RUN pip install --upgrade pip

# Set working directory
WORKDIR /

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application files
COPY . .

# Start the application
CMD ["uvicorn", "main:app", "--reload"]