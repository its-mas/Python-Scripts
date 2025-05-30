from scapy.all import ARP, Ether, srp
import socket
import argparse

target_ip = "192.168.1.1/24" 

# Ip address for the destination
# Create ARP packet

arp = ARP(pdst = target_ip)

# Create the ether brodcast packet
# ff:ff:ff:ff:ff:FF MAC address indicates brodcasting
ether = Ether(dst = "ff:ff:ff:ff:ff:ff")

# stack them

packet = ether/arp

result = srp(packet, timeout = 3)[0]

# a list of clients, we will fill this in the upcoming loop
clients = []

for sent, received in result:
    # for each response, append ip and mac address to 'clients' list
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})

#print clients

print("Available devices in the network :\n")
print("IP" + " " * 18 + "MAC")
for client in clients:
    print("{:16}    {}".format(client['ip'], client['mac']))
