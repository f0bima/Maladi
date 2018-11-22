import telnetlib
IP = "192.168.2.3"  # IP Base Station
tn = telnetlib.Telnet(IP, "28097")
# tn.write()
while 1:
    print(tn.read_all())
