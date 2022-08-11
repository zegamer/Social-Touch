# Recieves haptic input from haptic_send.ino
# Sends signal to reciever.py

import connection

com = connection.connectComPort("Leonardo")
sock, ot_ip = connection.connectSocket()

try:
    while True:
        val = com.readline()
        print(val)
        sock.sendto(val, ot_ip)

except Exception as e:
    print(e)

finally:
    print("Closing")
    com.close()
    sock.close()
