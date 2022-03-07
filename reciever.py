import connection

com = connection.connectComPort("ESP32")
sock, ot_ip = connection.connectSocket()
prev, cur = 0, 0

try:
    while True:
        cur = sock.recv(16)
        if cur is not prev:
            print(cur.decode().strip())
            com.write(cur)
            prev = cur

except Exception as e:
    print(e)

finally:
    print("Closing")
    com.close()
    sock.close()
