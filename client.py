import socket
from rabin import *

allData = ""
dataToSend=[]
for i in range(1,6):
	f = open ('c'+str(i)+'.txt','r')
	allData=allData + f.read() 
	f.close()

x = allData.split("\n")
for i in range(len(x)-1):
	if( i > 1000 and i< 3000):
		dataToSend.append(x[i].split(":")[2]) 
	else:
		dataToSend.append(x[i].split(":")[1]) 
print(len(dataToSend),"hashes crakeados")

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect( (socket.gethostname(), 1234) )

data = my_socket.recv(4096)
publicKey=int(data.decode("utf-8"))
print(publicKey)

for z in range(len(dataToSend)):
	datoPrueba=str(dataToSend[z])
	plaintext =  bytes_to_long(datoPrueba.encode('utf-8'))
	ciphertext = encryption(plaintext, publicKey)
	my_socket.send(str(ciphertext).encode())
	data = my_socket.recv(4096)
	print (data.decode("utf-8"))
 

