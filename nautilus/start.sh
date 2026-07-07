#!/bin/bash

NAME=djrhee

if [ "$1" = "0" ]; then
    sed "s/djrhee/$NAME/g" session.yml | kubectl apply -f -
elif [ "$1" = "1" ]; then
    kubectl delete deployment ${NAME}-sim2real
else
    echo "Usage: start.sh 0 (open) | 1 (close)"
fi
