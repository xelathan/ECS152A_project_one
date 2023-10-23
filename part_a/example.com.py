import dpkt
import socket

f = open('example.pcap', 'rb')
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

    if tcp.dport == 80:
        try:
            http = dpkt.http.Request(tcp.data)
            print(f"Data: {http.headers}, Timestamp: {timestamp}, Dest IP Address: {socket.inet_ntoa(ip.dst)}")
        except:
            print("Malformed HTTP Request packet")
    elif tcp.sport == 80:
        try:
            http = dpkt.http.Response(tcp.data)
            print(f"Data: {http.headers}, Timestamp: {timestamp}, Dest IP Address: {socket.inet_ntoa(ip.dst)}")
        except:
            print("Malformed HTTP Response packet")

# Close the pcap file
f.close()


