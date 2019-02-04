FROM ubuntu:18.04

#=============
# Set WORKDIR
#=============
WORKDIR /root

#============================
# Install Bats for unit-test
#============================
RUN apt-get -qqy update && \
	apt-get -qqy --no-install-recommends install bats \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* 

#=================
# Run the project
#=================
COPY cli/cli.sh /usr/local/bin/cfb-b
COPY cli/test.bats /root/tests.bats
