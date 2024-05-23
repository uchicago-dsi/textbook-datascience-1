FROM quay.io/jupyter/scipy-notebook:2025-03-14

COPY requirements.txt /usr/local/share/requirements.txt

RUN pip install -r /usr/local/share/requirements.txt \
    && pip install sphinx-proof \
    && pip list
