# key pair creation

import boto3

ec2 = boto3.client('ec2')
def create_key(keyname):
    #create file in users ssh directory to write contents of key
    f = open("/home/mark/.ssh/%s" % keyname, "w")
    resp = ec2.create_key_pair(
        KeyName=keyname
        )
    key_contents = resp['KeyMaterial']
    # write contents of key to file
    f.write(key_contents)

def create_security_group(groupname):
    resp = ec2.create_security_group(
            GroupName=groupname,
            Description="Automated dev instance",
            VpcId='vpc-a92e55cc'
            )
    groupid = resp['GroupId']
    print(groupid)
create_security_group('auto')
