FROM python:3.10.2-slim

RUN useradd -ms /bin/bash python

USER python

WORKDIR /home/python/app

CMD [ "tail", "-f", "/dev/null" ]
