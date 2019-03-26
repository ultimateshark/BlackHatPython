import socket

t_host=input("Enter Host:  \n")
t_port=int(input("Enter PORT:  \n"))

#creating socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connect the client
client.connect((t_host,t_port))

#sending some data
client.send('GET / HTTP/1.1\r\nHost: '+t_host+'\r\n\r\n')

#receive information
res=client.recv(4096)

print(res)
