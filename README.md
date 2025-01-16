# github-firehose-quixio
A real-time stream of all the public events going through Github's API.

## Prerequisites

### Install Quix

```bash
curl -fsSL https://github.com/quixio/quix-cli/raw/main/install.sh | bash
quix --help
quix status
```

###  Install librdkafka

```bash
brew install librdkafka
export CFLAGS="-I/opt/homebrew/Cellar/librdkafka/2.6.1/include"
export LDFLAGS="-L/opt/homebrew/Cellar/librdkafka/2.6.1/lib"
```

### Install Python Dependencies

```bash
pip install -r requirements.txt
```

## Run

### Run Quix Pipeline

```bash
(venv) (base) vishalgattani@Vishals-MacBook-Pro github-firehose-quixio % quix pipeline up
✗ Docker needs to be installed in order to run this command.
# install Docker for Mac: https://docs.docker.com/docker-for-mac/install/

(venv) (base) vishalgattani@Vishals-MacBook-Pro github-firehose-quixio % quix pipeline up
✗ 'quix.yaml' was not found
# create a 'quix.yaml' file in the root of your project
# see https://quix.io/docs/quix-cli/yaml-reference/pipeline-descriptor.html#best-practices for more information
(venv) (base) vishalgattani@Vishals-MacBook-Pro github-firehose-quixio % cat quix.yaml
# Quix Project Descriptor
# This file describes the data pipeline and configuration of resources of a Quix Project.
metadata:
  version: 1.0
# This section describes the Deployments of the data pipeline
deployments: []
# This section describes the Topics of the data pipeline
topics: []
(venv) (base) vishalgattani@Vishals-MacBook-Pro github-firehose-quixio % quix pipeline up
  Generating 'compose.local.yaml'
! No deployments found
✓ Generated 'compose.local.yaml'

Executing 'docker compose -f compose.local.yaml up --build -d --remove-orphans
kafka_broker'

[+] Running 6/6
 ✔ kafka_broker Pulled                                                     7.6s
   ✔ 22d97f6a5d13 Pull complete                                            2.5s
   ✔ edeb22f0d581 Pull complete                                            2.7s
   ✔ 3609efb86686 Pull complete                                            2.7s
   ✔ a4414af7c7bd Pull complete                                            2.9s
   ✔ 9f313c00445c Pull complete                                            4.9s
[+] Running 2/2
 ✔ Network github-firehose-quixio_default           Created                0.0s
 ✔ Container github-firehose-quixio-kafka_broker-1  Started                0.7s
! No topics specified

Executing 'docker compose -f compose.local.yaml up --build -d --remove-orphans'

[+] Running 8/8
 ✔ console Pulled                                                          6.6s
   ✔ bca4290a9639 Pull complete                                            1.0s
   ✔ f956afea6f2c Pull complete                                            1.0s
   ✔ 812ea3a264e5 Pull complete                                            1.0s
   ✔ ea843e68d75f Pull complete                                            4.1s
   ✔ 65cddddd697c Pull complete                                            4.3s
   ✔ 52fc8902fe27 Pull complete                                            4.4s
   ✔ 1c75b1e8ceb9 Pull complete                                            4.4s
[+] Running 2/2
 ✔ Container github-firehose-quixio-console-1       Started                1.0s
 ✔ Container github-firehose-quixio-kafka_broker-1  Running                0.0s
✓ Open http://localhost:8080 to manage your pipeline broker
```


```bash
python main.py
```