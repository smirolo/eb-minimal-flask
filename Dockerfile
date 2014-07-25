FROM ubuntu:12.04

RUN apt-get -y update
RUN apt-get -y install python python-pip build-essential git-core
RUN git clone https://github.com/smirolo/eb-minimal-flask.git
RUN pip install eb-minimal-flask/requirements.txt
RUN apt-get -y purge build-essential
RUN apt-get -y autoremove

EXPOSE 80

CMD ["/usr/bin/python", "eb-minimal-flask/hello.py" ]
