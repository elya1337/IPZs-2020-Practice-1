import ipaddress 

an_address = ipaddress.ip_address('93.220.0.1')
a_network = ipaddress.ip_network('93.220.0.0/24')

address_in_network = an_address in a_network

print(address_in_network)