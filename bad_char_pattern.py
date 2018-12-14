import sys

def run():
    if len(sys.argv) > 2:
        print buildUsage()
    elif len(sys.argv) == 1:
        print buildChars()
    elif len(sys.argv) == 2:
        print "Not yet implemented, sorry!"

def buildUsage():

    return ""

# builds the string of potentially bad characters
def buildChars():
    pattern = ''
    c = 0
    while c < 256:
        # we want \x01 instead of \x1
        if c < 16:
            pattern += "\\x0%x" %c
        else:
            pattern += "\\x%x" %c 
        c += 1

    return pattern

run()
