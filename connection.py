import socket
import serial
import serial.tools.list_ports

# # For quick view of ports in python terminal
# import serial.tools.list_ports
# ports = serial.tools.list_ports.comports()
# for p, d, h in ports:
#     print("{}: {} [{}]".format(p,d,h))


def findComPort(board):
    ports = serial.tools.list_ports.comports()

    if board == "Leonardo":
        usbID = "USB VID:PID=2341:8036"
    elif board == "ESP32":
        usbID = "USB VID:PID=10C4:EA60"
    else:
        print("Board ID not registered")
        return 1

    for x in ports:
        if usbID in x[2]:
            return x[0]
    
    print("Port not found")
    exit(1)

def connectComPort(board):
    comPort = findComPort(board)
    print(comPort)
    return serial.Serial(comPort, 115200)

def connectSocket():
    
    # Ip, Ports combo should be same in both PCs 

    my_name = socket.gethostname()
    if my_name == "PC-18671":
        my_port = 4005 # Dell
        ot_port = 4000 # Asus
        ot_name = "DESKTOP-VI41OAR"
    elif my_name == "DESKTOP-VI41OAR":
        my_port = 4000 # Asus
        ot_port = 4005 # Dell
        ot_name = "PC-18671"
    
    my_ip = (socket.gethostbyname(my_name), my_port)
    ot_ip = (socket.gethostbyname(ot_name), ot_port)    

    # # IP valid in WiFi: medialab_50

    # if my_name == "PC-18671":
    #     my_ip = ("192.168.1.78", 4005) # Dell
    #     ot_ip = ("192.168.1.77", 4000) # Asus
    # elif my_name == "DESKTOP-VI41OAR":
    #     my_ip = ("192.168.1.77", 4000) # Asus
    #     ot_ip = ("192.168.1.78", 4005) # Dell
        
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(my_ip)
    return (s, ot_ip)