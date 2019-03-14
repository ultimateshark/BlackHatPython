import socket

t_host=input("Enter Host:  ")
t_port=int(input("Enter Port:  "))

#create socket object
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#sending some data to client
client.sendto("AAABBBCCC",(t_host,t_port))

#now receive some data
data,ad=client.recvfrom(4096)
print(data)
