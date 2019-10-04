import boto3

session = boto3.Session(
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
    aws_session_token=SESSION_TOKEN, #optional
    region_name = 'us-east-1',
)


s3_resource = session.resource('s3')

#creation of buckets
bucket_name =str('first-devops-bucket')+str('03Oct19')
s3_resource.create_bucket(Bucket=bucket_name)
