FROM node:8

#=============
# Set WORKDIR
#=============
WORKDIR /root

#=================
# Run the project
#=================
COPY . /root/
RUN npm install -g ./
CMD cfb-js --help
