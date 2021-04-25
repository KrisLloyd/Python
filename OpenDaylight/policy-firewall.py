# Imports
import requests, json, os
from pprint import pprint
import os
import time
import sys
import re


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
flows = {}
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
                x = input("Press any key to return to the main menu...")
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
    print("[5] Add/Modify A Flow")
    print("[9] Exit")


def getTopology(s):
    newline()
    print("[{GREEN}*{RESET}] Requesting topology from controller.".format(GREEN = GREEN, RESET = RESET))
    time.sleep(0.5)
    response = requests.get('http://192.168.248.128:8181/restconf/operational/network-topology:network-topology', auth=('admin', 'admin'))
    if response:
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

    # Sort Hosts
    hosts.sort(key=lambda x: x.getName())
    # Sort Switches
    switches.sort(key=lambda x: x.getName())
    # Add Switches flows dictionary
    for i in switches:
        if i.getName() not in flows:
            flows[i.getName()] = []


    print("[{GREEN}*{RESET}] Topology has been loaded.".format(GREEN = GREEN, RESET = RESET))
    if s:
        newline()
        x = input("Press any key to return to the main menu...")
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

    newline(2)
    print("[{GREEN}*{RESET}] Gathering info.".format(GREEN = GREEN, RESET = RESET))
    time.sleep(0.2)
    newline(2)
    print("\tHost ID:\t\t\tIP Address:\tMAC Address:\t\tStatus:")
    print("\t----------\t\t\t-----------\t------------\t\t-------")
    for i in hosts:
        print("\t{HOST}\t\t{IP}\t{MAC}\t{GREEN}Active{RESET}".format(HOST = i.getName(), IP = i.getIP(), MAC = i.getMAC(), GREEN = GREEN, RESET = RESET))
    newline()

    if s:
        return
    newline()
    x = input("Press any key to return to the main menu ...")


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
    x = input("Press any key to return to the main menu...")


def getFlows():
    while True:
        os.system('cls' if os.name=='nt' else 'clear')
        print("=".center(105, "="))
        print(" Flows ".center(105, "-"))
        print("=".center(105, "="))
        newline(2)

        print("[1] Show All Flows")
        print("[2] Add A Flow")
        print("[3] Modify A Flow")
        print("[4] Delete A Flow")
        print("[9] Return To Main Menu")
        newline()
        print("What would you like to do?")
        while True:
            state = input("{GREEN}>>>{RESET} ".format(GREEN = GREEN, RESET = RESET))
            if state == "":
                continue
            else:
                break

        newline()
        # Show all flows
        if state == '1':
            print("[{GREEN}*{RESET}] Gathering info.".format(GREEN = GREEN, RESET = RESET))
            time.sleep(0.2)
            if len(switches) < 1:
                if emptyList('switches') == False:
                    return
            print("----- All Flows: -----".center(105, " "))
            newline()
            for switch in switches:
                response = requests.get('http://192.168.248.128:8181/restconf/operational/opendaylight-inventory:nodes/node/{SWITCH}/table/0'.format(SWITCH = switch.getName()), auth=('admin', 'admin'))
                data = response.json()
                newline()
                flows[switch.getName()] = []
                print("\tSwitch ID: {SWITCH}".format(SWITCH = switch.getName()))
                for j in range(len(data['flow-node-inventory:table'][0]['flow'])):
                    if data['flow-node-inventory:table'][0]['flow'][j]['id'][0] != 'L' and data['flow-node-inventory:table'][0]['flow'][j]['id'][0] != '#':
                        flows[switch.getName()].append(data['flow-node-inventory:table'][0]['flow'][j]['id'])
                if len(flows[switch.getName()]) > 0:
                    for i in range(len(flows[switch.getName()])):
                        print("\t\tFlow ID: {ID}".format(ID = flows[switch.getName()][i]))
                else:
                    print("\t\t{YELLOW}NOTICE{RESET} - No flows have been applied to this device.".format(YELLOW = YELLOW, RESET = RESET))

            newline()
            print("[{GREEN}*{RESET}] Complete.".format(GREEN = GREEN, RESET = RESET))
            input("Press any key to return to the Flows menu...")

        # Add flow rule
        if state == '2':
            os.system('cls' if os.name=='nt' else 'clear')
            if len(switches) < 1:
                if emptyList('switches') == False:
                    return
            if len(hosts) < 1:
                if emptyList('hosts') == False:
                    return
            print("----- Add A Flow: -----".center(105, " "))
            newline()
            print("\tSelect the souce(s):")
            newline()
            print("\tSelection\tHost ID:\t\t\tIP Address:\tMAC Address:\t\tSRC: DST:")
            print("\t---------\t--------\t\t\t-----------\t------------\t\t---- ----")
            for i in range(len(hosts)):
                print("\t[{i}]\t\t{HOST}\t\t{IP}\t{MAC}".format(i = i + 1, HOST = hosts[i].getName(), IP = hosts[i].getIP(), MAC = hosts[i].getMAC()))

            newline(2)
            print("\tSeparate multiple hosts with a space.")
            print("\tExample:")
            print("\t\t{GREEN}>>>{RESET} 1 3 5".format(GREEN = GREEN, RESET = RESET))
            newline()

            # This section needs input validation. To do at a later time. -------
            sources = list(map(int, input("{GREEN}>>>{RESET} ".format(GREEN = GREEN, RESET = RESET)).split()))
            # --------------------------------------------------------------------

            os.system('cls' if os.name=='nt' else 'clear')
            print("----- Add A Flow: -----".center(105, " "))
            newline()
            print("\tSelect the destination(s):")
            newline()
            print("\tSelection\tHost ID:\t\t\tIP Address:\tMAC Address:\t\tSRC: DST:")
            print("\t---------\t--------\t\t\t-----------\t------------\t\t---- ----")
            for i in range(len(hosts)):
                m = "\t[{i}]\t\t{HOST}\t\t{IP}\t{MAC}"
                if i + 1 in sources:
                    m += "\t {RED}*{RESET}"
                print(m.format(i = i + 1, HOST = hosts[i].getName(), IP = hosts[i].getIP(), MAC = hosts[i].getMAC(), RED = RED, RESET = RESET))

            newline(2)
            print("\tSeparate multiple hosts with a space.")
            print("\tExample:")
            print("\t\t{GREEN}>>>{RESET} 1 3 5".format(GREEN = GREEN, RESET = RESET))
            newline()

            # This section needs input validation. To do at a later time. -------
            destinations = list(map(int, input("{GREEN}>>>{RESET} ".format(GREEN = GREEN, RESET = RESET)).split()))
            # --------------------------------------------------------------------

            os.system('cls' if os.name=='nt' else 'clear')
            print("----- Add A Flow: -----".center(105, " "))
            newline()
            print("\tSelect the match criteria:")
            newline()
            print("\tSelection\tHost ID:\t\t\tIP Address:\tMAC Address:\t\tSRC: DST:")
            print("\t---------\t--------\t\t\t-----------\t------------\t\t---- ----")
            for i in range(len(hosts)):
                m = "\t[{i}]\t\t{HOST}\t\t{IP}\t{MAC}"
                if i + 1 in sources:
                    m += "\t {RED}*{RESET}"
                    if i + 1 in destinations:
                        m += "    {RED}*{RESET}"
                elif i + 1 in destinations:
                    m += "\t      {RED}*{RESET}"

                print(m.format(i = i + 1, HOST = hosts[i].getName(), IP = hosts[i].getIP(), MAC = hosts[i].getMAC(), RED = RED, RESET = RESET))
            newline(2)

            print("\tOptions - IP, MAC, PROTOCOL")
            print("\tExample:")
            print("\t\t{GREEN}>>>{RESET} MAC".format(GREEN = GREEN, RESET = RESET))
            newline()
            match = input("{GREEN}>>>{RESET} ".format(GREEN = GREEN, RESET = RESET))
            newline(2)
            print("\tSelect the switch(es) to apply the flow rule:")
            newline()
            print("\tSelection:\tSwitch:")
            print("\t----------\t-------")
            for i in range(len(switches)):
                print("\t[{i}]\t{SWITCH}".format(i = i + 1, SWITCH = switches[i].getName()))

            newline(2)
            print("\tSeparate multiple hosts with a space.")
            print("\tExample:")
            print("\t\t{GREEN}>>>{RESET} 4 6".format(GREEN = GREEN, RESET = RESET))
            newline()

            # This section needs input validation. To do at a later time. -------
            targets = list(map(int, input("{GREEN}>>>{RESET} ".format(GREEN = GREEN, RESET = RESET)).split()))
            # --------------------------------------------------------------------

            os.system('cls' if os.name=='nt' else 'clear')
            print("----- Add A Flow: -----".center(105, " "))
            newline()
            print("\tConfirm the following selections:")
            newline()
            print("\tSource:")
            for i in range(len(sources)):
                print("\t\tName: {}".format(hosts[sources[i] - 1].getName()))
                print("\t\tIP: {}".format(hosts[sources[i] - 1].getIP()))
                print("\t\tMAC: {}".format(hosts[sources[i] - 1].getMAC()))
            newline()
            print("\tDestination:")
            for i in range(len(destinations)):
                print("\t\tName: {}".format(hosts[destinations[i] - 1].getName()))
                print("\t\tIP: {}".format(hosts[destinations[i] - 1].getIP()))
                print("\t\tMAC: {}".format(hosts[destinations[i] - 1].getMAC()))
            newline()
            print("\tMatch:")
            print("\t\t{MATCH}".format(MATCH = match))
            newline()
            print("\tTargets:")
            for i in range(len(targets)):
                print("\t\t{}".format(switches[targets[i] - 1].getName()))

            newline(2)
            print("\tIs this information correct?")
            newline()
            # This section needs input validation. To do at a later time. -------
            confirm = input("{GREEN}>>>{RESET} ".format(GREEN = GREEN, RESET = RESET))
            # --------------------------------------------------------------------


            if confirm == 'y':
                newline()
                print("[{GREEN}*{RESET}] Flow data confirmed.".format(GREEN = GREEN, RESET = RESET))
                print("[{GREEN}*{RESET}] Sending flow request to controller.".format(GREEN = GREEN, RESET = RESET))

                for i in range(len(targets)):
                    for j in range(len(sources)):
                        for k in range(len(destinations)):
                            flowid = 'h' + hosts[sources[j] - 1].getName()[-1] + 'h' + hosts[destinations[k] - 1].getName()[-1] + 's' + switches[targets[i] - 1].getName()[-1] + '-' + match[:3]
                            xml = """<?xml version="1.0"?>
<flow xmlns="urn:opendaylight:flow:inventory">
  <priority>1000</priority>
  <flow-name>{FLOWID}</flow-name>
  <match>
    <ethernet-match>
      <ethernet-type>
        <type>2048</type>
      </ethernet-type>
    </ethernet-match>
    <ipv4-source>{SRC}/32</ipv4-source>
    <ipv4-destination>{DST}/32</ipv4-destination>
  </match>
  <id>{FLOWID}</id>
  <table_id>0</table_id>
  <instructions>
    <instruction>
      <order>0</order>
      <apply-actions>
        <action>
          <order>0</order>
          <drop-action/>
        </action>
      </apply-actions>
    </instruction>
  </instructions>
</flow>""".format(FLOWID = flowid, SRC = hosts[sources[j] - 1].getIP(), DST = hosts[destinations[k] - 1].getIP())
                            headers = {'Content-Type': 'application/xml'}
                            uri = 'http://192.168.248.128:8181/restconf/config/opendaylight-inventory:nodes/node/{SWITCH}/table/0/flow/{NAME}'.format(SWITCH = switches[targets[0] - 1].getName(), NAME = flowid)
                            request = requests.put(uri, data=xml, headers=headers, auth=('admin', 'admin'))

                            if request:
                                print("[{GREEN}*{RESET}] FlowID {FLOWID} added sucessfully.".format(GREEN = GREEN, RESET = RESET, FLOWID = flowid))
                            else:
                                print("[{RED}*{RESET}] Error applying flow {FLOWID}.".format(RED = RED, RESET = RESET, FLOWID = flowid))
                                print("[{RED}*{RESET}] Error: {REQUEST}".format(RED = RED, RESET = RESET, REQUEST = request))
                print("[{GREEN}*{RESET}] Complete.".format(GREEN = GREEN, RESET = RESET, FLOWID = flowid))
                input('Press any key to return to the Flows menu...')
            else:
                print("[{RED}*{RESET}] Aborting.".format(RED = RED, RESET = RESET))
                input('Press any key to return to the Flows menu...')

        # Modify existing rule
        if state == '3':
            newline()
            if len(switches) < 1:
                if emptyList('switches') == False:
                    return
            print("----- All Flows: -----".center(105, " "))
            newline()
            for switch in switches:
                response = requests.get('http://192.168.248.128:8181/restconf/operational/opendaylight-inventory:nodes/node/{SWITCH}/table/0'.format(SWITCH = switch.getName()), auth=('admin', 'admin'))
                data = response.json()
                newline()
                flows[switch.getName()] = []
                print("\tSwitch ID: {SWITCH}".format(SWITCH = switch.getName()))
                for j in range(len(data['flow-node-inventory:table'][0]['flow'])):
                    if data['flow-node-inventory:table'][0]['flow'][j]['id'][0] != 'L' and data['flow-node-inventory:table'][0]['flow'][j]['id'][0] != '#':
                        flows[switch.getName()].append(data['flow-node-inventory:table'][0]['flow'][j]['id'])
                if len(flows[switch.getName()]) > 0:
                    for i in range(len(flows[switch.getName()])):
                        print("\t\tFlow ID: {ID}".format(ID = flows[switch.getName()][i]))
                else:
                    print("\t\t{YELLOW}NOTICE{RESET} - No flows have been applied to this device.".format(YELLOW = YELLOW, RESET = RESET))

            newline(2)
            print("\tWhich flow would you like to modify?")
            newline()
            mod = input("{GREEN}>>>{RESET} ".format(GREEN = GREEN, RESET = RESET))
            if mod in flows[switches[int(mod[5]) - 1].getName()]:
                # Flow IO found
                newline()
                print("[{GREEN}*{RESET}] Requesting Flow ID {FLOWID} details from controller.".format(GREEN = GREEN, RESET = RESET, FLOWID = mod))
                response = requests.get('http://192.168.248.128:8181/restconf/operational/opendaylight-inventory:nodes/node/openflow:4/table/0/flow/{FLOWID}'.format(FLOWID = mod), auth=('admin', 'admin'))
                if response:
                    print("[{GREEN}*{RESET}] Request sucessful.".format(GREEN = GREEN, RESET = RESET))
                else:
                    newline()
                    print("[{RED}*{RESET}] Request failed.".format(RED = RED, RESET = RESET))
                    print("[{RED}*{RESET}] Error {ERROR}.".format(RED = RED, RESET = RESET, ERROR = response))
                    newline()
                    input("Press any key to return to the Flows menu...")

                data = response.json()
                newline(2)
                r = r"[a-z0-9]*-([a-zA-Z]{2,3})"
                src = data['flow-node-inventory:flow'][0]['match']['ipv4-source'].strip('/32')
                dst = data['flow-node-inventory:flow'][0]['match']['ipv4-destination'].strip('/32')
                type = re.search(r, mod)[1]
                tar = switches[int(mod[5]) - 1].getName()

                print('\tFlow ID: {FLOWID}'.format(FLOWID = mod))
                print("\t-------------------")
                print("\t[1] Source: {SRC}".format(SRC = src))
                print("\t[2] Destination: {DST}".format(DST = dst))
                print("\t[3] Match Type: {MAT}".format(MAT = type))
                print("\t[4] Switch: {SWITCH}".format(SWITCH = tar))

                newline(2)
                print("What would you like to change?")
                change = input("{GREEN}>>>{RESET} ".format(GREEN = GREEN, RESET = RESET))

                if change == '1':
                    newline(2)
                    print("What is the new source address?")
                    src = input("{GREEN}>>>{RESET} ".format(GREEN = GREEN, RESET = RESET))
                if change == '2':
                    newline(2)
                    print("What is the new destination address?")
                    dst = input("{GREEN}>>>{RESET} ".format(GREEN = GREEN, RESET = RESET))
                if change == '3':
                    newline(2)
                    print("What is the new match type?")
                    type = input("{GREEN}>>>{RESET} ".format(GREEN = GREEN, RESET = RESET))
                    print("What is the new source address?")
                    src = input("{GREEN}>>>{RESET} ".format(GREEN = GREEN, RESET = RESET))
                    print("What is the new destination address?")
                    dst = input("{GREEN}>>>{RESET} ".format(GREEN = GREEN, RESET = RESET))
                if change == '4':
                    newline(2)
                    print("What is the new switch?")
                    tar = input("{GREEN}>>>{RESET} ".format(GREEN = GREEN, RESET = RESET))

                print("[{GREEN}*{RESET}] Updating request.".format(GREEN = GREEN, RESET = RESET))

                print('DEBUG')
                print(src)
                print(dst)
                print(tar)
                print(type)
                flowid = 'h' + src[-1] + 'h' + dst[-1] + 's' + tar[-1] + '-' + type[:3]
                print(flowid)
                print('DEBUG END')

                flowid = 'h' + src[-1] + 'h' + dst[-1] + 's' + tar[-1] + '-' + type[:3]
                xml = """<?xml version="1.0"?>
<flow xmlns="urn:opendaylight:flow:inventory">
  <priority>1000</priority>
  <flow-name>{FLOWID}</flow-name>
  <match>
    <ethernet-match>
      <ethernet-type>
        <type>2048</type>
      </ethernet-type>
    </ethernet-match>
    <ipv4-source>{SRC}/32</ipv4-source>
    <ipv4-destination>{DST}/32</ipv4-destination>
  </match>
  <id>{FLOWID}</id>
  <table_id>0</table_id>
  <instructions>
    <instruction>
      <order>0</order>
      <apply-actions>
        <action>
          <order>0</order>
          <drop-action/>
        </action>
      </apply-actions>
    </instruction>
  </instructions>
</flow>""".format(FLOWID = flowid, SRC = src, DST = dst)
                headers = {'Content-Type': 'application/xml'}

                # Delete old request
                uriDel = 'http://192.168.248.128:8181/restconf/config/opendaylight-inventory:nodes/node/{SWITCH}/table/0/flow/{NAME}'.format(SWITCH = tar, NAME = mod)
                requestDel = requests.delete(uri, headers=headers, auth=('admin', 'admin'))
                if requestDel:
                    print("[{GREEN}*{RESET}] FlowID {FLOWID} removed.".format(GREEN = GREEN, RESET = RESET, FLOWID = mod))
                else:
                    print("[{RED}*{RESET}] Error removing flowID {FLOWID}.".format(RED = RED, RESET = RESET, FLOWID = mod))
                    print("[{RED}*{RESET}] Error: {REQUEST}".format(RED = RED, RESET = RESET, REQUEST = request))

                # Add new request
                uriNew = 'http://192.168.248.128:8181/restconf/config/opendaylight-inventory:nodes/node/{SWITCH}/table/0/flow/{NAME}'.format(SWITCH = tar, NAME = flowid)
                requestNew = requests.put(uriNew, data=xml, headers=headers, auth=('admin', 'admin'))
                if requestNew:
                    print("[{GREEN}*{RESET}] FlowID {FLOWID} added.".format(GREEN = GREEN, RESET = RESET, FLOWID = flowid))
                else:
                    print("[{RED}*{RESET}] Error applying flow {FLOWID}.".format(RED = RED, RESET = RESET, FLOWID = flowid))
                    print("[{RED}*{RESET}] Error: {REQUEST}".format(RED = RED, RESET = RESET, REQUEST = request))

                input('BREAK HERE')
            else:
                # Flow ID not found
                print("[{RED}*{RESET}] FlowID {FLOWID} not found.".format(RED = RED, RESET = RESET, FLOWID = mod))
            print("[{GREEN}*{RESET}] Complete.".format(GREEN = GREEN, RESET = RESET))
            input("Press any key to return to the Flows menu...")

        # Delete flow rule
        if state == '4':
            print("[{GREEN}*{RESET}] Gathering info.".format(GREEN = GREEN, RESET = RESET))
            time.sleep(0.2)
            if len(switches) < 1:
                if emptyList('switches') == False:
                    return
            print("----- All Flows: -----".center(105, " "))
            newline()
            for switch in switches:
                response = requests.get('http://192.168.248.128:8181/restconf/operational/opendaylight-inventory:nodes/node/{SWITCH}/table/0'.format(SWITCH = switch.getName()), auth=('admin', 'admin'))
                data = response.json()
                newline()
                flows[switch.getName()] = []
                print("\tSwitch ID: {SWITCH}".format(SWITCH = switch.getName()))
                for j in range(len(data['flow-node-inventory:table'][0]['flow'])):
                    if data['flow-node-inventory:table'][0]['flow'][j]['id'][0] != 'L' and data['flow-node-inventory:table'][0]['flow'][j]['id'][0] != '#':
                        flows[switch.getName()].append(data['flow-node-inventory:table'][0]['flow'][j]['id'])
                if len(flows[switch.getName()]) > 0:
                    for i in range(len(flows[switch.getName()])):
                        print("\t\tFlow ID: {ID}".format(ID = flows[switch.getName()][i]))
                else:
                    print("\t\t{YELLOW}NOTICE{RESET} - No flows have been applied to this device.".format(YELLOW = YELLOW, RESET = RESET))

            newline()

            print("\tWhich flow would you like to delete?")
            newline()
            delFlow = input("{GREEN}>>>{RESET} ".format(GREEN = GREEN, RESET = RESET))
            if delFlow in flows[switches[int(delFlow[5]) - 1].getName()]:
                headers = {'Content-Type': 'application/xml'}

                # Delete old request
                uriDel = 'http://192.168.248.128:8181/restconf/config/opendaylight-inventory:nodes/node/{SWITCH}/table/0/flow/{NAME}'.format(SWITCH = switches[int(delFlow[5]) - 1].getName(), NAME = headers)
                requestDel = requests.delete(uri, headers=headers, auth=('admin', 'admin'))
                if requestDel:
                    print("[{GREEN}*{RESET}] FlowID {FLOWID} removed.".format(GREEN = GREEN, RESET = RESET, FLOWID = mod))
                else:
                    print("[{RED}*{RESET}] Error removing flowID {FLOWID}.".format(RED = RED, RESET = RESET, FLOWID = mod))
                    print("[{RED}*{RESET}] Error: {REQUEST}".format(RED = RED, RESET = RESET, REQUEST = request))
            print("[{GREEN}*{RESET}] Complete.".format(GREEN = GREEN, RESET = RESET))
            input("Press any key to return to the Flows menu...")

        # Return to main menu
        if state == '9' or state == 'x':
            return

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

    def getIP(self):
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
                x = input("\nPress any key to return to the main menu...")
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
                x = input("\nPress any key to return to the main menu...")
            else:
                continue



        # Add Flow
        if state == '5':
            getFlows()
            x = input("\nPress any key to return to the main menu...")

        # Enf of Loop
        os.system('cls' if os.name=='nt' else 'clear')

except KeyboardInterrupt:
    newline(2)
    print("[{RED}*{RESET}] User aborted operation.".format(RED = RED, RESET = RESET))
    print("[{RED}*{RESET}] Exiting...".format(RED = RED, RESET = RESET))
    sys.exit(1)
