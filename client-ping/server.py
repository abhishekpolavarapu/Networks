import random
from socket import *
import time                

def main():
    # Create a UDP socket
    # Notice the use of SOCK_DGRAM for UDP packets
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    # Assign IP address and port number to socket
    serverSocket.bind(("", 7777))

    while True:
        rand = random.randint(0, 10)
        # Receive the client packet along with the address it is coming from
        msg, address = serverSocket.recvfrom(1024)
        msg = msg.upper()
        # If rand is less is than 4, we consider the packet lost and do not respond
        if rand < 4:
            continue
        # Otherwise, the server responds
        time.sleep(.05)        
        serverSocket.sendto(msg, address)
    pass

if __name__ == "__main__":
    main()
