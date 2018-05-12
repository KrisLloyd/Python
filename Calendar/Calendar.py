"""This is a basic command line calendar. This calendar will allow the user to view the current calendar, and add/update/delete events in the calendar."""

from time import sleep, strftime

username = "Kris"
#raw_input("Please enter your name: ")

calendar = {}


def welcome():
  print "Calendar is opening...\n"
  print "Welcome, " + username + "."
  sleep(1)
  print "Today's Date: " + strftime("%A, %B, %d, %Y")
  print "Current time: " + strftime("%I:%M:%S %p")
  print "\nWhat would you like to do?"

  
def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = raw_input("\nA - Add new event\nU - Update an event\nV - View an event\nD - Delete an event\nX - Quit Calendar\nYour choice: ")
    user_choice = user_choice.upper()
    if user_choice == "V":
      if len(calendar.keys()) < 1:
        print "You have no events in the calendar."
      else:
        print "The calendar should print here..."
        print calendar
    elif user_choice == "U":
      date = raw_input("What date would you like to update? (MM/DD/YYYY) ")
      if (10 < len(date) < 10) or (int(date[6:]) < int(strftime("%Y"))) or (int(date[:2]) not in range(1, 13)) or (int(date[3:5]) not in range(1, 31)):
        print "An invalid date was entered."
        try_again = raw_input("Would you like to try again? (Y/N) ")
        try_again = try_again.upper()
        if try_again == "Y":
          continue
        else:
          start = False
      print "\nFound the following event(s) on %s:" % (date)
      print calendar[date]
      event = raw_input("\nWhich event would you like to update? ")
      if event in calendar[date]:
        calendar[date][calendar[date].index(event)] = raw_input("\nWarning, this action will overwrite the previous entry.\nWhat would you like to update this entry with?\nUpdate for '%s' on '%s': " % (event, date))
        print "Updating..."
        sleep(1)
        print "Update completed."
        print calendar
    elif user_choice == "A":
      event = raw_input("What event would you like to add? ")
      date = raw_input("What is the date of the event? (MM/DD/YYYY) : ")
      if (10 < len(date) < 10) or (int(date[6:]) < int(strftime("%Y"))) or (int(date[:2]) not in range(1, 13)) or (int(date[3:5]) not in range(1, 31)):
        print "An invalid date was entered."
        try_again = raw_input("Would you like to try again? (Y/N) ")
        try_again = try_again.upper()
        if try_again == "Y":
          continue
        else:
          start = False
      else:
        if date in calendar:
          calendar[date].append(event)
        else:
          calendar[date] = []
          calendar[date].append(event)
    elif user_choice == "D":
      if len(calendar.keys()) < 1:
        print "You have no events in the calendar."
      else:
        event = raw_input("What event would you like to delete? ")
        count = 0
        delete_list = []
        for date in calendar.keys():
          if event in calendar[date]:
            count += 1
            delete_list.append(date)
        print
        print "Found %s matche(s)" % (count)
        print "Matching event foind on date %s" % (date)
        if count > 0:
          print
          delete_event = raw_input("Which date would you like to remove? (MM/DD/YYYY) ")
          if (10 < len(date) < 10) or (int(date[6:]) < int(strftime("%Y"))) or (int(date[:2]) not in range(1, 13)) or (int(date[3:5]) not in range(1, 31)):
            print "An invalid date was entered."
            try_again = raw_input("Would you like to try again? (Y/N) ")
            try_again.upper()
            if try_again == "Y":
              continue
            else:
              start = False
          calendar[date].remove(event)
          print "Event %s was sucessfully deleted from %s." % (event, date)
    elif user_choice == "X":
      user_input = raw_input("\nAre you sure you want to quit? (Y/N) ")
      user_input = user_input.upper()
      if user_input == "Y":
        start = False
      else:
        continue
    else:
      print "\nInvalid menu option. Please try again.\n"
      continue
    
start_calendar()
