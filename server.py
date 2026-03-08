import socket
import threading

# Global variable to store the client address
client_addr = None

def receive_messages(sock):
    """Continuously receive messages from the client."""
    global client_addr
    while True:
        try:
            data, addr = sock.recvfrom(1024)
            client_addr = addr
            print(f"\nClient ({addr[0]}:{addr[1]}): {data.decode()}")
            print("Server: ", end="", flush=True)
        except Exception as e:
            print("\n[ERROR receiving]:", e)
            break

def main():
    # Get the server's local IPv4 address
    server_ip = socket.gethostbyname(socket.gethostname())
    server_port = 12345

    print(f"\n[SERVER STARTED]")
    print(f"IP Address: {server_ip}")
    print(f"Port: {server_port}")

    # Create UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((server_ip, server_port))

    # Start receiver thread
    threading.Thread(target=receive_messages, args=(sock,), daemon=True).start()

    print("\n[READY] Waiting for client messages...")
    print("Type your message and press Enter to send.")
    print("Type 'exit' to quit.\n")

    # Sending loop
    while True:
        msg = input("Server: ")
        if msg.lower() == "exit":
            print("Server shutting down.")
            break
        if client_addr:
            sock.sendto(msg.encode(), client_addr)
        else:
            print("No client connected yet! Waiting for message...")

if __name__ == "__main__":
    main()
