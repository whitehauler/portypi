from sys import argv, exit
import socket

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
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.settimeout(1320)
        print("Port " + str(port))
        if conn.connect((host_ip, port)):
            print(port)
            ports_open.append(port)
    except socket.error as err:
        print("Error Creating socket")
    except ConnectionRefusedError:
        continue
    conn.close()

print(ports_open)
