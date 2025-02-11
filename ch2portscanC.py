import argparse
import socket
import threading

def conn_scan(tgt_host, tgt_port):
    # Initialize a semaphore for controlling access to the screen for printing results
    screen_lock = threading.Semaphore()
    # Create a socket object for the connection
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn_skt:
        try:
            # Attempt to connect to the target host and port
            conn_skt.connect((tgt_host, tgt_port))
            # Send a string to the target host
            conn_skt.send(b'ViolentPython\r\n')
            # Receive up to 100 bytes of data from the target host
            results = conn_skt.recv(100).decode('utf-8')
            # Acquire the screen lock before printing
            screen_lock.acquire()
            # Print that the port is open
            print(f'[+] {tgt_port}/tcp open')
            # Print the results received from the host
            print(f'[>] {results}')
        except OSError:
            # Acquire the screen lock before printing
            screen_lock.acquire()
            # Print that the port is closed
            print(f'[-] {tgt_port}/tcp closed')
        finally:
            # Release the screen lock after printing
            screen_lock.release()

# Define the target host and a list of ports to scan
tgt_host = '127.0.1.1'
tgt_ports = [80, 22, 23, 25]

# Iterate over each port in the list
for ports in tgt_ports:
    # Create a new thread for each port and start the connection scan
    t = threading.Thread(target=conn_scan, args=(tgt_host, int(ports)))
    t.start()
