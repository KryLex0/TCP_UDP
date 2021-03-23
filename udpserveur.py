# coding: utf-8

import socket
import sys

#udpclient.py 12000

UDP_PORT = int(sys.argv[1])
UDP_IP = ''

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)           #Internet, UDP
socket.bind((UDP_IP, UDP_PORT))

#############################################################################################################################

while True:
    try:
        print("En attente de client...")
        data, addr = socket.recvfrom(1024)                                  #reception du message venant du client
        print("client d'adresse",addr[0], "depuis port", addr[1])           #Adresse IP du client , Port d'écoute du client
        print("ok :", data.decode())                                        #affichage du message venant du client

#############################################################################################################################

        data_reponse = "reçu \'ok : " + data.decode() + "\'"
        socket.sendto(data_reponse.encode(), (addr[0], addr[1]))            #envoie de la réponse du serveur au client

    except Exception as e:
        print(e)
        socket.close()                                                      #fermeture connexion
