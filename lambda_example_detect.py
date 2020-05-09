import boto3

def labels(bucket, name):
	"""This takes an S3 bucket and a image name"""
	
	print(f"This is the bucketname {bucket} !")
	print(f"This is the imagename {name} !")
	rekognition = boto3.client("rekognition")
	response = rekognition.detect_labels(
			Image={
				"S3Object": {
					"Bucket": bucket,
					"Name": name,
				}
			},
		)
	return response


def lambda_handler(event, context):
    print(f"You gave me this event: {event}")
    bucket = event["bucket"]
    name = event["name"]
    response = labels(bucket, name)
    print(f"THIS IS THE RAW RESPONSE: {response}")
    return response['Labels']
    
    
    
