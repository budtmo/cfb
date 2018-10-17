FROM ubuntu:18.04

#=============
# Set WORKDIR
#=============
WORKDIR /root

#================
# Install Python
#================
RUN apt-get -qqy update && \
	apt-get -qqy --no-install-recommends install \
	python3.6-dev python3-pip python3-setuptools python3-wheel gcc \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  && update-alternatives --install /usr/bin/python python /usr/bin/python3 1 \
  && update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1

#============
# Set Locale
#============
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

#=================
# Run the project
#=================
COPY . /root/
RUN pip install -e $(pwd)
CMD cfb-python
