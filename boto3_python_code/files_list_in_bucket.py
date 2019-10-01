import boto3
import os
client = boto3.client(
    's3',
    # Hard coded strings as credentials, not recommended.
    #aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_access_key_id=""
    #aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY']
    aws_secret_access_key=""
)

#creation of buckets
#client.create_bucket(Bucket='first-devops-bucket')

#listing of buckets
response = client.list_buckets()

for bucket in response['Buckets']:
    print bucket['Name']
    bu = boto3.resource('s3',aws_access_key_id="",\
                        aws_secret_access_key="").Bucket(bucket['name'])
    for file in bu.objects.all():
        print(file)
