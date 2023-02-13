#!/bin/bash
set -e

docker build -t benchmark:1.0.0 --quiet .

docker run benchmark:1.0.0 $@
