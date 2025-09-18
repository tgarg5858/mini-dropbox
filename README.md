# 🗂️ Mini Dropbox

A simple **client-server file sharing system** built with Python sockets.
This project allows you to **upload** and **download** files between a client and server, mimicking basic Dropbox functionality.

---

## 🚀 Features

* Upload files from client to server
* Download files from server to client
* Stores uploaded files inside a `server_files/` directory
* Simple text-based menu for client interaction
* Works on localhost (can be extended for LAN/WAN)

---

## 📂 Project Structure

```
mini-dropbox/
│── server.py       # Server script
│── client.py       # Client script
│── server_files/   # Auto-created folder to store uploaded files
│── README.md       # Documentation
```

---

## ⚙️ Requirements

* Python **3.7+**

No external libraries required (only built-in Python modules: `socket`, `os`).

---

## 🖥️ Usage

### 1️⃣ Start the Server

Run the following command in one terminal:

```bash
python server.py
```

You should see:

```
Server running on 127.0.0.1:5000
```

---

### 2️⃣ Start the Client

Run the following command in another terminal:

```bash
python client.py
```

---

### 3️⃣ Client Menu

You’ll get a simple menu:

```
1. Upload File
2. Download File
3. Exit
```

#### Upload a File

* Enter `1`, then type the filename (must exist in client directory).
* The file will be uploaded to the server inside `server_files/`.

#### Download a File

* Enter `2`, then type the filename (must exist in `server_files/`).
* The file will be saved in client directory as `downloaded_<filename>`.

#### Exit

* Enter `3` to quit the client.

---

## 🔒 Notes

* Default host: `127.0.0.1` (localhost)
* Default port: `5000`
* Change `HOST` and `PORT` in both `server.py` and `client.py` for different setups.
* Server must be running before client connects.

---

## 🛠️ Future Improvements

* Add authentication (username/password)
* Support multiple clients simultaneously
* Add file listing feature
* Implement file delete/rename operations
