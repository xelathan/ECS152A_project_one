import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5500
PACKET_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
    data = b'0' * PACKET_SIZE * 100
    packets = [data[i:i+PACKET_SIZE] for i in range(0, len(data), PACKET_SIZE)]
    for packet in packets:
        client_socket.sendto(packet, (SERVER_HOST, SERVER_PORT))
    client_socket.sendto(b'', (SERVER_HOST, SERVER_PORT))  # Signal the end of the message

    # Receive the throughput from the server
    throughput, addr = client_socket.recvfrom(PACKET_SIZE)
    print(f"Received throughput from the server: {throughput.decode('utf-8')} kbps")

client_socket.close()
