import boto3
import json

def lambda_handler(event, context):
    if 'body' in event:
        event = json.loads(event["body"])
    image = event["image"]
    rekognition = boto3.client("rekognition")
    response = rekognition.detect_labels(
		Image={
			"S3Object": {
				"Bucket": "demoapril10",
				"Name": image,
			}
		},
	)

    print(response)
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
