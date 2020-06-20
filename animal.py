#!/usr/bin/env python3

import click
import boto3

@click.command(help="This code detects animals")
@click.option('--file', prompt='I need your file!',
              help='This is the name of the file')
def detect(file):
    client = boto3.client('rekognition')

    response = client.detect_labels(
        Image={
            'S3Object': {
                'Bucket': 'computervisiontest619',
                'Name': file,
            },
        },
    )

    print(response)

if __name__ == '__main__':
    detect()