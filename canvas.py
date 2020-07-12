import colours as cl
from rtColourFactory import rtColourFactory

class outOfCanvasBounds(Exception):

    def __init__(self, message):
        super(outOfCanvasBounds, self).__init__(message)


class Canvas():

    def __init__(self, width, height):

        self.canvas = {}
        self.canvas['width'] = width
        self.canvas['height'] = height
        self.canvas['data'] = [0] * height 
        for iheight in range (0, height):
            self.canvas['data'][iheight] = [None] * width


    def height(self):
        return self.canvas['height']
    
    def makeBlackCanvas(self):

        rtf = rtColourFactory()
        for iheight in range (0, self.canvas['height']):
            self.canvas['data'][iheight] = [rtf.newBlack().getRGB()] * self.canvas['width']

        return self.canvas

    def makeWhiteCanvas(self):
 
        for iheight in range (0, self.canvas['height']):
            self.canvas['data'][iheight] = [rtf.newWhite().getRGB()] * self.canvas['width']

        return self.canvas

    def setPixel (self, x, y, colour):

        if (x<0) or (x>=self.canvas['width']):
            raise (outOfCanvasBounds('out of bounds'))
        if (y<0) or (y>=self.canvas['height']):
            raise (outOfCanvasBounds('out of bounds'))
        
        self.canvas['data'][y][x] = colour.getRGB()
        
    def getPixel (self, x, y):

        if (x<0) or (x>=self.canvas['width']):
            raise (outOfCanvasBounds('out of bounds'))
        if (y<0) or (y>=self.canvas['height']):
            raise (outOfCanvasBounds('out of bounds'))

        return self.canvas['data'][y][x]
        

    def showMe(self, short=False):

        print ('Canvas %i x %i ' % (self.canvas['width'], self.canvas['height']))
        
        if short == True:
            return 

        for iheight in range (0, self.canvas['height']):
            for iwidth in range (0, self.canvas['width']):
                print (self.canvas['data'][iheight][iwidth])
            print ('new row \n')


    def saveAs(self, filename):

        fd = open (filename, 'w')

        try:

            fd.write('P3\n')
            fd.write ('%s %s\n' % (str(self.canvas['width']), str(self.canvas['height'])))
            fd.write ('255\n')
    
            counter = 0
            for iheight in range (0, self.canvas['height']):
                for iwidth in range (0, self.canvas['width']):
                    pixel = self.getPixel(iwidth, iheight)
                    pixelString = '%s %s %s ' % ( \
                        str(int(pixel[0] * 255)), \
                        str(int(pixel[1] * 255)), \
                        str(int(pixel[2] * 255)))
                    fd.write (pixelString)
                    counter = counter + 3
                    if counter > 30:
                        fd.write ('\n')
                        counter = 0

            fd.write('\n')                    
            fd.close()
            
        except Exception:
            fd.close()
        

if __name__== "__main__":

    ##  Testing scripts

    print (' ^^^ Testing the canvas') 

    rtf = rtColourFactory()
    cc = Canvas(7, 3)
    cc.makeBlackCanvas()
    cc.showMe()
    cc.setPixel(6, 0, rtf.newRed())
    cc.showMe()

    print (str(cc.getPixel(6, 0)))

    cc = Canvas(64, 40)
    cc.makeBlackCanvas()
    for i in range (0, 40):
        cc.setPixel (31, i, rtf.newYellow() )
        cc.setPixel (37, i, rtf.newGreen() )
        cc.setPixel (41, i, rtf.newYellow() )
        cc.setPixel (43, i, rtf.newRed() )
    
    cc.saveAs ('/home/pi/Projects/rayTracing/outputs/testCanvas.ppm')
