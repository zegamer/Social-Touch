import socket
import serial
import serial.tools.list_ports

def findComPort(board):
    ports = serial.tools.list_ports.comports()

    # Mapped to a particular board only
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
    
    # my_ip = (socket.gethostbyname(my_name), 4000)
    # ot_ip = (socket.gethostbyname(ot_name), 4005)    

    # Hardcoding IPs since gethostbyname returned ethernet ip in some instances
    my_ip = ("192.168.0.101", 4000)
    ot_ip = ("192.168.0.102", 4005)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(my_ip)
    return (s, ot_ip)


if __name__ == "__main__":
    s, ot = connectSocket()
    print(ot)
    s.close()