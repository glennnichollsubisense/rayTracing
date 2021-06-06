
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
        resR = self.sRGB[0] + bRGB[0]
        resG = self.sRGB[1] + bRGB[1]
        resB = self.sRGB[2] + bRGB[2]
        if resR > 10.0:
            resR = 10.0
        if resG > 10.0:
            resG = 10.0
        if resB > 10.0:
            resB = 10.0
        return rtColour(resR, resG, resB)

    def subtractFromMe (self, b):
        
        bRGB = b.getRGB()
        resR = self.sRGB[0] - bRGB[0]
        resG = self.sRGB[1] - bRGB[1]
        resB = self.sRGB[2] - bRGB[2]
        if resR < 0.0:
            resR = 0.0
        if resG < 0.0:
            resG = 0.0
        if resB < 0.0:
            resB = 0.0

        return rtColour(resR, resG, resB)

    
    def multiplyByScalar (self, scalar):

        resR = self.sRGB[0] * scalar
        resG = self.sRGB[1] * scalar
        resB = self.sRGB[2] * scalar
        if resR > 10.0:
            resR = 10.0
        if resG > 10.0:
            resG = 10.0
        if resB > 10.0:
            resB = 10.0
        return rtColour(resR, resG, resB)

    
    
    def multiplyByAnother (self, another):

        anotherRGB = another.getRGB()
        resR = self.sRGB[0] * anotherRGB[0]
        resG = self.sRGB[1] * anotherRGB[1]
        resB = self.sRGB[2] * anotherRGB[2]
        if resR > 10.0:
            resR = 10.0
        if resG > 10.0:
            resG = 10.0
        if resB > 10.0:
            resB = 10.0
        if resR < 0.0:
            resR = 0.0
        if resG < 0.0:
            resG = 0.0
        if resB < 0.0:
            resB = 0.0

        return rtColour(resR, resG, resB)



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
    
