import dpkt
import socket

f = open('ftp.pcap', 'rb')
pcap = dpkt.pcap.Reader(f)

i = 1
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

    if tcp.dport == 21 or tcp.sport == 21:
        print(i)
        i+=1
        print(f"Protocol: FTP, Timestamp: {timestamp}, Dest IP: {socket.inet_ntoa(ip.dst)}")
        ftp_data = tcp.data.decode('utf-8')
        print(ftp_data)
