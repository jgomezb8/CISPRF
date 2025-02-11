import argparse
import socket
import threading

if __name__ == '__main__':
    # Initialize the argument parser with a usage message
    parser = argparse.ArgumentParser(
        usage='port_scan.py TARGET_HOST -p TARGET_PORTS\nexample: python3 port_scan.py scanme.nmap.org -p 21,80')
    # Add an argument for specifying the target host (IP address or domain name)
    parser.add_argument('tgt_host', type=str, metavar='TARGET_HOST',
                        help='specify target host (IP address or domain name)')
    # Add an argument for specifying target ports, separated by commas
    parser.add_argument('-p', required=True, type=str, metavar='TARGET_PORTS',
                        help='specify target port[s] separated by comma (no spaces)')
    # Parse the command-line arguments
    args = parser.parse_args()

    # Split the ports by commas and convert them to a list
    args.tgt_ports = str(args.p).split(',')

    # Print the entered host
    print("The host that you have entered is: " + args.tgt_host)

    # Print the ports to be scanned
    print("The port is to be scanned is: " + str(args.tgt_ports))

    # The line below seems to be intended to call the port_scan function with the provided arguments
    # port_scan(args.tgt_host, args.tgt_ports)
