
import netfilterqueue
import scapy.all as scapy
import subprocess

#remote system
#subprocess.call("iptables -I FORWARD -j NFQUEUE --queue-num 0")

#local system (vms)
#subprocess.call("iptables -I OUTPUT -j NFQUEUE --queue-num 0")
#subprocess.call("iptables -I INPUT -j NFQUEUE --queue-num 0")
# iptables -D [command entered] to undo

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    print(scapy_packet.show())
    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()

