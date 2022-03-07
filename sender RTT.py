import connection
import time

s, ot_ip = connection.connectSocketSender()

try:
    x = 0
    for i in range(1, 101):
        t = time.perf_counter()
        s.sendto(str(i).encode(), ot_ip)
        if int(s.recv(16).decode().strip()) == 1:
            x += (time.perf_counter() - t)
        else:
            print("exiting")
            break
    
    s.sendto('0'.encode(), ot_ip)
    print("{} seconds".format(x/100))

except Exception as e:
    print(e)

finally:
    print("Finally")
    s.close()