#!/bin/bash
set -e

docker compose up -d

docker build -t benchmark:1.0.0 --quiet .

rm -f result.json
touch result.json

docker run \
    --network dogefuzz_benchmark \
    --network-alias benchmark \
    --name dogefuzz_benchmark \
    -p "5000:5000" \
    -v "$PWD/result.json:/app/result.json" \
    benchmark:1.0.0 \
    $@

docker rm -f dogefuzz_benchmark > /dev/null
