import boto3

class aws_cls(object):
    def __init__(self):
        aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID']
        aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY']
        aws_session = boto3.Session(
                   aws_access_key_id=aws_access_key_id,
                   aws_secret_access_key=aws_secret_access_key,                   
                   region_name = 'us-east-1',
                   )
        self.ec2_resource = aws_session.resource('ec2')
        self.s3_resource = aws_session.resource('s3')
        self.ec2_client = aws_session.client('ec2')
        self.s3_client = aws_session.client('s3')
    def upload_file(self,local_file_name,remote_file_name,bucket_name):
        self.s3_client.upload_file(local_file_name, bucket_name, remote_file_name)

    def create_bucket(self,bucket_name):
        self.s3_resource.create_bucket(Bucket=bucket_name)

    def list_volumes(self):
        list_volume_ids=[]
        volumes = self.ec2_resource.volumes.all()
        for volume in volumes:
            print(volume.id)
            list_volume_ids.append(volume.id)
        return list_volume_ids
        
    def count_snapshots(self):
        response = self.ec2_client.describe_snapshots()
        print(response.keys())
        print(len(response['Snapshots']))
        print(response['Snapshots'][0].keys())
        return len(response['Snapshots'])
        

