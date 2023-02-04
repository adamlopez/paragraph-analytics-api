
BUILD_ID := $(shell git rev-parse --short HEAD 2>/dev/null || echo no-commit-id)
CONTAINER_NAME := paragraph-analytics-api

build:
	docker build -t $(CONTAINER_NAME):$(BUILD_ID) .

start:
	docker run -p 8000:8000 -it $(CONTAINER_NAME):$(BUILD_ID); true

test:
	python3 -m pytest