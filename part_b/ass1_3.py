import dpkt


f = open('ass1_3.pcap', 'rb')
pcap = dpkt.pcap.Reader(f)

i = 1
for timestamp, data in pcap:
    eth = dpkt.ethernet.Ethernet(data)
    if not isinstance(eth.data, dpkt.ip.IP):
        continue
    ip = eth.data
    if isinstance(ip.data, dpkt.icmp.ICMP):
        icmp_packet = ip.data
        print(f"ICMP Packet {i}:")
        print(f"Type: {icmp_packet.type}")
        print(f"Code: {icmp_packet.code}")
        print(f"Checksum: {icmp_packet.sum}")
        print(f"Data: {icmp_packet.data}")
        print(f"Echo: {repr(icmp_packet.data.data)}")
        print('\n')
        i += 1
