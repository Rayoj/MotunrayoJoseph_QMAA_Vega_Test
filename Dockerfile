# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Install required dependencies
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    gnupg \
    lsb-release \
    ca-certificates \
    fonts-liberation \
    libappindicator3-1 \
    libgdk-pixbuf2.0-0 \
    libnspr4 \
    libnss3 \
    libxss1 \
    xdg-utils \
    && rm -rf /var/lib/apt/lists/*

# Add the Google Chrome repository
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN DISTRO=$(lsb_release -c | awk '{print $2}') && \
    echo "deb [signed-by=/etc/apt/trusted.gpg] http://dl.google.com/linux/chrome/deb/ $DISTRO main" | tee -a /etc/apt/sources.list.d/google-chrome.list

# Install Google Chrome
RUN apt-get update && apt-get install -y google-chrome-stable

# Install ChromeDriver
RUN CHROME_VERSION=$(google-chrome --version | cut -d ' ' -f 3 | cut -d '.' -f 1) && \
    wget https://chromedriver.storage.googleapis.com/$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE_${CHROME_VERSION})/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    mv chromedriver /usr/local/bin/ && \
    chmod +x /usr/local/bin/chromedriver

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install selenium pytest

# Set working directory for the tests
WORKDIR /app

# Copy the test scripts to the container
COPY . /app

# Command to run the tests
CMD ["pytest", "test_obj1_scenario1.py", "--headless"]
