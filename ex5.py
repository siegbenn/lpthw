my_name = 'Bennett E. Siegel'
my_age = 20 # About to turn 21.
my_height = 12 * 6 + 1 # Inches.
my_weight = 150
my_eyes = 'Green'
my_teeth = 'White'
my_hair = "Brown"

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# This line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight , my_age + my_height + my_weight)