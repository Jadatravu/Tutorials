import boto3
import os
client = boto3.client(
    's3',
    # Hard coded strings as credentials, not recommended.
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY']
)

#creation of buckets
#client.create_bucket(Bucket='first-devops-bucket')

#listing of buckets
response = client.list_buckets()

for bucket in response['Buckets']:
    print bucket['Name']

