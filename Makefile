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
