import socket
import sys
from datetime import datetime

if (len(sys.argv)==4):
    target = socket.gethostbyname(sys.argv[1]) # Define our target
    beginningPort = sys.argv[2]
    endingPort = sys.argv[3]
    if(beginningPort>endingPort):
        a = endingPort
        endingPort = beginningPort
        beginningPort = a
    elif(beginningPort==endingPort):
        endingPort+=1
    # Add a banner
    print("-" * 50)
    print("Scanning started : " + str(datetime.now()))
    print("-" * 50)

    try:
        for port in range(int(beginningPort), int(endingPort)):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Creation of socket
            socket.setdefaulttimeout(1)  # If port doesn't response after 1 seconds it means it is closed
            result = s.connect_ex((target, port))
            openPorts = []
            if result == 0:
                openPorts.append(port)
                print("Port {} is open".format(port))
        if(len(openPorts)==0):
            print("No open ports were found")
        else:
            print("Open ports are : "+openPorts)
    except KeyboardInterrupt:
        print("Exiting")
        print("Scanning finished " + str(datetime.now()))

    except socket.gaierror:
        print("Can't resolve hostname")
    except socket.error:
        print("Can't conncet to the server")
else:
    print("You missed something : Syntax looks like this : py portScanner.py <ip> <beginning_port> <ending_port>")

