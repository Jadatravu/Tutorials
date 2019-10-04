import boto3

ec2 = boto3.resource(
    'ec2',
    # Hard coded strings as credentials, not recommended.
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
    region_name='us-east-1'
)


instance = ec2.create_instances(
    ImageId='ami-0b2f2d7c5173e3a44',
    MinCount=1,
    MaxCount=1,
    KeyName="",
    InstanceType='t2.micro',
    SubnetId='',
)
print(instance[0].id)

