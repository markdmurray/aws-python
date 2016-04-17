import boto3


def main(keyname):
    ec2 = boto3.client('ec2')
    resp = ec2.create_key_pair(
        KeyName=keyname
        )
    print(resp['KeyMaterial'])

main("testkey")
