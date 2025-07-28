# Textbook: Data Science I

This repository contains the source materials for the University of Chicago's "Introduction to Data Science I & II" course.

All textbook content is generated from Jupyter Notebooks and Markdown files using [Jupyter Book](https://jupyterbook.org/).

## Getting Started

### Prerequisites

Before you begin, you will need to have [Docker](https://docs.docker.com/get-docker/) installed on your computer.

### Setup & Workflow

This project uses a `Makefile` to simplify the development process. Here are the main commands you will use:

#### 1. Build the Docker Image

This command builds the necessary Docker image that contains all the dependencies for the textbook. You only need to run this once initially, and then again anytime the `requirements.txt` file changes.

```bash
make build
```

#### 2. Edit Content (Live Editing)

To edit the textbook's content, use the `serve` command. This will start a live Jupyter Lab server.

```bash
make serve
```

You can then access the Jupyter environment by navigating to the URL provided in the terminal output. All the source files for the textbook are located in the `textbook/` directory.

#### 3. Build the Static HTML Book

To compile the notebooks and markdown files into a static HTML book, run the `build-book` command.

```bash
make build-book
```

This will generate the static site in the `preview/html/` directory. **Note that this can take quite a while**

#### 4. Preview the Static Book

To view the generated HTML book, you can use the `serve-book` command. This will start a simple web server.

```bash
make serve-book
```

You can then view the book in your browser at `http://localhost:8001`.

## Available `make` Commands

Here is a summary of all available commands:

- `make check-docker`: Verifies that Docker is installed and running.
- `make build`: Builds the Docker image with all necessary dependencies.
- `make serve`: Starts a Jupyter Lab server for editing the course content.
- `make interactive`: Starts an interactive `bash` session inside the Docker container for debugging.
- `make build-book`: Generates the static HTML version of the book.
- `make serve-book`: Serves the generated static HTML book for local preview. 