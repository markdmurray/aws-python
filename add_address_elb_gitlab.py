import dns.resolver
import socket
import boto3

ec2 = boto3.client('ec2')

def get_ip():
    resolver = dns.resolver.Resolver()
    resolver.nameservers=[socket.gethostbyname('resolver1.opendns.com')]
    for rdata in resolver.query('myip.opendns.com','A'):
        return(rdata)

def create_ingress_rules(ipaddress):
    resp = ec2.authorize_security_group_ingress(
            GroupId='sg-5819dd3c',
            IpProtocol='tcp',
            FromPort=443,
            ToPort=443,
            CidrIp='%s/32' % ipaddress
            )

ip_address = get_ip()
create_ingress_rules(ip_address)
