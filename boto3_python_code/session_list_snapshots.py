import boto3

session = boto3.Session(
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
    aws_session_token=SESSION_TOKEN, #optional
    region_name = 'us-east-1',
)

ec2_client = session.client('ec2')

#listing snapshots
response = ec2_client.describe_snapshots()
print(response.keys())
print(len(response['Snapshots']))
print(response['Snapshots'][0].keys())
