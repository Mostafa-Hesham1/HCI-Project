import socket
import requests
from flask_socketio import SocketIO

socketio = SocketIO()

soc = socket.socket()
hostname = "localhost"  # 127.0.0.1
port = 65434
soc.bind((hostname, port))
soc.listen(5)
conn, addr = soc.accept()
print("Device connected:", addr)

try:
    while True:
        data = conn.recv(1024)  # Receiving data
        if not data:
            break

        # Decode the received data
        received_message = data.decode('utf-8')
        print(f"Received SymbolID: {received_message}")

        # Send the received message to Flask server via an HTTP POST request
        requests.post('http://localhost:5000/tuio_event', json={'message': received_message})

        if received_message == "exit":
            break
except ConnectionResetError:
    print("Connection closed by the remote host")
finally:
    conn.close()