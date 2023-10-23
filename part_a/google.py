import dpkt
import socket

# Open the pcap file
f = open('google.pcap', 'rb')
pcap = dpkt.pcap.Reader(f)
GOOGLE_IP = "172.217.12.110"

for timestamp, data in pcap:
    eth = dpkt.ethernet.Ethernet(data)
    if not isinstance(eth.data, dpkt.ip.IP):
        continue
    ip = eth.data
    if not isinstance(ip.data, dpkt.icmp.ICMP):
        continue
    if socket.inet_ntoa(ip.src) == GOOGLE_IP or socket.inet_ntoa(ip.dst) == GOOGLE_IP:
        print(f"Protocol: ICMP, Timestamp: {timestamp}, Dest IP Address: {socket.inet_ntoa(ip.dst)}")

# Close the pcap file
f.close()
