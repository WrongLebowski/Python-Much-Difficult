# this is where i define my variables; "x" & "y" have a string in a string
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
# this is where the variables are printed
print x 
print y 
# this is a string within a string
print "I said: %r." % x
print "I also said: %s." % y 

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
# prints joke_evaluation string then the variable hilarious
print joke_evaluation % hilarious
# this combines the two strings into one long string
w = "This is the left side of..."
e = "a string with a right side."

print w + e 