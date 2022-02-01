#!/bin/sh
mkdir ./data
docker build -t coin-app .
docker run -d -v $PWD/data:/src/data -p 3000:3333 coin-app
