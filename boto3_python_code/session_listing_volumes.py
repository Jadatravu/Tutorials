import boto3

session = boto3.Session(
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
    aws_session_token=SESSION_TOKEN, #optional
    region_name = 'us-east-1',
)

ec2_resource = session.resource('ec2')

#listing volumes
volumes = ec2_resource.volumes.all()

for volume in volumes:
    print(volume.id)
