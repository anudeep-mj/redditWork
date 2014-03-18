'''
Created on Mar 9, 2014

@author: Anudeep
'''
print "Hello World!"
print "Hello Again"
print "I like typing this."
print "This is fun."
print 'Yay! Printing.'
print "I'd much rather you 'not'."
print 'I "said" do not touch this.'

print "I will now count my chickens:"

print "Hens", 25 + 30 / 6
print "Roosters", 100 - 25 * 3 % 4

print "Now I will count the eggs:"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2



cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."


my_name = 'Anudeep'
my_age = 24
my_height = 185
my_weight = 170
my_eyes = 'brown'
my_teeth = 'white'
my_hair = 'black'

print 'lets talk about %s' % my_name
print "he is", my_height, 'cms tall'
print "he is %d pounds heavy" % my_weight
print "thats not up there yet"
print "he is %s eyes and %s hair" %(my_eyes, my_hair)
print "his teeth are usually %s  depending on the coffee" % my_teeth
print "if i add %d, %d, add %d I get %d" % (my_age, my_weight, my_height, my_weight+my_height+my_height)




x = "there are %d types of people in the world!" % 10
binary = "binary"
do_not = "don't"
y= "those who know %s and those who %s" % (binary, do_not)
print x
print y

print "I said: %r" % x
print "I also said: %s" % y 
hilarious = False
joke_evaluation = "Isn't that funny ?! %r"
print joke_evaluation % hilarious

w = "this is the left side of ...."
e = "a string with a right side"

print w+e



print "mary had a little lamb"
print "its fleece was white as %s" % 'snow'
print "and everywhere that mary went"
print "." * 10 

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
print end1+end2+end3+end4+end5+end6,
print end7+end8+end9+end10+end11+end12


formatter = "%r %r %r %r"
print formatter % (1,2,3,4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
                 "I had this thing.",
                 "That you could type up right.",
                 "But it didn't sing.",
                 "So I said goodnight."
)


days= "mon tue wed thu fri sat sun"
months= "jan\nfeb\nmar\napr\nmay\njun\njul\naug\nsep\noct\ndec"

print "here are the days:", days
print "here are the months:", months
print """
There's something going on here
with the three double quotes
we'll be able to type as much as we want
4 or 5 or 6
"""

tabby_cat = "\t i'm tabbed in"
persian_cat = "i'm split\non a line"
backlash_cat = "i'm \\ a \\ cat"
fat_cat = """
i'll do a list:
\t* cat food
\t* fishies
\t* catnip 
"""

print tabby_cat
print persian_cat
print backlash_cat
print fat_cat


# print "how old are you ?"
# age = int(raw_input())
# print "how tall are you?"
# height = raw_input()
# print "how much do you weigh ?"
# weight = raw_input()
# 
# print "so you are %d years old, %r cms tall and %r in weight" % (age, height, weight)


# age = raw_input("how old are you ? ")
# height = raw_input("how tall are you ?")
# weight = raw_input("how much do you weigh ?")

# print "so you are %r years old, %r cms old and %r lbs heavy" % (age, height, weight)




