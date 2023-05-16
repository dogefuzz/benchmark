#!/bin/bash
set -e

mkdir -p results

echo "[1] Starting fuzzer and dependencies"
docker compose up -d;

echo "[1.1] Wait for all containers to be healthy"
while true; do
  health_status=$(docker inspect --format='{{.State.Health.Status}}' dogefuzz_api);

  if [ "$health_status" = "healthy" ]; then
    echo "All containers are healthy";
    break;
  fi

  sleep 5;
done

echo "[2] Building benchmark container image"
docker build -t benchmark:1.0.0 --quiet .;

echo "[3] Running benchmark"
docker run \
    --network dogefuzz_benchmark \
    --network-alias benchmark \
    --name dogefuzz_benchmark \
    -p "5000:5000" \
    -v "$PWD/result.json:/app/result.json" \
    -v "$PWD/results:/app/results" \
    benchmark:1.0.0 \
    $@;

echo "[4] Stopping all containers"
docker rm -f dogefuzz_benchmark > /dev/null;
docker compose down > /dev/null;
