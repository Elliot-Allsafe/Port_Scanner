import sys
import socket
from datetime import datetime as dt
print("*** It Takes Some Time but It's Worth It ***")
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Wrong Syntax")
    print("Syntax: python Port_Scanner.py HostName")
try:
    print("-"*50)
    print("Scanning Target: "+str(target))
    print("Scanning Started: "+str(dt.now()))
    print("-"*50)
except NameError:
    print("Exiting Program...")
    sys.exit()

try:
    print("Port Number Should Be btw(0-65535)")
    r1 = int(input("Enter First Port Number:> "))
    r2 = int(input("Enter Last Port Number:> "))
    print("-"*50)
    for port in range(r1, r2+1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Checking Port Number:> "+str(port))
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print("*"*50)
            print("YES!! Port "+str(port)+" is open..")
            print("*"*50)
        s.close()
except KeyboardInterrupt:
    print("Exiting Program!!")
    sys.exit()
except socket.gaierror:
    print("Unable to resolve HostName..")
    sys.exit()
except socket.error:
    print("Host Seems Down!!!")
    print("Exiting Program!")
    sys.exit()
except ValueError:
    print("Enter a Number Only..")
    print("Try Running the Script Again!")
    sys.exit()
except NameError:
    print("Enter a Number Only..")
    print("Try Running the Script Again!")
    sys.exit()
