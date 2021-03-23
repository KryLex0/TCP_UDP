# coding: utf-8

import socket
import sys

#python.exe .\tcpserveur.py 50

#tcpclient.py 12000

TCP_PORT = int(sys.argv[1])
TCP_IP = ''

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)             #Internet, TCP
socket.bind((TCP_IP, TCP_PORT))
socket.listen(5)                                                       #liste d'attente (5 clients max et si aucune des connexions
                                                                       #n'est accepté, impossible qu'un autre client se connecte)
while True:
    try:
        print("En attente de client...")
        connexion_avec_client, addr = socket.accept()                          #acceptation d'une connexion d'un client

        print("client d'adresse", addr[0], "depuis port", addr[1])             #Adresse IP du client , Port d'écoute du client

#############################################################################################################################

        msg_recu = connexion_avec_client.recv(1024)                            #reception du message venant du client
        print("ok :", msg_recu.decode(), "\n")                                      #affichage du message venant du client

#############################################################################################################################

        msg_reponse = "reçu \'ok : " + msg_recu.decode() + "\'"
        connexion_avec_client.send(msg_reponse.encode())                       #envoie de la réponse du serveur au client



    except Exception as e:
        print(e)
        socket.close()                                          #fermeture de la connexion
