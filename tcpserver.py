import socket
import threading

b_ip="0.0.0.0"
b_port=5000

ser=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ser.bind((b_ip,b_port))

ser.listen(5)

def handleclient(clientsocket):
    req=clientsocket.recv(1024)
    print("Received:",req)
    clientsocket.send("ACK!")
    clientsocket.close()

while True:
    client,add=ser.accept()
    print("Accepted Connection From:",add[0],add[1])
    client_h=threading.Thread(target=handleclient,args=(client,))
    client_h.start()
