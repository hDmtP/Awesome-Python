from ipwhois import IPWhois
from pprint import pprint
ipaddress = str(input("Enter the ip address: \n"))
obj = IPWhois(ipaddress)
results = obj.lookup_rdap(depth=1)
pprint(results)

print("----------------------------------------------------------------------------------------------------")

from urllib import request

handler = request.ProxyHandler({
        'http': 'http://192.168.0.1:80/',
        'https': 'https://192.168.0.1:443/'
    })
opener = request.build_opener(handler)
obj = IPWhois('74.125.225.229', proxy_opener = opener)