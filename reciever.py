# Recieves input from sender.py
# Sends signal to SleeveTouch.ino

import connection

com = connection.connectComPort("ESP32")
sock, ot_ip = connection.connectSocket()

try:
    while True:
        cur = sock.recv(16)
        print(cur)
        com.write(cur)

except Exception as e:
    print(e)
    

finally:
    print("Closing")
    com.close() 
    sock.close()

