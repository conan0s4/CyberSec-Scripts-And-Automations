from scapy.all import rdpcap
from scapy.layers.dns import DNS, DNSQR
from scapy.layers.inet import IP
packets = rdpcap('silent_broadcast.pcap')

dns_packets = [pkt for pkt in packets if pkt.haslayer(DNS)]

addr = input("filter ip_dst: ")
for pkt in dns_packets:
    if IP in pkt and pkt.haslayer(DNSQR):
        if pkt[IP].dst == addr:
            print(f"{pkt.time}: {pkt[DNSQR].qname}")

