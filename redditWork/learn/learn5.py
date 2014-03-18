'''
Created on Mar 13, 2014

@author: Anudeep
'''
from sys import argv

script, filename = argv

print "we are going to erase %r" % filename
print "if you dont want that, hit CTRL+C"
print "if you do want that, hit RETURN"

raw_input("?")

print "opening the file...."
target = open(filename, 'w')

print "truncating the file..."
target.truncate()

print "now i am going to ask you for three lines"
line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "i am going to write thes to the file"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)


print "and we finally close it.."
target.close()



