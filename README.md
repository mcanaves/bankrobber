# Bank Robber CLI

[![Build Status](https://travis-ci.com/mcanaves/bankrobber.svg?branch=master)](https://travis-ci.com/mcanaves/bankrobber)

Just another CLI to request information from N26 bank accounts :gun: :sunglasses:.

## Prerequisites

You’ll need at least Docker 1.17.

If you don’t already have it installed, follow the instructions for your OS:

- On Mac OS X, you’ll need [Docker for Mac](https://docs.docker.com/docker-for-mac/)
- On Windows, you’ll need [Docker for Windows](https://docs.docker.com/docker-for-windows/)
- On Linux, you’ll need [docker-engine](https://docs.docker.com/engine/installation/)

## Usage

Simply run the following script to see all commands and options:

**Note:** *docker image must be built before try to run this script. See development section.*

```bash
./scripts/run --help
```

## Development

To work with this codebase you'll want to clone the repository and build the docker image:

```bash
git clone git@github.com:mcanaves/bankrobber
cd bankrobber
./scripts/setup
```

To lint the code and run the tests run the following scripts:

**Note:** *docker image must be built before try to run any of these scripts. See development section.*

```bash
./scripts/lint
./scripts/test
```

<p align="center">&mdash; Built with :heart: in Pollença City &mdash;</p>
