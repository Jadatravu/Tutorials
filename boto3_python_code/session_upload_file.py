import boto3

session = boto3.Session(
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
    aws_session_token=SESSION_TOKEN, #optional
    region_name = 'us-west-2',
)

s3_client = session.client('s3')

#uploading a file
filename = 'file.txt'
bucket_name = str('first-devops-bucket')+str("03Oct19")

s3_client.upload_file(filename, bucket_name, filename)
