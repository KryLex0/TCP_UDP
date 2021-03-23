# coding: utf-8
import socket
import sys

#python.exe .\tcpclient.py 127.0.0.1 50

#tcpclient.py localhost 12000 bonjour

TCP_IP = sys.argv[1]
TCP_PORT = int(sys.argv[2])
msg      = sys.argv[3]

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)          #Internet, TCP

try:
    print("Connexion avec le serveur")
    socket.connect((TCP_IP, TCP_PORT))                              #connexion au serveur
    socket.send(msg.encode())                                       #envoie du message au serveur

    msg_recu = socket.recv(1024)                                    #reception de la réponse du serveur
    print(msg_recu.decode())                                        #affichage de la réponse du serveur


except:
    print("Impossible de se connecter au serveur")
    socket.close()                                                  #fermeture connexion
