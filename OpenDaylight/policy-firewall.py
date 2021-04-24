# Imports
import requests, json, os
from pprint import pprint
import os
import time
import sys


# r = requests.put()
# r = requests.delete()
# r = requests.head()
# r = requests.options()

# Global variables
RED = "\u001b[31m"
YELLOW = "\u001b[33m"
BLUE = "\u001b[34m"
GREEN = "\u001B[32m"
PURPLE = "\u001B[35m"
RESET = "\u001b[0m"
hosts = []
switches = []
state = '0'

# Assets
odl = [
"                                {RESET}".format(RESET = RESET),
"                                {RESET}".format(RESET = RESET),
"                                {RESET}".format(RESET = RESET),
"            {YELLOW}#//////*    %       {RESET}".format(YELLOW = YELLOW, RESET = RESET),
"     {YELLOW}&////# #//////*  /////     {RESET}".format(YELLOW = YELLOW, RESET = RESET),
"   {YELLOW}///////////////////////////  {RESET}".format(YELLOW = YELLOW, RESET = RESET),
"     {YELLOW}///////////////////////    {RESET}".format(YELLOW = YELLOW, RESET = RESET),
" {YELLOW}//////////////{RED}((({YELLOW}//////////////{RESET}".format(YELLOW = YELLOW, RED = RED, RESET = RESET),
" {YELLOW}*//////////{RED}(((((((({YELLOW}////////////{RESET}".format(YELLOW = YELLOW, RED = RED, RESET = RESET),
" {YELLOW}*//////////{RED}(((((((({YELLOW}////////////{RESET}".format(YELLOW = YELLOW, RED = RED, RESET = RESET),
"       {YELLOW}////////{RED}((({YELLOW}///////#      {RESET}".format(YELLOW = YELLOW, RED = RED, RESET = RESET),
"    {YELLOW}#///////////////////////    {RESET}".format(YELLOW = YELLOW, RESET = RESET),
"   {YELLOW}//////////////////////////&  {RESET}".format(YELLOW = YELLOW, RESET = RESET),
"      {YELLOW}////# #//////*  /////     {RESET}".format(YELLOW = YELLOW, RESET = RESET),
"            {YELLOW}#//////*            {RESET}".format(YELLOW = YELLOW, RESET = RESET),
"                                {RESET}".format(YELLOW = YELLOW, RESET = RESET),
"                                {RESET}".format(YELLOW = YELLOW, RESET = RESET),
"                                {RESET}".format(YELLOW = YELLOW, RESET = RESET)]

python = [
"               {BLUE}#(((((((((((((((#{RESET}".format(BLUE = BLUE, RESET = RESET),
"            {BLUE}&(((( (((((((((((((((({RESET}".format(BLUE = BLUE, RESET = RESET),
"            {BLUE}&(((   (((((((((((((((({RESET}".format(BLUE = BLUE, RESET = RESET),
"            {BLUE}&(((((((((((((((((((((({RESET}".format(BLUE = BLUE, RESET = RESET),
"                       {BLUE}#((((((((((( ,{YELLOW},,**{RESET}".format(BLUE = BLUE, YELLOW = YELLOW, RESET = RESET),
"   {BLUE}(((((((((((((((((((((((((((((((( ,{YELLOW},******({RESET}".format(BLUE = BLUE, YELLOW = YELLOW, RESET = RESET),
"  {BLUE}((((((((((((((((((((((((((((((((( ,{YELLOW}********/{RESET}".format(BLUE = BLUE, YELLOW = YELLOW, RESET = RESET),
" {BLUE}((((((((((((((((((((((((((((((((( ({YELLOW}**********{RESET}".format(BLUE = BLUE, YELLOW = YELLOW, RESET = RESET),
" {BLUE}((((((((((((((((((((((((((((((&  {YELLOW}************{RESET}".format(BLUE = BLUE, YELLOW = YELLOW, RESET = RESET),
" {BLUE}((((((((((((  {YELLOW}*,,,,,,,,,,,,,*****************{RESET}".format(BLUE = BLUE, YELLOW = YELLOW, RESET = RESET),
" {BLUE}((((((((((( {YELLOW},,,,,,,,,,,,,********************{RESET}".format(BLUE = BLUE, YELLOW = YELLOW, RESET = RESET),
"  {BLUE}(((((((((#{YELLOW}&,,,,,,,,,,,*********************{RESET}".format(BLUE = BLUE, YELLOW = YELLOW, RESET = RESET),
"   {BLUE}#(((((((#{YELLOW}&,,,,,,,,,*********************({RESET}".format(BLUE = BLUE, YELLOW = YELLOW, RESET = RESET),
"            {YELLOW}&,,,,,,*****{RESET}".format(YELLOW = YELLOW, RESET = RESET),
"            {YELLOW}&,,,,*,****************{RESET}".format(YELLOW = YELLOW, RESET = RESET),
"            {YELLOW}&,**************   %***{RESET}".format(YELLOW = YELLOW, RESET = RESET),
"             {YELLOW}*********************%{RESET}".format(YELLOW = YELLOW, RESET = RESET),
"                {YELLOW}#**************%{RESET}".format(YELLOW = YELLOW, RESET = RESET)]

def newline(num=1):
    for i in range(num):
        print()

def welcome():
    os.system('cls' if os.name=='nt' else 'clear')
    newline(2)
    print("OpenDaylight SDN Controller Policy Firewall".center(105, "="))
    newline(2)
    for i in range(len(odl)):
        print("\t " + odl[i] + "        " + python[i])
    newline(2)
    print("=".center(105, "="))
    time.sleep(2.5)

def emptyList(listType):
    print("[{YELLOW}*{RESET}] Warning: No {type} found.".format(YELLOW = YELLOW, RESET = RESET, type = listType))
    print("[{YELLOW}*{RESET}] Warning: Topology either has no {type}, or topology has not been pulled from controller.".format(YELLOW = YELLOW, RESET = RESET, type = listType))
    newline()
    print("[{YELLOW}*{RESET}] Would you like to attempt to pull the topology now? (y/n/x)".format(YELLOW = YELLOW, RESET = RESET))
    while True:
        op = input("{GREEN}>>>{RESET} ".format(GREEN = GREEN, RESET = RESET))
        if op.lower() == 'y':
            getTopology(False)
            if len(globals()[listType]) < 1:
                print("[{YELLOW}*{RESET}] Warning: Topology does not contain {type}. Try generating some traffic or verifying the topology.".format(YELLOW = YELLOW, RESET = RESET, type = listType))
                newline()
                x = input("Press any key to return to the menu options...")
                return False
            break
        if op.lower() == 'x' or op.lower() == 'n':
            return False
    return True

def menu():
    os.system('cls' if os.name=='nt' else 'clear')
    print("=".center(105, "="))
    print(" Menu ".center(105, "-"))
    print("=".center(105, "="))
    newline()
    print("Useage: Press {RED}x{RESET} on any menu to return to the main menu.".format(RED = RED, RESET = RESET))
    print("Press {RED}CTRL + C{RESET} to exit the program".format(RED = RED, RESET = RESET))
    newline(2)
    print("[1] Load Topology")
    print("[2] Show Known Hosts")
    print("[3] Show known Switches")
    print("[4] Show Flow Statistics")
    print("[5] Modify A Flow")
    print("[9] Exit")


def getTopology(s):
    newline()
    print("[{GREEN}*{RESET}] Requesting topology from controller.".format(GREEN = GREEN, RESET = RESET))
    time.sleep(0.5)
    response = requests.get('http://192.168.248.128:8181/restconf/operational/network-topology:network-topology', auth=('admin', 'admin'))
    if response != None:
        print("[{GREEN}*{RESET}] Request sucessful.".format(GREEN = GREEN, RESET = RESET))
    else:
        print("[{RED}*{RESET}] Request failed.".format(RED = RED, RESET = RESET))
        print("[{RED}*{RESET}] Check the status of the OpenDaylight Controller.".format(RED = RED, RESET = RESET))
        return
    data = response.json()

    print("[{GREEN}*{RESET}] Loading request into system.".format(GREEN = GREEN, RESET = RESET))
    for i in data['network-topology']['topology'][0]['node']:
        isNew = True
        if 'host' in i['node-id']:
            for j in range(len(hosts)):
                if hosts[j].name == i['node-id']:
                    isNew = False
            if isNew:
                hosts.append(host(i['node-id'], i['host-tracker-service:addresses'][0]['ip'], i['host-tracker-service:addresses'][0]['mac']))
        else:
            for j in range(len(switches)):
                if switches[j].name == i['node-id']:
                    isNew = False
            if isNew:
                switches.append(switch(i['node-id']))

    print("[{GREEN}*{RESET}] Topology has been loaded.".format(GREEN = GREEN, RESET = RESET))
    if s:
        newline()
        x = input("Press any key to return to the menu options...")
        return


def getHosts(s):
    os.system('cls' if os.name=='nt' else 'clear')
    print("=".center(105, "="))
    print(" Hosts ".center(105, "-"))
    print("=".center(105, "="))
    newline(2)

    if len(hosts) < 1:
        if emptyList('hosts') == False:
            return

    for i in hosts:
        print(i)

    if s:
        return
    newline()
    x = input("Press any key to return to the menu options...")


def getSwitches(s):
    os.system('cls' if os.name=='nt' else 'clear')
    print("=".center(105, "="))
    print(" Switches ".center(105, "-"))
    print("=".center(105, "="))
    newline(2)

    if len(switches) < 1:
        if emptyList('switches') == False:
            return

    print("[{GREEN}*{RESET}] Gathering info.".format(GREEN = GREEN, RESET = RESET))
    time.sleep(0.2)
    newline(2)
    print("\tSwitch ID:\t\tStatus:")
    print("\t----------\t\t-------")
    for i in switches:
        print("\t{}\t\t{GREEN}Active{RESET}".format(i.getName(), GREEN = GREEN, RESET = RESET))

    if s:
        return
    newline()
    x = input("Press any key to return to the menu options...")


# Classes
class host():
    def __init__(self, name, ip, mac):
        self.name = name
        self.ip = ip
        self.mac = mac

    def __str__(self):
        return "Host: {}\n\tIP: {}\n\tMAC: {}".format(self.name, self.ip, self.mac)

    def getName(self):
        return self.name

    def getIP(sefl):
        return self.ip

    def getMAC(self):
        return self.mac


class switch():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Switch-id: {}".format(self.name)

    def getName(self):
        return self.name


# Menu
try:
    while state != '9':
        # Welcome banner
        if state == '0':
            os.system('cls')
            welcome()
        else:
            os.system('cls')

        # Display Menu
        menu()
        newline()
        print("What would you like to do?")
        while True:
            state = input("{GREEN}>>>{RESET} ".format(GREEN = GREEN, RESET = RESET))
            if state == "":
                continue
            else:
                break

        # Load Topology
        if state == '1':
            getTopology(True)

        # Show Known Hosts
        if state == '2':
            getHosts(False)

        # Show Known Switches
        if state == '3':
            getSwitches(False)

        # Show Flows Statistics
        if state == '4':
            while True:
                op = input("Would you like to see the flow statistics for all switches (a) or a specific switch (s)? (a/s/x): ")
                if op == 'a' or op == 's' or op == 'x':
                    break
                else:
                    continue

            if op.lower() == 'a':
                print("\nStatistics for {} switches. Press ENTER to continue.\n".format(len(switches)))
                for switch in switches:
                    r = requests.get('http://192.168.248.128:8181/restconf/operational/opendaylight-inventory:nodes/node/{}/flow-node-inventory:table/0/opendaylight-flow-table-statistics:flow-table-statistics'.format(switch.name), auth=('admin', 'admin'))
                    print('Switch: {}\n\tActive Flows: {}\n\tPackets-Looked-Up: {}\n\tPackets Matched: {}'.format(switch.name, r.json()['opendaylight-flow-table-statistics:flow-table-statistics']['active-flows'], r.json()['opendaylight-flow-table-statistics:flow-table-statistics']['packets-looked-up'], r.json()['opendaylight-flow-table-statistics:flow-table-statistics']['packets-matched']))
                    x = input()
                x = input("\nPress any key to return to the menu options...")
            elif op.lower() == 's':
                print("\n")
                for i in range(len(switches)):
                    print('{}. {}'.format(i, switches[i].name))

                print("\n")
                while True:
                    op = input("Which switch would you like to see the flow statistics for? (#/x): ")
                    try:
                        if op == 'x' or int(op) in range(len(switches)):
                            break
                        else:
                            print("Not a valid option.")
                    except ValueError:
                        if op == '':
                            continue
                        print("Not a valid option")
                if op == 'x':
                    continue

                newline()
                r = requests.get('http://192.168.248.128:8181/restconf/operational/opendaylight-inventory:nodes/node/{}/flow-node-inventory:table/0/opendaylight-flow-table-statistics:flow-table-statistics'.format(switches[int(op)].name), auth=('admin', 'admin'))
                print('Switch: {}\n\tActive Flows: {}\n\tPackets-Looked-Up: {}\n\tPackets Matched'.format(switches[int(op)].name, r.json()['opendaylight-flow-table-statistics:flow-table-statistics']['active-flows'], r.json()['opendaylight-flow-table-statistics:flow-table-statistics']['packets-looked-up'], r.json()['opendaylight-flow-table-statistics:flow-table-statistics']['packets-matched']))
                x = input("\nPress any key to return to the menu options...")
            else:
                continue



        # Modify Flow
        if state == '5':
            print("This feature is under construction.")
            print("\nThis feature would make an API request to the ODL controller that would resemble the following:")
            print("POST http://192.168.248.128:8181/restconf/config/opendaylight-flow-table-statistics:get-flow-tables-statistics")
            print("\n\nThe resules would be in JSON format, and would be parsed for relevant data.")
            x = input("\nPress any key to return to the menu options...")

        # Enf of Loop
        os.system('cls')

except KeyboardInterrupt:
    newline(2)
    print("[{RED}*{RESET}] User aborted operation.".format(RED = RED, RESET = RESET))
    print("[{RED}*{RESET}] Exiting...".format(RED = RED, RESET = RESET))
    sys.exit(1)
