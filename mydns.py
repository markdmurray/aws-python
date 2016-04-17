import socket
import dns.resolver

resolver = dns.resolver.Resolver()
resolver.nameservers = resolver.nameservers=[socket.gethostbyname('resolver1.opendns.com')]
for rdata in resolver.query('myip.opendns.com','A'):
    print(rdata)
