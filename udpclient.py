# coding: utf-8

import socket
import sys



#udpclient.py localhost 12000 bonjour

UDP_IP = sys.argv[1]
UDP_PORT = int(sys.argv[2])
msg  = sys.argv[3]

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   #Internet, UDP

try:
    print("Connexion avec le serveur")
    socket.sendto(msg.encode(), (UDP_IP, UDP_PORT))         #envoie du msg au serveur

    data, addr = socket.recvfrom(1024)                      #reception de la réponse du serveur
    print(data.decode())                                    #affichage de la réponse du serveur


except:
    print("Impossible de se connecter au serveur")
    socket.close()                                          #fermeture connexion
