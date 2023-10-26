import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5500
PACKET_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
    data = b'0' * PACKET_SIZE * 100
    packets = [data[i:i+PACKET_SIZE] for i in range(0, len(data), PACKET_SIZE)]
    for packet in packets:
        client_socket.sendto(packet, (SERVER_HOST, SERVER_PORT))
    data, addr = client_socket.recvfrom(PACKET_SIZE)
    print(data.decode('utf-8'))


client_socket.close()
