import socket
import time


def calculate_throughput(data_size, total_bytes_received):
    elapsed_time = time.time() - start_time

    if elapsed_time > 0:
        throughput_kbps = total_bytes_received / elapsed_time * 0.001
        return throughput_kbps

def main():
    host = '127.0.0.1'
    port = 5500
    data_size = 1024  # 1 kilobyte

    global server_socket, start_time
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    try:
        data, client_address = server_socket.recvfrom(data_size)  # Receive the first packet

        start_time = time.time()
        total_bytes_received = len(data)

        message = [data]
        while True:
            data, client_address = server_socket.recvfrom(data_size)
            if not data:
                break
            message.append(data)
            total_bytes_received += len(data)

        full_message = b"".join(message)
        throughput_kbps = calculate_throughput(data_size, total_bytes_received)

        # Send the throughput back to the client
        server_socket.sendto(str(throughput_kbps).encode(), client_address)

    except KeyboardInterrupt:
        print("Server terminated by the user.")


if __name__ == '__main__':
    main()
