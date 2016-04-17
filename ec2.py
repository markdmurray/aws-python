import boto3


def main(keyname):
    f = open("/home/mark/.ssh/%s" % keyname, "w")
    ec2 = boto3.client('ec2')
    resp = ec2.create_key_pair(
        KeyName=keyname
        )
    key_contents = resp['KeyMaterial']
    f.write(key_contents)

main("testkey2")
