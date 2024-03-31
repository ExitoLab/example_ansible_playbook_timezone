#!/usr/bin/env python3

import re
import json
import os

# Get the current directory
current_directory = os.getcwd()

# Concatenate the current directory with the file name
server_file = os.path.join(current_directory, 'servers.txt')

def read_servers_file(server_file):
    """Reads the server file and extracts the IP addresses."""
    ips = []
    with open(server_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if 'ip_address=' in line:
                match = re.search(r'ip_address=([\d\.]+)', line)
                if match:
                    ips.append(match.group(1))
    return ips

def generate_inventory(ips):
    """Generates the inventory in JSON format."""
    inventory = {
        '_meta': {
            'hostvars': {}
        },
        'all': {
            'hosts': ips
        }
    }
    return inventory

def main():
    """Main function."""
    ips = read_servers_file(server_file)
    inventory = generate_inventory(ips)
    print(json.dumps(inventory))

if __name__ == '__main__':
    main()