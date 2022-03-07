import connection

s, ot_ip = connection.connectSocket()

try:
    while True:
        a = s.recv(16).decode().strip()
        print(a)
        if int(a) > 0:
            s.sendto('1'.encode(), ot_ip)
        else:
            s.sendto('0'.encode(), ot_ip)
            print("exiting")
            break
                
except Exception as e:
    print(e)

finally:
    print("Finally")
    s.close()