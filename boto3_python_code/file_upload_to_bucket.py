
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


#uploading a file
filename = 'file.txt'
bucket_name = 'first-devops-bucket'

client.upload_file(filename, bucket_name, filename)

#downloading file
local_file_name = "local_file.txt"
remote_file_name = "remote_file.txt"

client.download_file(bucket_name, remote_file_name, local_file_name)

