[< Back to Python Projects](https://github.com/KrisLloyd/Python#python)
***

# About
This is a basic command line calendar. This calendar will allow the user to view the current calendar, and add/update/delete events.

# Useage

Save the program to disk, run the program from the command line

```
calendar.py
```

Use the menu to select different options. Any saved calendar data from previous sessions will automatically be loaded if available.

```
Welcome, Kris.
Today's Date: Saturday, April, 03, 2021
Current time: 07:05:25 PM

What would you like to do?

        [ A ] - Add new event
        [ U ] - Update an event
        [ V ] - View an event
        [ D ] - Delete an event
        [ X ] - Quit Calendar

Selection:
```

Any menu can be escaped using **'x'**

All events and changes made to the calendar will be saved at exit to **cal.dat**. Calendar is only saved when program shuts down gracefully, and keyboard interupts which result in the program ending prematurly will not trigger the saving mechanism.

# Examples

* Creating a calendar event:

  ```
  What is the date of the event?
  (format mm/dd/yyyy)

  Date: 04/03/2021


  What is the name of the event?

  Event name: My Event


  What are the event details?

  Event Details: These are details for the event
  ```

* Viewing an existing calendar event:

  ```
  What is the date of the event? (format mm/dd/yyyy) 04/03/2021

        Event: My Event
        Details: These are details for the event


  Press any key to return to the menu
  ```

* Updating an existing calendar event:

  ```
  Date: 04/03/2021
  Event: My Event
  Details: These are details for the event

  What would you like to update?
  [ 1 ] - Event date
  [ 2 ] - Event name
  [ 3 ] - Event message

  Selection: 3


  What are the event details?

  Event Details: Update the event details with a new message
  ```
