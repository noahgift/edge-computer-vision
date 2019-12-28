import json
import boto3

def detect(name):
    print(f"Passed in this name")
    rekognition = boto3.client("rekognition")
    response = rekognition.detect_labels(
		Image={
			"S3Object": {
				"Bucket": "dec27computervision",
				"Name": "fig_7_titan_small.jpg",
			}
		},
    )
    print(response)
    return response
    
def lambda_handler(event, context):
    if 'body' in event:
        event = json.loads(event["body"])
    print(f"Received this body: {event}")
    name = event["name"]
    return detect(name)