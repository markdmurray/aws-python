import boto3

ec2 = boto3.client('ec2')

resp = ec2.describe_instances(
    InstanceIds=[
        'i-1bbdcf8c',
        ],
    )

resp = resp['Reservations']

for x in resp:
    x = x['Instances']
    for y in x:
        print(y['PublicDnsName'])
