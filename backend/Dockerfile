###############################################################################
##  Name:   Dockerfile
##  Date:   2018-02-11
##  Developer:  Chris Page
##  Email:  phriscage@gmail.com
##  Purpose:   This Dockerfile contains an example process
################################################################################
# Using official python runtime base apline image
FROM python:3.6-alpine

# Set the file maintainer (your name - the file's author)
MAINTAINER Chris Page <phriscage@gmail.com>

# Set the application directory
WORKDIR /app

# Copy the requirements
ADD requirements.txt /app/requirements.txt

# Add the dependencies for SQLAlchemy and MySQLdb
# Install our requirements and clean-up
RUN pip install -r requirements.txt && \
      rm -rf .cache/pip 

# Explicitly copy our files from the current folder to /app inside the container
ADD api /app/api 
ADD lib /app/lib 

#EXPOSE 8080
EXPOSE 5000

# Define our command to be run when launching the container
ENTRYPOINT ["python", "/app/api/main.py"]
