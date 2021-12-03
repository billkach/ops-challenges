#!/usr/bin/python3

# Script Name                           401ops42.py
# Author                                Bill Kachersky
# Date of last revision                 12/02/2021
# Description of purpose                Attack Tools Part 2 of 3 (Python NMAP Tool)


# Resources and Thanks
# https://github.com/codefellows/seattle-cyber-401d3/blob/main/class-42/challenges/DEMO.md
# https://www.pythonpool.com/python-nmap/


import nmap

scanner = nmap.PortScanner()

print("Nmap Automation Tool")
print("--------------------")

ip_addr = input("IP address to scan: ")
print("The IP you entered is: ", ip_addr)

resp = input("""\nSelect scan to execute:
                1) SYN ACK Scan
                2) UDP Scan
                3) OS Scan             \n""") ### TODO: Select what your third scan type will be
print("You have selected option: ", resp)




if resp == '1':
    # Prompt the user to type in a port range for this tool to scan
    range = input("Please specify a port range to scan; ex: 1-50: ")
    print("You have selected port(s): ", range)
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, range, '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())

elif resp == '2':
    # Prompt the user to type in a port range for this tool to scan
    range = input("Please specify a port range to scan; ex: 1-50: ")
    print("You have selected port(s): ", range)
    # Here, v is used for verbose, which means if selected it will give #extra information
    #-sU means perform a UDP SYN connect scan, it send the SYN packets to #the host
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, range, '-v -sU')
    print(scanner.scaninfo())
    # state() tells if target is up or down
    print("Ip Status: ", scanner[ip_addr].state())
    # all_protocols() tells which protocols are enabled like TCP UDP etc
    print("protocols:",scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())

elif resp == '3':
#     scanner.scan(hosts='192.168.1.0/24', arguments='-n -sP -PE -PA21,23,80,3389')
#     hosts_list = [(x, scanner[x]['status']['state']) for x in scanner.all_hosts()]
#     for host, status in hosts_list:
#         print('{0}:{1}'.format(host, status))
    print(scanner.scan(ip_addr, arguments="-O")['scan'][ip_addr]['osmatch'][1])
else:
    print("Please enter a valid option")