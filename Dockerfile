FROM centos:latest

# RUN rpm --import http://mirror.centos.org/centos/RPM-GPG-KEY-CentOS-7
# RUN rpm -Uvh http://download.fedoraproject.org/pub/epel/beta/7/x86_64/epel-release-7.0.1406.noarch.rpm
RUN yum install -y python python-virtualenv git-all gcc
# gcc because markupsafe pulled as dependency for Flask
RUN git clone https://github.com/smirolo/eb-minimal-flask.git
RUN virtualenv-2.7 virtualenv
RUN virtualenv/bin/pip install -r eb-minimal-flask/requirements.txt

EXPOSE 80

CMD ["virtualenv/bin/python", "eb-minimal-flask/hello.py" ]
