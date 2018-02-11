# Beer App
This application provides information about Beers. The Beer data is constructed from various Beer microservices.

* [Prerequisites](#prerequisites)
* [Setup](#setup)
* [Development](#development)
* [Deployment](#deployment)


## <a name="prerequisites"></a>Prerequisites:
* [Docker](https://www.docker.com) installed and running
* [Docker Compose](https://www.docker.com/products/docker-compose) installed
* [Node](https://nodejs.org/en/) installed
* [Npm](https://www.npmjs.com/) installed


## <a name="setup"></a>Setup:
Install the Node packages via NPM
        
        cd frontend
        npm install

## <a name="development"></a>Development:
Build and run the development environment as a Node instance and Docker application locally. Make changes accordingly.

Frontend:
        
        cd frontend
        npm build dev

Backend

        TAG=dev make dev

## To-Do
* automated builds
