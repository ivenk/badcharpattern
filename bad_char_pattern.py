import sys

# main
def run():
    if len(sys.argv) > 2:
        print buildUsage()
    elif len(sys.argv) == 1:
        print buildChars()
    elif (sys.argv[1] == '-h') or (sys.argv[1]=='--help'):
        print buildUsage()
    elif len(sys.argv) == 2:
        print "Not yet implemented, sorry!"

# builds and returns the usage string
def buildUsage():
    txt = ""
    txt += "Usage: \n"
    txt += "python badcharpattern.py (< pattern of ascii chars >)\n"
    txt += "    - no argument: prints pattern of ascii(256) chars \n"
    txt += "    - one argument <pattern of ascii chars>: prints the differences between the supplied pattern and the original one. "
    return txt

# builds and returns the string of potentially bad characters
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
