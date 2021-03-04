#!/usr/bin/env python

import scapy.all as scapy
import re
import optparse
import subprocess
#%%
# sending ARP request
# def scan(ip):
#     arp_request = scapy.ARP()
#     arp_request.pdst=ip
#     print(arp_request.summary())
#
# scan("10.0.0.1/24")

# setting destination mac to broadcast mac
# def scan(ip):
#     arp_request = scapy.ARP(pdst=ip)
#     arp_request.show()
#     broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
#     broadcast.show()
#     arp_request_broadcast = broadcast/arp_request
#     arp_request_broadcast.show()
#
# scan("10.0.0.1/24")

# sending the packet into the network, automatically goes to broadcast MAC
# def scan(ip):
#     arp_request = scapy.ARP(pdst=ip)
#     broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
#     arp_request_broadcast = broadcast/arp_request
#     answered, unanswered = scapy.srp(arp_request_broadcast, timeout = 1)
#     print(answered.summary())
#
# scan("10.0.0.1/24")

# Paring the responses
# def scan(ip):
#     arp_request = scapy.ARP(pdst=ip)
#     broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
#     arp_request_broadcast = broadcast/arp_request
#     answered_list = scapy.srp(arp_request_broadcast, timeout = 1) [(0)]
#
#     for element in answered_list:
#         print(element[1].psrc)
#         print(element[1].hwsrc)
#         print("===================================")
#
#
# scan("10.0.0.1/24")
#

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    print(" IP\t\t\t\t\tMAC Address")
    print("===================================")

    for element in answered_list:
        print(element[1].psrc + "\t\t" + element[1].hwsrc)
        print("===================================")


scan("192.168.133.2/24")
