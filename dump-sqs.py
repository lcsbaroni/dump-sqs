#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import json
import os
import boto3

def get_messages_from_queue(queue_url):
    print("Connecting to AWS: ")
    sqs_client = boto3.client('sqs')

    messages = []

    print("Reading queue: ", queue_url)
    while True:
        resp = sqs_client.receive_message(
            QueueUrl=queue_url,
            AttributeNames=['All'],
            MaxNumberOfMessages=10
            # https://boto3.amazonaws.com/v1/documentation/api/1.9.42/reference/services/sqs.html#SQS.Client.receive_message
            # MaxNumberOfMessages (integer) -- The maximum number of messages to return. Amazon SQS never returns more messages than this value (however, fewer messages might be returned). Valid values: 1 to 10. Default: 1.
        )

        try:
            messages.extend(resp['Messages'])
        except KeyError:
            break

    return messages


if __name__ == '__main__':
    # Get environment variables
    queue_url = os.getenv('QUEUE_URL')
    file_path = os.getenv('FILE_PATH')

    messages = []
    for message in get_messages_from_queue(queue_url):
        messages.append(message)

    print("Writing ", len(messages) ," messages on file: ",file_path)
    with open(file_path, 'w') as outfile:
        json.dump(messages, outfile, indent = 2)
