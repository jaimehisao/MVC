FROM python:3.10-buster

ENV PYTHONUNBUFFERED=1
ENV HOST=0.0.0.0
ENV PORT=8000

WORKDIR /code
COPY .. /code/

RUN pip install --upgrade pip \
 && pip install -r requirements.txt
EXPOSE 8000
CMD uvicorn webapp.main:app --host ${HOST} --port ${PORT}
