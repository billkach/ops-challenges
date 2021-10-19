#!/usr/bin/env python3

# Script Name                           401ops11.py
# Author                                Bill Kachersky
# Date of last revision                 10/19/2021
# Description of purpose                TCP Port Range Scanner

# All content cited from https://thepacketgeek.com/scapy/building-network-tools/part-10/
# Script must be run as sudo in linux, Admin in Windows.

# Imports
import random
from scapy.all import ICMP, IP, sr1, sr, TCP

# Variables
host = input("Enter IP Address to scan: ")
port_range = [22, 23, 80, 443, 3389]

def tcpscan():
    # Send SYN with random Src Port for each Dst port
    for dst_port in port_range:
        src_port = random.randint(1025,65534)
        resp = sr1(
            IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="S"),
            timeout=1,
            verbose=0)
    # port filtered response for no flag received
    if resp is None:
        print(f"{host}:{dst_port} is filtered (silently dropped).")

    elif(resp.haslayer(TCP)):
        # port open notification for 0x12
        if(resp.getlayer(TCP).flags == 0x12):
            # Send a gratuitous RST to close the connection
            send_rst = sr(
                IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags='R'),
                timeout=1,
                verbose=0,
            )
            print(f"{host}:{dst_port} is open.")

        # port closed notification for 0x14
        elif (resp.getlayer(TCP).flags == 0x14):
            print(f"{host}:{dst_port} is closed.")

    elif(resp.haslayer(ICMP)):
        # port filtered response for no flag received
        if(
            int(resp.getlayer(ICMP).type) == 3 and
            int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]
        ):
            print(f"{host}:{dst_port} is filtered (silently dropped).")



# Main

tcpscan()

# End