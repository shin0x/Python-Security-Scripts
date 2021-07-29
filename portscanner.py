import socket
import subprocess
import sys
import getopt
from datetime import datetime

first_port = 1
last_port = 45000

opts, rest = getopt.getopt(sys.argv[1:], "t:l:f:")

for opt, arg in opts:
    if opt == '-t':
        target = arg
    if opt == '-l':
        last_port = int(arg)
    if opt == '-f':
        first_port = int(arg)

#target = "scanme.nmap.org"
targetIP = socket.gethostbyname(target)

tstart = datetime.now()
try:
    for i in range(first_port, last_port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        res = sock.connect_ex((targetIP, i))
        if res  == 0:
            print("Port " + str(i) + " is open!")
        sock.close()
except Exception:
    print("ERROR")
    sys.exit()
tend = datetime.now()
diff = tend - tstart

print("Scan completet in " + str(diff))