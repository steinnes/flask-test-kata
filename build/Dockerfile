FROM ubuntu
MAINTAINER Steinn Eldjarn Sigurdarson <steinn@plainvanillagames.com>
ENV DEBIAN_FRONTEND noninteractive

# Install basic packages
RUN apt-get update && apt-get upgrade -y
RUN apt-get update \
 && apt-get upgrade -y \
 && apt-get install -y htop make build-essential ntp python-dev python-pip libssl-dev

# Install Python packages
RUN pip install requests raven virtualenv virtualenv-tools circus ipython uwsgi boto honcho
ADD requirements.txt /app/requirements.txt
RUN cd /app && pip install -r /app/requirements.txt
ADD src.tgz /app
CMD uwsgi --yaml /app/build/uwsgi.yaml
