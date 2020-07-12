
class rtColour(object):

    def __init__(self, red=0.0, green=0.0, blue=0.0, name='No Name'):

        self.sName = name
        self.sRGB = (red, green, blue)


    def getName(self):

        return self.sName


    def getRGB(self):

        return self.sRGB


    def addB(self, b):
        bRGB = b.getRGB()
        return rtColour(
            self.sRGB[0] + bRGB[0], \
            self.sRGB[1] + bRGB[1], \
            self.sRGB[2] + bRGB[2], \
        )

    def subtractFromMe (self, b):
        
        return rtColour(self.sRGB[0] - b[0], \
                self.sRGB[1] - b[1], \
                self.sRGB[2] - b[2]
        )
    
    def multiplyByScalar (self, scalar):

        return rtColour(self.sRGB[0] * scalar, \
                self.sRGB[1] * scalar, \
                self.sRGB[2] * scalar
        )
    
    
    def multiplyByAnother (self, another):

        anotherRGB = another.getRGB()
        return rtColour(self.sRGB[0] * anotherRGB[0],
                        self.sRGB[1] * anotherRGB[1],
                        self.sRGB[2] * anotherRGB[2])



    def showMe(self, title=''):
        print ('Colour *** %s ** %s ** %s ' % (title, self.sName, str(self.sRGB)))

               
if __name__== "__main__":

    ##  Testing scripts

    print ('%s' % str(newCyan()))
    print (addAB(newGreen(), newBlue()))
    print (addAB(newYellow(), newBlue()))
    print (subtractBFromA(newYellow(), newBlue()))
    print (multiplyColourByScalar (newYellow(), 3.1))
    print (multiplyColourByAnother (newYellow(), newGreen()))
    
