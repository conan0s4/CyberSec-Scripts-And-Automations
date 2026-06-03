import argparse
from scapy.all import rdpcap
from scapy.layers.inet import ICMP
from scapy.packet import Raw

parser = argparse.ArgumentParser()
parser.add_argument(
    "-f",
    "--file",
    required=True,
    help="pcap or pcapng file"
)
args = parser.parse_args()
packets = rdpcap(args.file)
print(f"[*] Loaded {len(packets)} packets")
for packet in packets:
    if packet.haslayer(ICMP):
        packet.show()
for packet in packets:
    if packet.haslayer(ICMP):
        if packet.haslayer(Raw):
            raw_data = packet[Raw].load
            print(raw_data)


