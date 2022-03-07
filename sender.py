import connection

com = connection.connectComPort("Leonardo")
sock, ot_ip = connection.connectSocket()

prev, a = 0, 0

try:
    while True:
        cur = com.readline()
        print(cur)
        sock.sendto(cur, ot_ip)

except Exception as e:
    print(e)

finally:
    print("Closing")
    com.close()
    sock.close()