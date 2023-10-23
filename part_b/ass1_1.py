import dpkt
import json

f = open('ass1_1.pcap', 'rb')
pcap = dpkt.pcap.Reader(f)

for timestamp, data in pcap:
    eth = dpkt.ethernet.Ethernet(data)

    if not isinstance(eth.data, dpkt.ip6.IP6):
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
            if '?' in http.uri:
                slash, query_string = http.uri.split('?', 1)
                print(query_string[7:])
            if 'secret' in http.headers:
                print(http.headers['secret'])
            if 'secret' in http.body.decode():
                print(json.loads(http.body.decode())['secret'])

        except Exception as e:
            print(e)