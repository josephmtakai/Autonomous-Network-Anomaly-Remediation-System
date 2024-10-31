from scapy.all import send, Raw
from scapy.layers.inet import IP

def generate_high_traffic(src_ip, dest_ip, packet_size=1500, count=1000):
    for _ in range(count):
        send(IP(src=src_ip, dst=dest_ip)/Raw(b"X"*packet_size), verbose=0)
        
# Usage
generate_high_traffic("192.168.1.10", "192.168.1.100")
