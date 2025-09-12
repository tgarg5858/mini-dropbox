import socket
import os

HOST = '127.0.0.1'   # localhost
PORT = 5000          # choose any free port
SERVER_FOLDER = "server_files"

# Make sure folder exists
if not os.path.exists(SERVER_FOLDER):
    os.makedirs(SERVER_FOLDER)

# Start TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
print(f"Server running on {HOST}:{PORT}")

while True:
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    # Receive command
    command = conn.recv(1024).decode()

    if command == "UPLOAD":
        filename = conn.recv(1024).decode()
        filepath = os.path.join(SERVER_FOLDER, filename)

        with open(filepath, "wb") as f:
            while True:
                data = conn.recv(1024)
                if data == b"DONE":
                    break
                f.write(data)
        print(f"File {filename} uploaded successfully.")

    elif command == "DOWNLOAD":
        filename = conn.recv(1024).decode()
        filepath = os.path.join(SERVER_FOLDER, filename)

        if os.path.exists(filepath):
            with open(filepath, "rb") as f:
                while chunk := f.read(1024):
                    conn.sendall(chunk)
        conn.sendall(b"DONE")
        print(f"File {filename} sent to client.")

    conn.close()
