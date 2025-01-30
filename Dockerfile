FROM python:3.9

# Update and install system packages
RUN apt-get update -y && \
    apt-get install --no-install-recommends -y -q \
    git libpq-dev python3-dev unzip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install DBT
RUN pip install --upgrade pip && \
    pip install boto3 streamlit

# Install AWS CLI v2
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install

# Set environment variables
ENV PYTHONIOENCODING=utf-8
ENV LANG C.UTF-8

# Set WORKDIR and VOLUME
WORKDIR /usr/app
VOLUME /usr/app
