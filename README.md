# local_chat
Localchat project
# Local Chat Program

## Overview
This project implements a simple "local chat" application using a client-server model based on the UDP protocol. It allows two users on the same local network (e.g., same WiFi or Ethernet domain) to chat directly without relying on third-party services like Skype or Discord. The server starts first, prints its IP address and port, and waits for the client to connect. Once connected, both can send and receive messages continuously, even sending multiple messages without waiting for replies.

This fulfills the requirements for COSC 331 Project 1, due November 7, 2025. The implementation is in Python using the `socket` and `threading` modules for non-blocking, bidirectional communication.

## Features
- **Server**: Binds to a UDP socket, prints IP and port, and handles incoming/outgoing messages via threads.
- **Client**: Connects to the server's IP and port, sends an initial message, and enables continuous chat.
- **Continuous Communication**: Supports sending multiple messages from one side without replies (requirement #5).
- **Cross-Platform**: Works on Windows, Linux, or Android (with Python environment).
- **No Dependencies**: Uses only built-in Python libraries.

## Requirements
- Python 3.8 or higher.
- Two machines on the same local network for demonstration.
- No external libraries required.

## Setup
1. Clone or download the project files:
   - `server.py`
   - `client.py`
   - `README.md`

2. Ensure Python is installed on both machines.

## How to Run
### Step 1: Start the Server
On the first machine:

- Enter the server's IP and port when prompted.
- Send your first message (e.g., "Hello from client!").

### Step 3: Chat
- Both sides will prompt for input (e.g., "You (Server):" or "You (Client):").
- Type messages and press Enter to send.
- Messages from the other side appear in real-time.
- To exit: Type "quit" (or Ctrl+C).

## Example Usage
- Server receives client's first message and starts chatting.
- Send multiple messages from client: They all arrive on server without blocking.
- Works on localhost for testing (use IP `127.0.0.1`), but demonstrate on two machines.

## Grading Alignment
- Server prints IP/port: 20 points.
- Client creates UDP socket based on server info: 30 points.
- Continuous bidirectional chat: 50 points.
- Total: 100 points (extra 10 for solo implementation).

## Notes
- Port is hardcoded to 12345; change if needed (update in both files).
- Handle firewalls: Allow UDP traffic on the port.
- For Android: Use Termux with Python installed.
- Submission: ZIP the files and submit via Canvas. Include names if partnered.
- Demonstration: Notify instructor for lab access if using lab machines.
