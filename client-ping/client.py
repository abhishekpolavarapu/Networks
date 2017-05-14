from socket import *
from datetime import datetime                                   
# needed for my timeout system

def main():
    sName = "localhost" # destination server is localhost
    sPort = 7777# destination port number
    counter = 0  # number of pings starts at 0
    msg="PING"

    while counter < 10:                                  
        counter = counter +1                                  
        mainSocket = socket(AF_INET,SOCK_DGRAM)                 # create's socket

        try:
            mainSocket.settimeout(1.0) 
            startTime = datetime.now()                       

            mainSocket.sendto(msg,(sName, sPort)) # send the msg
            modifiedmsg, serverAddress = mainSocket.recvfrom(1024)  # modified msg is the msg it gets back
            endTime = datetime.now()                            # end time is current time at declaration

        except timeout:                                      
            print "PING" +str(counter)+" "+ str(startTime)+ ": Request timed out!" # print timeout msg
            mainSocket.close()                                
        else:                                                   # else print PING num Start Time Returned msg and RTT
            print "PING" +str(counter)+" "+ str(startTime)+": Returned: " + modifiedmsg + " after "+ str(endTime-startTime)

    mainSocket.close()                                          #close socket
    pass

if __name__ == "__main__":
    main()
