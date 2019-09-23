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


"""
response = client.describe_instances()
print(response)
print(response["Reservations"][0]["Instances"])
print(response["Reservations"][0]["Instances"][0].keys())
print(response["Reservations"][0]["Instances"][0]["InstanceId"])
"""
instance_id="i-0beaa139f7c98d9b1"
try:
    # create an EBS volume, 20G size
    ebs_vol = client.create_volume(
        Size=20,
        AvailabilityZone='us-east-2'
    )

    volume_id = ebs_vol['VolumeId']

# check that the EBS volume has been created successfully
    if ebs_vol['ResponseMetadata']['HTTPStatusCode'] == 200:
        print "Successfully created Volume! " + volume_id
    # attaching EBS volume to our EC2 instance
    attach_resp = client.attach_volume(
        VolumeId=volume_id,
        #InstanceId=ec2_instance['Instances'][0]['InstanceId'],
        InstanceId=instance_id,
        Device='/dev/sdm'
    )
    print(attach_response)
    #response = client.reboot_instances(InstanceIds=[instance_id], DryRun=False)
    #print(response)
except ClientError as e:
        print(e)
