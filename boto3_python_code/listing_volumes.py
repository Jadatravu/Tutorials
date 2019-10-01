import boto3

ec2 = boto3.resource(
    'ec2',
    # Hard coded strings as credentials, not recommended.
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
    region_name='us-east-2'
)

volumes = ec2.volumes.all()

for volume in volumes:
    print(volume.id)
