myVar=int(raw_input('Type Number\n'))

if 0<=myVar<=5:
    print "number between 0 and 10"

    if myVar==3:
        print '3 is a nice number'

elif myVar<0:
    print "number below 0"

else:
    print "number greater than 10"
