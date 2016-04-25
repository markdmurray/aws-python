# key pair creation
import boto3
import socket
import dns.resolver

ec2 = boto3.client('ec2')

def get_ip():
    resolver = dns.resolver.Resolver()
    resolver.nameservers = resolver.nameservers=[socket.gethostbyname('resolver1.opendns.com')]
    for rdata in resolver.query('myip.opendns.com','A'):
        return rdata

def create_key(keyname):
    #create file in users ssh directory to write contents of key
    f = open("/home/mark/.ssh/%s" % keyname, "w")
    resp = ec2.create_key_pair(
        KeyName=keyname
        )
    key_contents = resp['KeyMaterial']
    # write contents of key to file
    f.write(key_contents)

def create_security_group(groupname,ipaddress):
    resp = ec2.create_security_group(
            GroupName=groupname,
            Description="Automated dev instance",
            VpcId='vpc-a92e55cc'
            )
    groupid = resp['GroupId']
    create_ingress_rules(groupid,ipaddress)

def create_ingress_rules(groupid,ipaddress):
    get_ip()
    resp = ec2.authorize_security_group_ingress(
            GroupId=groupid,
            IpProtocol='tcp',
            FromPort=22,
            ToPort=22,
            CidrIp='%s/32' % ipaddress
            )

def latest_ami():
    resp = ec2.describe_images(
            Owners=[
                '137112412989',
                ],
            Filters=[
                {
                    'Name': 'name',
                    'Values': [
                        'amzn-ami-hvm-2016.*.x86_64-gp2',
                        ],
                    'Name': 'block-device-mapping.volume-type',
                    'Values': [
                        'gp2',
                        ],
                    },
                ]
            )
    print(resp[0]['Images'])



#def create_instance():

#def port_test():


#def ssh_login():


#def terminate_instance():


#ipaddress = get_ip()
#create_security_group('test',ipaddress)

latest_ami()
