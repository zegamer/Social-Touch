import socket
import serial
import serial.tools.list_ports

# # For quick view of boards' IDs, run this in python terminal
# # Lists board name, port number and hardware ID

# import serial.tools.list_ports
# ports = serial.tools.list_ports.comports()
# for p, d, h in ports:
#     print("{}: {} [{}]".format(p,d,h))

def findComPort(board):

    ports = serial.tools.list_ports.comports()

    # Find board COM port from name of board than manually writing 'COM4'
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

    # my_pc_name = ""
    # my_port = 4000
    # other_pc_name = "
    # other_port = 4005
    
    # This does not work sometimes
    # my_ip = (socket.gethostbyname(my_name), my_port)
    # ot_ip = (socket.gethostbyname(oter_pc_name), other_port)  

    my_ip = ('192.168.0.105', 4005)
    ot_ip = ('192.168.0.101', 4000)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(my_ip)
    return (s, ot_ip)
