"""This is a basic command line calendar. This calendar will allow the user to view the current calendar, and add/update/delete events in the calendar."""

from time import sleep, strftime
import re
import datetime
import copy
import os
import csv

class Event:

    def __init__(self, date = None, name = None, message = None):
        self.date = self.setDate(True) if date == None else date
        self.name = self.setName(True) if name == None else name
        self.message = self.setMessage(True) if message == None else message


    def __repr__(self):
        return "Date: {} Event: {} Details: {}".format(self.date, self.name, self.message)

    def __str__(self):
        return "Date: {} Event: {} Details: {}".format(self.date, self.name, self.message)

    def setDate(self, new = False):
        while True:
            date = input("What is the date of the event?\n(format mm/dd/yyyy)\n\nDate: ")
            if checkDate(date):
                break
        if new:
            return date
        else:
            self.date = date

    def getDate(self):
        return self.date

    def setName(self, new = False):
        name = input("\n\nWhat is the name of the event?\n\nEvent name: ")
        if new:
            return name
        else:
            self.name = name

    def getName(self):
        return self.name

    def setMessage(self, new = False):
        message =  input("\n\nWhat are the event details?\n\nEvent Details: ")
        if new:
            return message
        else:
            self.message = message

    def getMessage(self):
        return self.message


def checkDate(date):
    # Format is mm/dd/yyyy
    res = re.search(r'(^[0-9]{2})/([0-9]{2})/([0-9]{4}$)', date)
    if res == None:
        return False
    try:
        if datetime.datetime(year=int(res[3]),month=int(res[1]),day=int(res[2])):
            return True
    except ValueError:
        return False

def getNum(s, numRange):
    while True:
        num = input(s)
        if num.lower() == 'x':
            return -1
        if num.isnumeric() and int(num) in range(1, numRange + 1):
            num = int(num)
            break
    return num - 1

def newline():
    print()

def clearScreen():
    os.system('cls' if os.name=='nt' else 'clear')

def display():
    print("Today's Date: " + strftime("%A, %B, %d, %Y"))
    print("Current time: " + strftime("%I:%M:%S %p"))

def getOp(s, params):
    while True:
        op = input(s)
        if op.lower() == 'x':
          return -1
        if op.isalpha() and op.upper() in params:
          return op.upper()

def addEvent(date = None, name = None, message = None):
    clearScreen()
    event = Event(date, name, message)
    if event.getDate() in calendar:
        calendar[event.getDate()].append(event)
    else:
        calendar.update({event.getDate(): [event]})
    if date == None:
        print("Event has been added to calendar.")

def deleteEvent():
    clearScreen()
    while True:
        date = input("What is the date of the event? (format mm/dd/yyyy) ")
        if checkDate(date):
            break
    if date in calendar:
        if len(calendar[date]) > 1:
            print("Multiple events for that date.")
            for i in range(len(calendar[date])):
                print("[ {} ] - {}".format(i + 1, calendar[date][i].getName()))
            op = getNum("Which event should be removed? (x to cancel)", len(calendar[date]))
            if op == -1:
                return
            calendar[date].pop(op)
        else:
            print("Removing event: {}".format(calendar[date].getName()))
            calendar.pop(date)
        return
    else:
        print('There are no events for the given date.')
        return

def viewEvent():
    clearScreen()
    while True:
        date = input("What is the date of the event? (format mm/dd/yyyy) ")
        if checkDate(date):
            break
    if date in calendar:
        op = 0
        if len(calendar[date]) > 1:
            newline()
            print("Found {} events for that date.".format(len(calendar[date])))
            for i in range(len(calendar[date])):
                print("\t[ {} ] - {}".format(i + 1, calendar[date][i].getName()))
            newline()
            op = getNum("Which event would you like to view? (x to cancel) ", len(calendar[date]))
            if op == -1:
                return
        newline()
        print("\tEvent: {}\n\tDetails: {}".format(calendar[date][op].getName(), calendar[date][op].getMessage()))
        input("\n\nPress any key to return to the menu")
        return
    else:
        newline()
        print('\tThere are no events for the given date.')
        input("\n\nPress any key to return to the menu")
        return

def updateEvent():
    clearScreen()
    while True:
        date = input("What is the date of the event? (format mm/dd/yyyy) ")
        if checkDate(date):
            break
    if date in calendar:
        op = 0
        if len(calendar[date]) > 1:
            print("Multiple events for that date.")
            for i in range(len(calendar[date])):
                print("[ {} ] - {}".format(i + 1, calendar[date][i].getName()))
            op = getNum("Which event would you like to update? (x to cancel)", len(calendar[date]))
            if op == -1:
                return

        event = copy.deepcopy(calendar[date][op])
        if len(calendar[date]) > 1:
            calendar[date].pop(op)
        else:
            calendar.pop(date)

        while True:
            clearScreen()
            print("Date: {}\nEvent: {}\nDetails: {}".format(event.getDate(), event.getName(), event.getMessage()))
            newline()
            print("What would you like to update?")
            op = getNum("[ 1 ] - Event date\n[ 2 ] - Event name\n[ 3 ] - Event message\n\nSelection: ", 3) + 1
            if op == -1:
                if event.getDate() in calendar:
                    calendar[event.getDate()].append(event)
                else:
                    calendar.update({event.getDate(): [event]})
                return
            if op == 1:
                event.setDate()
            elif op == 2:
                event.setName()
            else:
                event.setMessage()
            if getOp("Finished updates? (Y/N)", ['Y', 'N']) == "Y":
                if event.getDate() in calendar:
                    calendar[event.getDate()].append(event)
                else:
                    calendar.update({event.getDate(): [event]})
                return
        return
    else:
        print('There are no events for the given date.')
        return

def saveCalendar():
    print("\n\nSaving calendar.")
    with open('cal.dat', 'w') as f:
        for k, v in calendar.items():
            f.write("{}, {}\n".format(k, v))

def start_calendar():
  # Load calendar data
  if os.path.exists('cal.dat'):

      with open('cal.dat', 'r') as f:
          reader = csv.reader(f)
          r = r"(Date: ([0-9]{2}/[0-9]{2}/[0-9]{4})\sEvent: ([\w'\s]+['!\?\.\^\\\*]?)\sDetails: ([\w'\s]+['!\?\.\^\\\*]?))"
          for row in reader:
              for i in range(1, len(row)):
                  res = re.search(r, row[i])
                  addEvent(row[0], res[3], res[4])

  while True:
      clearScreen()
      print("Welcome, " + username + ".")
      sleep(1)
      display()
      print("\nWhat would you like to do?")
      print("\n\t[ A ] - Add new event\n\t[ U ] - Update an event\n\t[ V ] - View an event\n\t[ D ] - Delete an event\n\t[ X ] - Quit Calendar\n")
      choice = getOp("Selection: ", ['A', 'U', 'V', 'D'])
      if choice == -1:
          saveCalendar()
          break

      # State selector
      # Add event
      if choice == 'A':
          addEvent()
          continue
      # Delete event
      if choice == 'D':
          deleteEvent()
          continue
      # View event
      if choice == 'V':
          viewEvent()
          continue
      # Update event
      if choice == 'U':
          updateEvent()
          continue

if __name__ == "__main__":
    calendar = {}
    username = "Kris"
    start_calendar()
    print("Goodbye.")
