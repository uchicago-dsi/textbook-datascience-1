ARG BASE_CONTAINER=jupyter/scipy-notebook
FROM $BASE_CONTAINER

COPY requirements.txt /usr/local/share/requirements.txt

RUN pip install -r /usr/local/share/requirements.txt\
    && pip install sphinx-proof\
    && pip list
