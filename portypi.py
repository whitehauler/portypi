import socket

try:
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print("Error Creating socket")


port = [ lambda: i for i in range(1001) ]

print(i)