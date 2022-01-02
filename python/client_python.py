import socket

while True:
	send_data = input("Enter: ")
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client_socket.connect(("192.168.0.111", 5000))

	client_socket.sendall(bytes(send_data, "utf-8"))
	data = client_socket.recv(1024)

	print("Received: ", repr(data))

client_socket.close()