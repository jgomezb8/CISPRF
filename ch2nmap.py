# Import the necessary libraries
import nmap
import argparse

def nmap_scan(tgt_host, tgt_ports):
    # Initialize the nmap port scanner
    nm_scan = nmap.PortScanner()
    # Iterate over each target port
    for tgt_port in tgt_ports:
        # Scan the specified port on the target host
        nm_scan.scan(tgt_host, tgt_port)
        # Retrieve the state of the port (open, closed, filtered)
        state = nm_scan[tgt_host]['tcp'][int(tgt_port)]['state']
        # Print the state of the port
        print(f'[*] {tgt_host} tcp/{tgt_port} {state}')

if __name__ == '__main__':
    # Initialize the argument parser with a usage message
    parser = argparse.ArgumentParser(
        usage='nmap_scan.py TARGET_HOST -p TARGET_PORTS')
    # Add an argument for specifying the target host's IP address
    parser.add_argument('host', type=str, metavar='TARGET_HOST',
                        help="specify target host's IP number")
    # Add an argument for specifying target ports, separated by commas
    parser.add_argument('-p', type=str, metavar='TARGET_PORTS',
                        help='specify target port[s] separated by comma '
                             '(no spaces)')
    # Parse the command-line arguments
    args = parser.parse_args()
    
    # Split the ports by commas and convert them to a list
    args.ports = str(args.p).split(',')
    # Call the nmap_scan function with the parsed host and ports
    nmap_scan(args.host, args.ports)
