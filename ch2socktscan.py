# Import the necessary socket library
import socket
from socket import *

# Define the target host and a list of ports to be scanned
lport = [22, 80, 23, 443]
tfhost = "127.0.1.1"

# Loop through each port in the list
for nport in lport:
    try:
        # Create a socket object for the connection
        connskt = socket(AF_INET, SOCK_STREAM)
        # Attempt to connect to the target host and port
        connskt.connect((tfhost, int(nport)))
        # Send a string to the target host to check its response
        connskt.send(b'127.0.0.1\r\n')
        # Receive up to 1,000,000 bytes of data from the target host
        result = connskt.recv(1000000)
        # Print the response received from the target host
        print('[+] ' + str(result))
    except:
        # Print a message if the port is closed
        print("port " + str(nport) + " is closed")
    finally:
        # Close the socket connection
        connskt.close()
