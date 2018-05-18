from socket import * #For programming using sockets
import re #For using RegEx matching in check_ips function
import subprocess #For ping results

#checks for valid IPs
def check_ips(ip):
    m = re.match(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)
    return bool(m) and all(map(lambda n: 0 <= int(n) <= 255, m.groups()))

s = socket(AF_INET, SOCK_STREAM)
s.bind("", 22)
s.listen(5)
while True:
    c,a = s.accept()
    print "Inbound connection received from: ", a
    c.send("Connection established.\nWhat is the IP address you would like to check connectivity for?\nIPv4 Address (x.x.x.x): ")
    data = s.recv(10000)
    if data == "quit":
        c.close()
    else:
        if check_ips(data):
            res = subprocess.call(['ping', '-c', '3', data])
            if res == 0:
                c.send("Destination is ONLINE.")
            else:
                c.send("Destination is OFFLINE.")
