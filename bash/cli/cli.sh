#!/bin/bash

function help() {
  cat <<EOF
Usage: $retry [options] -- execute command
    -h, --help, -?              Print help.                    
    -v, --version               Print the current version and exit.
    -w, --write=<text>          Print out given text to the console.
EOF
}

function version() {
  version="0.1"
  echo "cfb-b ${version}"
}

function write() {
  echo "$1"
}

# show help for no arguments
if [ -z "$1" ]; then
  help
else
  case "$1" in
    "-h"|"--help"|"-?") help;;
    "-v"|"--version") version;;
    "-w"|"--write") write $2;;
    *) echo "$1 is not recognized! Please use --help to get list of existing commands."
  esac
fi
exit 0
