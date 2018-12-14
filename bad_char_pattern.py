pattern = ''
c = 0
while c < 256:
    # we want \x01 instead of \x1
    if c < 16:
        pattern += "\\x0%x" %c
    else:
        pattern += "\\x%x" %c 
    c += 1

print pattern
