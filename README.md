# DUMP SQS
## A simple way to get a sample of messages at SQS

Dump SQS is a script running on docker with Python 3 that get message on AWS SQS and write on local file(json).
Also, you can run script locally to.

The messages are read and return to queue and not are deleted.
CAUTION: Each message have a counter of number of reads. Depends of your queue configuration, this number can trigger the process to move message to DLQ.

## How to use

To run with docker, set your AWS Credentials on `.env`
```
cp .env.example .env
```
and run the command bellow:
```
docker-compose up
```

To run locally, export your AWS Credentials like this example:
```
export QUEUE_URL=queue_url
export FILE_PATH=queue_sample.json
export AWS_DEFAULT_REGION=us-east-1
export AWS_ACCESS_KEY_ID=aws_access_key
export AWS_SECRET_ACCESS_KEY=aws_secret_access_key
export AWS_SESSION_TOKEN=aws_session_token
```
 and then:
```
python3 dump-sqs.py
```
