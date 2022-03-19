from sys import argv, exit
import socket

try:
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.settimeout(2.0)
except socket.error as err:
    print("Error Creating socket")

# Ports to scan
ports = [ i for i in range(100) ]

# Open Ports

ports_open = []


try: 
    host_ip = argv[1]
except socket.gaierror:
    print("Error Resolving Host")
    sys.exit()

for port in ports:
    try:
        print("Trying " + str(port))

        if conn.connect((host_ip, port)):
            ports_open.append(port)
            socket.close()
    except Exception as os_err:
        print("Try Bind to Gateway IP \n" + str(os_err) )

print(ports_open)