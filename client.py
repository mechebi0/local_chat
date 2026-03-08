import socket
import threading

def receive_messages(sock):
    """Continuously receive messages from the server."""
    while True:
        try:
            data, _ = sock.recvfrom(1024)
            print(f"\nServer: {data.decode()}")
            print("You: ", end="", flush=True)
        except Exception as e:
            print("\n[ERROR receiving]:", e)
            break

def main():
    server_ip = input("Enter server IP address: ").strip()
    server_port = int(input("Enter server port: "))

    # Create UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Send initial connection message
    sock.sendto("Client connected.".encode(), (server_ip, server_port))
    print(f"\n[CONNECTED] to server at {server_ip}:{server_port}")
    print("Type your message and press Enter to send.")
    print("Type 'exit' to quit.\n")

    # Start thread for receiving messages
    threading.Thread(target=receive_messages, args=(sock,), daemon=True).start()

    # Sending loop
    while True:
        msg = input("You: ")
        if msg.lower() == "exit":
            print("Disconnected.")
            break
        sock.sendto(msg.encode(), (server_ip, server_port))

if __name__ == "__main__":
    main()
