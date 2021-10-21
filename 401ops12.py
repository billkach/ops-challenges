#!/usr/bin/env python3

# Script Name                           401ops11.py
# Author                                Bill Kachersky
# Date of last revision                 10/19/2021
# Description of purpose                TCP Port Range Scanner

# All content cited from https://thepacketgeek.com/scapy/building-network-tools/part-10/
# Script must be run as sudo in linux, Admin in Windows.

# Imports
import random
from scapy.all import ICMP, IP, sr1, sr, TCP, sys
from ipaddress import IPv4Network

# Variables
menu = ("TCP Port Range Scanner",
        "ICMP Ping Sweeper",
        "Exit")




def display_menu():
    # this function will generate a menu for our user to interact with
    # it will take user input and validate it as an available option
    # then call the associated function or return to menu selection if 
    # user choice is invalid.
    for opt in range(0,len(menu)):
        print(str(opt+1)+". "+menu[opt])

    user_choice = input("Please input the number of the option you'd like: ")
    

    if user_choice == (len(menu)):
        sys.exit()

    elif user_choice == "1":
        tcpscan()

    elif user_choice == "2":
        ping_sweep()
        
    else:
        input("Wrong choice, hit any key to start over.")
        display_menu()





def tcpscan():
    host = input("Enter IP Address to scan: ")
    port_range = [22, 23, 80, 443, 3389]
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



def ping_sweep():
    # this function will get a CIDR block address from the user
    # we'll use the ipaddress.ip_network function to extrapolate individual host IDs from the CIDR block
    # then we'll ping each host and respond based on the challenge requirements.
    # then we'll count how many hosts are online and use an incrementing variable to do so.

    # User Input for IPv4 CIDR block
    network = input("Please enter the CIDR block for the IPv4 network you'd like to scan: ")

    # Variables for making a list of addresses out of our chosen network, and setting a live host counter
    addresses = IPv4Network(network)
    live_count = 0

    # Send ICMP ping request, wait for reply
    for host in addresses:
        if (host in (addresses.network_address, addresses.broadcast_address)):
            # Skip these two addresses
            continue

        resp = sr1(
            IP(dst=str(host))/ICMP(),
            timeout=1,
            verbose=0,
        )

        if resp is None:
            print(f"{host} is down or not responding.")
        elif (
            int(resp.getlayer(ICMP).type)==3 and
            int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]
        ):
            print(f"{host} is blocking ICMP traffic")
        else:
            print(f"{host} is responding.")
            #tcpscan(str(host))
            live_count += 1

    print (f"{live_count}/{addresses.num_addresses} hosts are online.")


# Main

display_menu()

# End