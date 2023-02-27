# DogeFuzz's Benchmark

This project is a benchmark for [DogeFuzz](https://github.com/dogefuzz/dogefuzz) project.

## Running the project using Docker

To run a benchmark using a script, copy the script.json file:

```
cp script.json.template script.json
```

And execute the script:

```
benchmark.sh script
```

To run all contracts available, run the follwing command passing the duration and type of fuzzing:

```
benchmark.sh all 30m directed_greybox
```

## Running the project locally
This project using Python 3.10 and [Poetry](https://python-poetry.org/) to manage its dependencies and virtual environment.

To run the project using a script, execute the following commands:
```
cp script.json.template script.json
poetry run benchmark script
```

To run the project with all available contracts, run the following command:

```
poetry run benchmark all 30m directed_greybox
```
