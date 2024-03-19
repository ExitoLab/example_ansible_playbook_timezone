#!/usr/bin/env python3

import re
import json
import os

# Get the current directory
current_directory = os.getcwd()

# Concatenate the current directory with the file name
log_file = os.path.join(current_directory, 'log.txt')

def read_log_file(log_file):
    """Reads the log file and extracts the IP addresses associated with ctlplane."""
    ctlplane_ips = []
    with open(log_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if 'ctlplane=' in line:
                match = re.search(r'ctlplane=([\d\.]+)', line)
                if match:
                    ctlplane_ips.append(match.group(1))
    return ctlplane_ips

def generate_inventory(ctlplane_ips):
    """Generates the inventory in JSON format."""
    inventory = {
        '_meta': {
            'hostvars': {}
        },
        'all': {
            'hosts': ctlplane_ips
        }
    }
    return inventory

def main():
    """Main function."""
    ctlplane_ips = read_log_file(log_file)
    inventory = generate_inventory(ctlplane_ips)
    print(json.dumps(inventory))

if __name__ == '__main__':
    main()
