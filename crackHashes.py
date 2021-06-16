
import subprocess
import time
times=[]
for h in range(1, 6):
	if(h==1):
		m=0 #MD5 modo 0
	if(h==2 or h==3):
		m=10 #MD5 pass:salt modo 10
	if(h==4):
		m=1000 #NTLM
	if(h==5):
		m=1800 #sha512
	comand=r'hashcat.exe -m '+str(m)+r' -o "C:\Users\Daniela\Desktop\tarea4 cripto\c'+str(h)+r'.txt" "C:\Users\Daniela\Desktop\tarea4 cripto\hashcat-6.2.1\Hashes\archivo_'+str(h)+r'" "C:\Users\Daniela\Desktop\tarea4 cripto\hashcat-6.2.1\diccionarios\diccionario_2.dict" --potfile-disable'
	start = time.time()
	subprocess.call(comand, cwd=r"C:\Users\Daniela\Desktop\tarea4 cripto\hashcat-6.2.1")
	done = time.time()
	times.append( done - start)

print("Time in seconds for crack files")	
for n in range(len(times)):
	print("Archivo",n,": ",times[n])

