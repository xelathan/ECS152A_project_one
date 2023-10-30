import dpkt

def process_icmp_packet(ts, eth_data):
    eth = dpkt.ethernet.Ethernet(eth_data)
    if isinstance(eth.data, dpkt.ip.IP):
        ip = eth.data
        if isinstance(ip.data, dpkt.icmp.ICMP):
            icmp = ip.data
            icmp_type = icmp.type
            icmp_code = icmp.code
            icmp_data = icmp.data
            print(f"Timestamp: {ts}")
            print(f"ICMP Type: {icmp_type}")
            print(f"ICMP Code: {icmp_code}")
            print(f"ICMP Data: {icmp_data}")
            print(f"Echo: {repr(icmp_data.data)}")
            print()

def process_pcap_file(file_path):
    with open(file_path, 'rb') as pcap_file:
        pcap = dpkt.pcap.Reader(pcap_file)
        for ts, pkt in pcap:
            process_icmp_packet(ts, pkt)

if __name__ == "__main__":
    pcap_file_path = "ass1_2.pcap"  # Change to your pcap file path
    process_pcap_file(pcap_file_path)
