SHELL=/bin/bash
IMAGE_NAME=textbook-jupyter-service
COMMON_ARGS=--rm -p 8888:8888 -v ./textbook:/home/jovyan/textbook
.PHONY: check-docker build serve interactive build-book serve-book build-book-ci

check-docker:
	@if ! command -v docker &> /dev/null; then \
		echo "Docker is not installed. Please install it to continue."; \
		exit 1; \
	fi

build: check-docker
	docker build -t $(IMAGE_NAME) .

serve: check-docker build
	docker run $(COMMON_ARGS) $(IMAGE_NAME) start-notebook.sh --NotebookApp.notebook_dir=textbook 

interactive: check-docker build
	docker run -it $(COMMON_ARGS) $(IMAGE_NAME) /bin/bash

build-book: check-docker build
	@echo "Building static HTML version of the book..."
	@mkdir -p preview
	docker run --rm -v ./textbook:/home/jovyan/textbook -v ./preview:/home/jovyan/preview $(IMAGE_NAME) jupyter-book build --path-output /home/jovyan/preview /home/jovyan/textbook
	@echo "Book built successfully. You can find it in the 'preview/html' directory."

serve-book: build-book
	@echo "Starting local server for the book at http://localhost:8001"
	@echo "Press Ctrl+C to stop."
	@docker run --rm -p 8001:4000 -v ./preview/html:/home/jovyan/html -w /home/jovyan/html $(IMAGE_NAME) python3 -m http.server 4000 --bind 0.0.0.0

build-book-ci: check-docker build
	@echo "Building static HTML version of the book for CI..."
	@rm -rf preview
	@mkdir -p preview
	-docker rm temp-build-ci 2>/dev/null || true
	docker run --name temp-build-ci -v ./textbook:/home/jovyan/src $(IMAGE_NAME) sh -c "cp -r /home/jovyan/src /home/jovyan/textbook && jupyter-book build /home/jovyan/textbook"
	docker cp temp-build-ci:/home/jovyan/textbook/_build/html ./preview/
	docker rm temp-build-ci
	@echo "Book built successfully. You can find it in the 'preview/html' directory."

