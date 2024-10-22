import socket

soc = socket.socket()
hostname = "localhost"  # 127.0.0.1
port = 65434
soc.bind((hostname, port))
soc.listen(5)
conn, addr = soc.accept()
print("Device connected:", addr)

while True:
    data = conn.recv(1024)  # Receiving data
    if not data:
        break

    # Decode the received data
    received_message = data.decode('utf-8')
    print(f"Received SymbolID: {received_message}")

    if received_message == "exit":
        break

conn.close()
