
import sys
import socket 
from datetime import datetime

#define our target
# argv is gonna be the amount arguments that we are giving.
# ' python3 scanner.py <ip> ' argv[0] -> scanner.py argv[1] -> <ip>
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) # translate hostname to IPv4
else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 scanner.py <ip>")

# add a pretty banner
print("-" * 50)
print("Scanning target: " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)

# we are setting a variable s because we're going to gather the IPv4 adress and we're going to gather the port that we're going to connect
# if a port is open, the area return will be 0, if a port is close it returns 1
try:
    for port in range(50,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()

except KeyboardInterrupt:  # ctrl+c
    print("\n Exiting program.")
    sys.exit()

except socket.gaierror:  # this is what happens when the hostname does not resolve
    print("hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Could not connect to server.")
    sys.exit()