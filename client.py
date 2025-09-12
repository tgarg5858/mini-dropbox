import socket
import os

HOST = '127.0.0.1'
PORT = 5000

def upload(filename):
    if not os.path.exists(filename):
        print("File does not exist!")
        return
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"UPLOAD")
        s.sendall(filename.encode())
        with open(filename, "rb") as f:
            while chunk := f.read(1024):
                s.sendall(chunk)
        s.sendall(b"DONE")
    print("Upload complete!")

def download(filename):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"DOWNLOAD")
        s.sendall(filename.encode())

        with open("downloaded_" + filename, "wb") as f:
            while True:
                data = s.recv(1024)
                if data == b"DONE":
                    break
                f.write(data)
    print("Download complete!")

# Simple menu
while True:
    print("\n1. Upload File\n2. Download File\n3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        fname = input("Enter filename to upload: ")
        upload(fname)
    elif choice == "2":
        fname = input("Enter filename to download: ")
        download(fname)
    else:
        break
