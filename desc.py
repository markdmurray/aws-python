import boto3
ec2 = boto3.resource('ec2')
describe = ec2.meta.client.describe_instance_status()['InstanceStatuses']

#print(describe[0]['InstanceId'])

for x in describe:
    print(x['InstanceId'])
