README.txt

ARP Network Scanner using Python and Scapy
------------------------------------------

This script performs an ARP scan on a local network to discover active devices. 
It sends ARP requests over a specified IP range and displays each device's IP and MAC address.

Requirements
------------
- Python 3.x
- scapy library

To install Scapy:
    pip install scapy

Usage
-----
1. Make sure you are running the script with administrative/root privileges.
2. Edit the line:
       target_ip = "192.168.1.1/24"
   to match the subnet of your local network.
3. Run the script:
       python script_name.py

Output
------
The script will print a list of all active devices on the specified network:

Example:
    Available devices in the network:
    IP                  MAC
    192.168.1.2         aa:bb:cc:dd:ee:ff
    192.168.1.3         11:22:33:44:55:66

How It Works
------------
- Creates an ARP request for each IP in the range.
- Broadcasts the request using Ethernet (ff:ff:ff:ff:ff:ff).
- Waits for devices to respond.
- Displays the IP and MAC addresses of each responsive device.

Author
------
Mohamed Ashraf Saber

