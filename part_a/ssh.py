import dpkt
import socket


f = open('ssh.pcap', 'rb')
pcap = dpkt.pcap.Reader(f)

for timestamp, data in pcap:
    eth = dpkt.ethernet.Ethernet(data)

    if not isinstance(eth.data, dpkt.ip.IP):
        continue

    ip = eth.data

    if not isinstance(ip.data, dpkt.tcp.TCP):
        continue

    tcp = ip.data

    if not len(tcp.data) > 0:
        continue

    if tcp.dport == 22 or tcp.sport == 22:
        print(f"Data: {tcp.data}, Timestamp: {timestamp}, Dest IP Address: {socket.inet_ntoa(ip.dst)}")

# Close the pcap file
f.close()


