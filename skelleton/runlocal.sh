#!/bin/sh

npm run build
sudo docker build -f Dockerfile_local . -t samstack-local-test
sudo docker run -p 8080:8080 samstack-local-test
