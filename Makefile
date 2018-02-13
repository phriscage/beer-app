SHELL := /bin/bash

default: build

build:
	echo "Building TAG=${TAG}...";
	TAG=${TAG}; docker-compose -f docker-compose.build.yml build;

dev_build:
	echo "Development Building TAG=${TAG}...";
	TAG=${TAG}; docker-compose -f docker-compose.dev.yml build;

dev: dev_build
	echo "Running TAG=${TAG}...";
	TAG=${TAG}; docker-compose -f docker-compose.yml -f docker-compose.dev.yml up;

test: dev_build
	echo "Running TAG=${TAG}...";
	TAG=${TAG}; docker-compose -f docker-compose.yml -f docker-compose.dev.yml -f dependencies/docker-compose.details.yml up;

test-clean: 
	echo "Cleaning TAG=${TAG}...";
	TAG=${TAG}; docker-compose -f docker-compose.yml -f docker-compose.dev.yml -f dependencies/docker-compose.details.yml stop; 
	TAG=${TAG}; docker-compose -f docker-compose.yml -f docker-compose.dev.yml -f dependencies/docker-compose.details.yml rm -f;
