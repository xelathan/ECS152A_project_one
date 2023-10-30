import dpkt
from dpkt.http import Request
import json
from datetime import datetime
import urllib.parse


# Function to extract and print HTTP request content from IPv6 traffic
def extract_ipv6_http_requests(file_path):
    with open(file_path, 'rb') as pcap_file:
        pcap = dpkt.pcap.Reader(pcap_file)
        for timestamp, packet in pcap:
            eth = dpkt.ethernet.Ethernet(packet)

            if eth.type == dpkt.ethernet.ETH_TYPE_IP6:
                ipv6 = eth.data

                if isinstance(ipv6.data, dpkt.tcp.TCP):
                    tcp = ipv6.data

                    # Check if it's an HTTP packet (port 80 or 8080)
                    if tcp.dport in (80, 8080) or tcp.sport in (80, 8080):
                        try:
                            http_request = Request(tcp.data)
                            ts = datetime.utcfromtimestamp(timestamp)
                            print(f'Timestamp: {ts}')
                            print(f'HTTP Request:\n{http_request}')

                            # Check for the "secret" field in different areas of the request

                            # Case 1: In the query parameters
                            query_params = urllib.parse.urlparse(http_request.uri).query
                            query_dict = urllib.parse.parse_qs(query_params)
                            if 'secret' in query_dict:
                                secret_value = query_dict['secret'][0]
                                print(f'Secret (from query parameter): {secret_value}\n')

                            # Case 2: In the headers
                            if 'secret' in http_request.headers:
                                secret_value = http_request.headers['secret']
                                print(f'Secret (from header): {secret_value}\n')

                            # Case 3: In the JSON data
                            if 'content-type' in http_request.headers and \
                                    'application/json' in http_request.headers['content-type'].lower():
                                try:
                                    json_data = http_request.body
                                    json_obj = json.loads(json_data)
                                    if 'secret' in json_obj:
                                        secret_value = json_obj['secret']
                                        print(f'Secret (from JSON data): {secret_value}\n')
                                except (json.JSONDecodeError, ValueError) as e:
                                    print(f'Error parsing JSON: {e}')

                        except dpkt.dpkt.UnpackError:
                            # Handle any unpacking errors
                            pass


# Replace 'your_pcap_file.pcap' with the path to your PCAP file
file_path = 'ass1_1.pcap'
extract_ipv6_http_requests(file_path)
