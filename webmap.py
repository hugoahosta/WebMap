#!/usr/bin/python3

import os
import sys

ans=True
while ans:
    print
    print('====================================')
    print('#            WEBMAP v1            #')
    print('====================================')
    print("1. Nmap Scan")
    print("2. Dirsearcher Scan")
    print("3. Nikto Scan")
    print("A. All the Scans")
    print("G. Get The Tools")
    print("E. Exit")
    print('====================================')
    ans=input("What would you like to do? Enter your selection: ")
    if ans=="1":
      os.system('cls' if os.name == 'nt' else 'clear')

    ans=True
    while ans:
        print
        print('====================================')
        print('#            Network Time          #')
        print('====================================')
        print("1. Scan An IP Address For Open Ports")
        print("2. Operating System Scan")
        print("3. Agressive Scan For An IP Address")
        print("4. Scan The Network For All Devices")
        print("M. Main Menu")
        print('====================================')
        print 
        ans=input("What would you like to do? Enter your selection: ")

        if ans=="1":
              os.system('cls' if os.name == 'nt' else 'clear')
              print
              print("______________________________________________________________________")
              print
              portscan=input("Enter the IP you want to scan the ports of: ")
              print("______________________________________________________________________")
              os.system("sudo nmap " + portscan)
              print("______________________________________________________________________")
        elif ans=="2":
              os.system('cls' if os.name == 'nt' else 'clear')
              print
              print("______________________________________________________________________")
              print
              osscan=input("Enter the IP you want to find the operating system of: ")
              print("______________________________________________________________________")
              os.system("sudo nmap -O " + osscan)
              print("______________________________________________________________________") 
                
        elif ans=="3":
                os.system('cls' if os.name == 'nt' else 'clear')
                print
                print("______________________________________________________________________")
                print
                ascan=input("Enter the IP you want to scan: ")
                print
                print("______________________________________________________________________")
                os.system("sudo nmap -A " + address)
                print("______________________________________________________________________")
        elif ans=="4":
              os.system('cls' if os.name == 'nt' else 'clear')
              print
              print("______________________________________________________________________")
              print
              address=input("Enter your address and range (i.e. 192.168.0.1/24) now: ")
              print
              print("______________________________________________________________________")
              os.system("sudo nmap -sn " + address)
              print("______________________________________________________________________")
        elif ans=="M":
                os.system('cls' if os.name == 'nt' else 'clear')
                os.system('python3 webmap.py')
                
        else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print
                print("Not Valid Choice Try again")
                print
                os.system("python3 webmap.py")
                ans = None
