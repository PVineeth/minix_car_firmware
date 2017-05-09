import bluetooth
import socket
import commands

target_name = "LG K10 4G"
target_address = None
server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
port = 0
c_sck = socket.socket()
cmd = 0 # Fake Object

class device:

    def __init__(self, commandsobj):
        server_sock.bind(("", port))
        server_sock.listen(1)
        self.cmd = commandsobj

    def connect(self):
        nearby_devices = bluetooth.discover_devices()
        for bdaddr in nearby_devices:
            if target_name == bluetooth.lookup_name(bdaddr):
                target_address = bdaddr
                break
        client_sock, address = server_sock.accept()
        self.c_sck = client_sock
        print("Accepted connection from ", address)

    def receive_data(self):
        while True:
            data = self.c_sck.recv(1024)
            print ("received [%s]" % data)
            self.cmd.process_command(data)
            if(data == "e"):
                print ("EXIT")
                break


        client_sock.close()
        server_sock.close()
