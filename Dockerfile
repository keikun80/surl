FROM python:3.13
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
CMD ["fastapi","run","app/main.py","--port","80"] 
HEALTHCHECK --interval=1m CMD curl --fail http://localhost:80 || exit 1
