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

To edit the textbook's content, use the `notebook` command. This will start a live Jupyter Lab server.

```bash
make notebook
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

You can then view the book in your browser at `http://localhost:4000`.

## Available `make` Commands

Here is a summary of all available commands:

- `make check-docker`: Verifies that Docker is installed and running.
- `make build`: Builds the Docker image with all necessary dependencies.
- `make notebook`: Starts a Jupyter Lab server for editing the course content.
- `make interactive`: Starts an interactive `bash` session inside the Docker container for debugging.
- `make build-book`: Generates the static HTML version of the book.
- `make serve-book`: Serves the generated static HTML book for local preview.

## How to Update

**Important**: This project should only be run via [Make](https://www.gnu.org/software/make/) and [Docker](https://docs.docker.com/get-docker/). Do not attempt to run the project directly without these tools.

To contribute updates to the textbook, follow this workflow:

1. **Pull the latest changes**: Before making any edits, ensure you have the most up-to-date version:
   ```bash
   git pull origin main
   ```

2. **Create a new branch**: Create a new branch for your changes:
   ```bash
   git checkout -b your-branch-name
   ```

3. **Make your changes**: Update or add content using the Docker/Make workflow described above:
   - Use `make notebook` to edit content in Jupyter Lab
   - Use `make build-book` to test your changes locally
   - Use `make serve-book` to preview the built book

4. **Push your branch**: Push your changes to GitHub:
   ```bash
   git add .
   git commit -m "Description of your changes"
   git push origin your-branch-name
   ```

5. **Create a Pull Request**: Create a pull request from your branch into the `dev` branch (not `main`). All changes must be reviewed before being merged.

## Hosting

This textbook is hosted on [Vercel](https://vercel.com/) with automatic deployments:

- **Development Preview**: Any pull request into the `dev` branch automatically builds a preview page that can be accessed at: https://textbook-datascience-1-dev.vercel.app/intro.html

- **Production Site**: Any merge into the `main` branch generates a new version of the live site at: https://ds1.datascience.uchicago.edu/intro.html

This setup allows for testing changes in a preview environment before they go live to students.