import socket
import time

HOST = '127.0.0.1'
PORT = 5500
PACKET_SIZE = 1024
NUM_PACKETS = 100
i = 0

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
    server_socket.bind((HOST, PORT))
    start_time = None
    end_time = None
    data_size = 0
    while True:
        data, addr = server_socket.recvfrom(PACKET_SIZE)
        if i == 0:
            start_time = time.time()
        elif i == NUM_PACKETS - 1:
            end_time = time.time()
            throughput = (data_size / (end_time - start_time) * 0.001)
            server_socket.sendto(bytes(f"{str(throughput)} Kbps", 'utf-8'), addr)
            i = 0
            data_size = 0
            continue
        data_size += len(data)
        i += 1


