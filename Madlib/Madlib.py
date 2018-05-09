"""This program is designed to be a MadLibs game. Users are prompted for input, which will then be substituted into blank spaces in a provided story, then print the resultsa for the user to read."""

# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."

print "Welcome to MadLibs!"
print ""
name = raw_input("Please enter a name: ")
print ""
print "Hello %s" % (name)
print ""
print "Time to get some words! We'll need 3 adjectives, 1 verb, 2 nouns, and some other fun choices! Lets Go!"
print ""
adjective1 = raw_input("Please enter an adjective: ")
adjective2 = raw_input("Please enter another adjective: ")
adjective3 = raw_input("Please enter a final adjective: ")
verb1 = raw_input("Please enter a verb: ")
noun1 = raw_input("Please enter a noun: ")
noun2 = raw_input("Please enter a final noun: ")
choice1 = raw_input("Please enter an animal: ")
choice2 = raw_input("Please enter a food: ")
choice3 = raw_input("Please enter a fruit: ")
choice4 = raw_input("Please enter a superhero: ")
choice5 = raw_input("Please enter a country: ")
choice6 = raw_input("Please enter a dessert: ")
choice7 = raw_input("Please enter a year: ")

print STORY % (name, adjective1, adjective2, choice1, choice2, verb1, noun1, choice3, adjective3, name, choice4, name, choice5, name, choice6, name, choice7, noun2)
