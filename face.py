import boto3

client = boto3.client('rekognition')

response = client.detect_faces(
    Image={
        'S3Object': {
            'Bucket': 'dec27computervision',
            'Name': 'jeff_portrait.jpg',
        },
    },
)

print(response)