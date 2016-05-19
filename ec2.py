# key pair creation
#pip packages required, dnspython3
import boto3
import socket
import dns.resolver
import getpass

ec2 = boto3.client('ec2')
current_user = getpass.getuser()

def get_ip():
    resolver = dns.resolver.Resolver()
    resolver.nameservers=[socket.gethostbyname('resolver1.opendns.com')]
    for rdata in resolver.query('myip.opendns.com','A'):
        return rdata

def create_key(keyname):
    #create file in users ssh directory to write contents of key
    f = open("/home/%s/.ssh/%s" %(current_user,keyname), "w")
    resp = ec2.create_key_pair(
        KeyName=keyname
        )
    key_contents = resp['KeyMaterial']
    keyname = resp['KeyName']
    # write contents of key to file
    f.write(key_contents)
    return keyname


def create_security_group(groupname,ipaddress):
    resp = ec2.create_security_group(
            GroupName=groupname,
            Description="Automated dev instance",
            VpcId='vpc-a92e55cc'
            )
    groupid = resp['GroupId']
    create_ingress_rules(groupid,ipaddress)
    return groupid

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
    array = []
    resp = ec2.describe_images(
            Owners=[
                '137112412989',
                ],
            Filters=[
                {
                    'Name': 'name',
                    'Values': [
                        'amzn-ami-hvm-2016*',
                      ],
                    },
                {
                    'Name': 'block-device-mapping.volume-type',
                    'Values': [
                        'gp2',
                        ],
                    },
                ]
            )
    output = resp['Images']
    for x in output:
        array.append(x['ImageId'])
    sorted_list = sorted(array)
#    sorted_list = sorted_list[-1]
    for x in sorted_list:
        return x.strip('"')



def create_instance(ami_id, key, security_group):
    resp = ec2.run_instances(
               ImageId=ami_id,
               KeyName=key,
               InstanceType='t2.micro',
               MinCount=1,
               MaxCount=1,
               SubnetId='subnet-abefbadc',
               SecurityGroupIds=[
                   security_group,
                   ],
               )
    output = resp['Instances']
    for x in output:
        return x['InstanceId']


def wait_running(instance_id):
    print(instance_id)
    waiter = ec2.get_waiter('instance_running')
    resp = waiter.wait(
               InstanceIds=[
                   instance_id,
                   ],
               )




#def port_test():


#def ssh_login():


#def terminate_instance():

ami_id = latest_ami()
key = create_key('test6')
ipaddress = get_ip()
security_group = create_security_group('test6',ipaddress)
instance_id = create_instance(ami_id, key, security_group)
if wait_running(instance_id) == None:
    print('Instance %s is in the running state' % instance_id)
else:
    print('something happened, cloud is broken')

