import boto3

client = boto3.client('rekognition')

response = client.detect_labels(
    Image={
        'S3Object': {
            'Bucket': 'computervisiontest619',
            'Name': 'elephant.jpeg',
        },
    },
)

print(response)