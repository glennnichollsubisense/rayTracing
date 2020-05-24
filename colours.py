
def newColour(r, g, b):
    return (r, g, b)

def newBlack():
    return (0.0, 0.0, 0.0)

def newWhite():
    return (1.0, 1.0, 1.0)

def newRed():
    return (1.0, 0.0, 0.0)

def newGreen():
    return (0.0, 1.0, 0.0)

def newBlue():
    return (0.0, 0.0, 1.0)

def newYellow():
    return (1.0, 1.0, 0.0)

def newCyan():
    return (0.0, 1.0, 1.0)

def newMagenta():
    return (1.0, 0.0, 1.0)


def addAB(a, b):
    return (
             a[0] + b[0], \
             a[1] + b[1], \
             a[2] + b[2], \
           )

def subtractBFromA (a, b):

    return (a[0] - b[0], \
            a[1] - b[1], \
            a[2] - b[2]
           )

def multiplyColourByScalar (vec, scalar):

    return (vec[0] * scalar, \
            vec[1] * scalar, \
            vec[2] * scalar
           )



if __name__== "__main__":

    ##  Testing scripts

    print ('%s' % str(newCyan()))
    print (addAB(newGreen(), newBlue()))
    print (addAB(newYellow(), newBlue()))
    print (subtractBFromA(newYellow(), newBlue()))
    print multiplyColourByScalar (newYellow(), 3.1)
    
