import argparse
import socket
import threading

def port_scan(tgt_host, tgt_ports):
    try:
        # Attempt to resolve the target host to an IP address
        tgt_ip = socket.gethostbyname(tgt_host)
    except socket.herror:
        # Print an error message if the host cannot be resolved
        print(f'[-] Cannot resolve {tgt_host}: Unknown host')
        return

    try:
        # Retrieve the host name associated with the IP address
        tgt_name = socket.gethostbyaddr(tgt_ip)
        print(f'\n[+] Scan Results for: {tgt_name[0]}')
    except socket.herror:
        # Print the IP address if the host name cannot be retrieved
        print(f'\n[+] Scan Results for: {tgt_ip}')

    # Set the default timeout for sockets
    socket.setdefaulttimeout(1)

# Define the target host and ports
tgt_host = "www.cc.edu"
tgt_ports = 80
# Call the port_scan function with the target host and ports
port_scan(tgt_host, tgt_ports)
