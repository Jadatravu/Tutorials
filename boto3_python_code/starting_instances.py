import boto3
import os
from botocore.exceptions import ClientError
client = boto3.client(
    'ec2',
    # Hard coded strings as credentials, not recommended.
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
    region_name='us-east-2'
)



"""
response = client.describe_instances()
print(response)
print(response["Reservations"][0]["Instances"])
print(response["Reservations"][0]["Instances"][0].keys())
print(response["Reservations"][0]["Instances"][0]["InstanceId"])
"""

instance_id="i-0beaa139f7c98d9b1"
try:
        response = client.start_instances(InstanceIds=[instance_id], DryRun=False)
        print(response)
except ClientError as e:
        print(e)


