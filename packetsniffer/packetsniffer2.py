#!/usr/bin/env python

import scapy.all as scapy
from scapy.all import http


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)


def process_sniffed_packet(packet): #checks for http data and prints it
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            print(packet[scapy.Raw].load) #scapy.show displays layer information


sniff("eth0")