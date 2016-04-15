import boto3

ec2 = boto3.client('ec2')

resp = ec2.create_key_pair(
        KeyName='testp'
        )

print(resp)
