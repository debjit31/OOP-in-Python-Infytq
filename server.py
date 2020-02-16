import socket

##msg = "Welcome to the Server!"
##print(f'{len(msg):<10}'+msg)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
	clientsocket,address = s.accept()
	print(f"Connection from {address} has been established!")
	clientsocket.send(bytes("welcome to the Server!", "utf-8"))
	clientsocket.close()


