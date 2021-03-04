#!/usr/bin/env python

from scapy.all import*

pkt = scapy.packet(count=1)
type(pkt)
print (pkt[0].summary())


