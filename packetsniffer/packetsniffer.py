#!/usr/bin/env python

import scapy.all as scapy
from scapy.all import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet, filter="http")


def process_sniffed_packet(packet):
    print(packet)


sniff("eth0")






