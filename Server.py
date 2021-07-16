#access files remotly
#   *   Gain acces to different directories
#   *   View Files
#   *   Download Files
#   *   Remove Files
#   *   Remove Derectories
#   *   Send Files
#   *   Create Directory

#shut down remotly


import socket

s = socket.socket()
host = socket.gethostname()
port = 80
s.bind((host, port))
print("")
print(" server is currently running @ ", host)
print("")
print(" Waiting for any incoming connections...")
s.listen(1)
conn, addr = s.accept()
print("")
print(addr, "Has connected to the server successfully ")

#connection has been completed

#command handling

while 1:
    print("")
    command = input(str("Command >> "))
    if command == "view_cwd":
        conn.send(command.encode())
        print("")
        print("Command sent waiting for execution...")
        print("")
        files = conn.recv(5000)
        files = files.decode()
        print("Command output : ", files)

    elif command == "custom_dir":
        conn.send(command.encode())
        print("")
        user_input = input(str("Custom Dir: "))
        conn.send(user_input.encode())
        print("")
        print("Command has been send")
        print("")
        files = conn.recv(5000)
        files = files.decode()
        print("Custom Dir Result : ", files)

    elif command == "download_file":
        conn.send(command.encode())
        filepath = input(str("Please enter the file path including filename : "))
        conn.send(filepath.encode())
        file = conn.recv(100000)
        filename = input(str("Please enter a filename for the incoming file including the extension :"))
        new_file = open(filename, "wb")
        new_file.write(file)
        print(filename, "Has been downloaded and saved")

    else:
        print("")
        print("Command not recognised")
