import boto3
from botocore.exceptions import ClientError

from datetime import datetime,date

import  os

today_string = date.today().strftime('%Y/%m/%d')
client = boto3.resource(
    'ec2',
    # Hard coded strings as credentials, not recommended.
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
    region_name='us-east-2'
)


for instance in client.instances.all( ):
   print instance
   if instance.id == 'i-0beaa139f7c98d9b1':
       for vol in instance.volumes.all():
           print vol
           name =today_string
           snapshot = vol.create_snapshot( Description = 'AutoSnapshot of {0}, on volume {1} - Created {2}'.format(name, vol.id, today_string),)
           snapshot.create_tags(Tags = [ { 'Key': 'auto_snap', 'Value': 'true' }, { 'Key': 'volume', 'Value': vol.id }, { 'Key': 'CreatedOn', 'Value': today_string }, { 'Key': 'Name', 'Value': '{} autosnap'.format(name) } ])



