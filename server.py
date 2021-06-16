import socket
from rabin import *
import bcrypt
import time

bits=800
while True:
        p = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
        if ((p % 4)==3): break

while True:
        q = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
        if ((p % 4)==3): break
n = p*q
print(("bit prime numbers ") , bits)
print("Private key is p:",p,"q:",q)
print("Public key is:",n) 


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind( (socket.gethostname(),1234) )
server.listen(5)
i=0
data= []
while True:                 # Bucle para esperar clientes nuevos
    clientConnection,clientAddress = server.accept()
    print ("CONNECTED CLIENT: ", clientAddress)
    clientConnection.sendall(bytes(str(n),'utf-8'))

    while True:             # Bucle para repetir con un cliente conectado
        recv = clientConnection.recv(4096)
        if recv == b"":     # Recibida cadena de bytes vacía implica desconexión
            break           # Salir de este bucle interno

        print ("RECIEVED STRING: "+recv.decode())
        data.append(recv.decode())
        clientConnection.sendall(bytes("OK",'utf-8'))
	
  
    print("CLIENT DISCONNECTED")
    clientConnection.close()   # Cerramos el socket pues ya no es útil
    break
    # Y volvemos a aceptar otro cliente

b=""
print(data)
#decoding data
for z in range(len(data)):
	plaintext = decryption(int(data[z]), p, q)
	st=format(plaintext, 'x')
	a=bytes.fromhex(st).decode()
	print(a)
	b= b+a+'\n'

print(b)
plainTextData = b.split("\n")
print(plainTextData)
#rehash

hashes= ""
start = time.time()
for h in range(len(plainTextData)-1):
	passwd = plainTextData[h].encode()
	salt= bcrypt.gensalt()
	hashed = bcrypt.hashpw(passwd, salt)
	hashes = hashes + hashed.decode() + '\n'
done = time.time()
print("time: ",done - start)
f = open ('output.txt','w')
f.write(hashes)
f.close()

