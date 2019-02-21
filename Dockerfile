FROM python:3.7

COPY run.py .

RUN pip install nltk
RUN python -m nltk.downloader punkt

ENTRYPOINT [ "python", "run.py"]