import boto3

#resource = boto3.resource("s3")
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