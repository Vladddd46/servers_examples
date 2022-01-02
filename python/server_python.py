import socket

listening_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

listening_socket.bind(("192.168.0.111", 5000))
listening_socket.listen()

while True:
	socket_for_communication, addr = listening_socket.accept()
	print("Connected by ", addr)
	data = socket_for_communication.recv(1024)
	if data:
		print("received data from client: ", data)
		socket_for_communication.sendall(bytes(reversed(data)))
	else:
		print("Error, while receiving data from socket.")
	socket_for_communication.close()
listening_socket.close()