###############################################################################
##  Name:   Dockerfile
##  Date:   2018-09-23
##  Developer:  Chris Page
##  Email:  phriscage@gmail.com
##  Purpose:   This Dockerfile contains the frontend application
################################################################################
## build stage
# Using official node runtime base apline image
FROM node:10.11-alpine as build-env

# Set the file maintainer (your name - the file's author)
MAINTAINER Chris Page <phriscage@gmail.com>

# Set the application directory
RUN mkdir -p /app
WORKDIR /app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json /app/

# Install app dependencies
RUN npm install 

# Bundle app source
COPY . .
RUN npm run build


### STAGE 2: Production Environment ###
FROM nginx:1.15-alpine
COPY --from=build-env /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
