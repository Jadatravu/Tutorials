import boto3
from botocore.exceptions import ClientError
import os

client = boto3.client(
    'ec2',
    # Hard coded strings as credentials, not recommended.
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
    region_name='us-east-2'
)

ebs_vol = client.create_volume(
        Size=20,
        AvailabilityZone='us-east-2'
    )

volume_id = ebs_vol['VolumeId']
print(volume_id)

