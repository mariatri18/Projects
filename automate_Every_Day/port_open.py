import socket

ip = socket.gethostbyname(socket.gethostname())

for port in range(65535):
    try:
        serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serv.bind((ip,port))

    except:
        print('[OPEN] Port Open :',port)

    serv.close()    
