from LogCollector.grabber import start_monitor
from time import sleep
from threading import Thread
from SmartContract.read import read
from SmartContract.write import write
from os import system, path, _exit
from queue import Queue
import sys

def menu():
    print("1) Start Mining")
    print("2) Read Data From Blockchain")
    print("3) Exit")
    
    inp = int(input())
    return inp

def pre_menu():
    print("1) Connect as a Node.")
    print("2) Start New Blockchain.")

    inp = int(input())
    ip_addr = ""
    if inp == 1:
        ip_addr = input('Enter IP address of Genesis Node:')
    else:
        print('Start Ganache on 0.0.0.0 and hit enter.')
        ip_addr = "0.0.0.0"
    
    return "http://" + ip_addr + ":" + "7545"



def mining():
    q = Queue()
    t1 = Thread(target = start_monitor, args =(q, ))
    t1.start()
    while True:
        if q:
            write(ganache_url, path_to_abi, address, server_id, q)
            print("Writing to Blockchain...")

def reading(count):
    read(ganache_url, path_to_abi, address, server_id, count)

print("WELCOME TO LogChain!")

ganache_url = pre_menu()

started = False
path_to_abi = path.abspath('abi.json')
address = "0x490E92418a235eA728A6d11541b185F850929B9f"
server_id = 3333

while True:
    
    system('clear')
    inp = menu()
   
    if inp == 1 and started:
        print("Mining already working.")
        continue
    
    if inp == 1:
        print('Starting Mining')
        t = Thread(target=mining)
        t.start()
        print('Mining Started')
        started = True
        sleep(4)
    elif inp == 2:
        count = int(input('Enter Number Of Records: '))
        reading(count)
        input()
    else:
        print('Exiting!')
        _exit(1)




         





