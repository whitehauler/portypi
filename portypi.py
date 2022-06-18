from sys import argv,exit
import socket

def usage():
	print("# PORTYPI")
	print("USAGE : Require exactly 1 argument.")
	exit(1)

if len(argv) != 2:
	usage()
	
# Ports to scan
ports = [ i for i in range(1000) ]

# Open Ports
ports_open = []
host_ip = argv[1]


print("# Open Ports")

for port in ports:
	try:
		conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		conn.settimeout(10)
		conn.connect((host_ip, port))
		
	except ConnectionRefusedError:
		continue
	except socket.error:
		continue
	except socket.gaierror as err:
		print("Error Resolving Host: {} ".format(err))
		exit(2)
		conn.close()
		# ports_open.append(port)
	print(port)
