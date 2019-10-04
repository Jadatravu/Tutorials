import boto3

session = boto3.Session(
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
    aws_session_token=SESSION_TOKEN, #optional
    region_name = 'us-west-2',
)

ec2_resource = session.resource('ec2')
s3_resource = session.resource('s3')

ec2_client = session.client('ec2')
s3_client = session.client('s3')
