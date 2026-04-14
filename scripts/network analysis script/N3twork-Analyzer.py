from scapy.all import rdpcap
from scapy.layers.dns import DNS, DNSQR
from scapy.layers.inet import IP

def ip_idnt(pcap):
    packets = rdpcap(pcap)
    ip_inspect = [pkt for pkt in packets if pkt.haslayer(IP)]
    addsrc = []
    addDst = []
    for pkt in ip_inspect:
        if pkt[IP].src not in addsrc:
            addsrc.append(pkt[IP].src)
    for pkt in ip_inspect:
        if pkt[IP].dst not in addDst:
            addDst.append(pkt[IP].dst)
    return f"src:{addsrc}  dst:{addDst}"

def ext(pcap, addr):
    packets = rdpcap(pcap)
    dns_packets = [pkt for pkt in packets if pkt.haslayer(DNS)]
    out = []
    for pkt in dns_packets:
        if IP in pkt and pkt.haslayer(DNSQR):
            if pkt[IP].dst == addr:
                out.append(f"{pkt.time}: {pkt[DNSQR].qname}")
    return out
if __name__ == "__main__":

    pcap = input("pcap_file:")
    filter = input("filter_ip[y/n]:")
    if filter == "y":
        addr = input("addr:")
        print(ext(pcap,addr))
    elif filter == "n":
        print(ip_idnt(pcap))
