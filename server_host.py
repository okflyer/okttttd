import socket

server=socket.socket()
server.bind(('127.0.0.1',8080))
server.listen(10)
client,addr=server.accept()
data=client.recv(1024)
html=open("xpath_example.html","r",encoding="utf-8").read()
res="HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n"+html
res=res.encode()
client.send(res)
print(data.decode())
#print(addr)
client.close()