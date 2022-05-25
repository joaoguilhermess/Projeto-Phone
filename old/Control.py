import socket

server = socket.socket()

server.bind(("0.0.0.0", 5000))
print("Listening...")

server.listen(1)

client, address = server.accept()

print("Connected: " + str(address))

while True:
	receive = client.recv(1024).decode("utf8")
	receive = receive.split("#")[0]
	receive = receive.split(":")
	print(" ".join(receive))
	Ax = receive[0]
	Ay = receive[1]
	Az = receive[2]
	Gx = receive[3]
	Gy = receive[4]
	Gz = receive[5]

	