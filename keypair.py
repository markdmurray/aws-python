# keypair creation for ec2

import boto3

def main(keyname):
    ec2 = boto3.resource('ec2')
    keypair = ec2.KeyPair(str(keyname))
    print(keypair)

main("testkey")
