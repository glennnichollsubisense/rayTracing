from matrixTransformationFactory import rtMatrixTransformationFactory
from rtPoint import rtPoint
from rtRay import rtRay
from rtSphere import rtSphere
from rtVector import rtVector

import canvas as cv
import colours as cl
from rtColourFactory import rtColourFactory


import cProfile

class sceneCreator(object):

    def runIt(self):
        ##  Testing scripts

        backPanelWidth = 200
        backPanelHeight = 200
        
        aCanvas = cv.Canvas(backPanelWidth, backPanelHeight)
        aCanvas.showMe(True)
        aCanvas.makeBlackCanvas()
        
        aSphere = rtSphere()
        tfac = rtMatrixTransformationFactory()
        aScaling = tfac.newScaling(50, 50, 50)
        aSphere.applyTransform(aScaling)

        rayOrigin = rtPoint(0, 0, -100)

        startX = int((backPanelWidth/2) * -1.0)
        endX   = int((backPanelWidth/2))
        startY = int((backPanelHeight/2) * -1.0)
        endY   = int((backPanelHeight/2))
        
        xOffset = int(backPanelWidth/2)
        yOffset = int(backPanelHeight/2)

        rtf = rtColourFactory()
        for ix in range (startX, endX):
            for iy in range (startY, endY):

                if ix==iy:
                    print ('%s-%s' % (str(ix), str(iy)))
                
                rayVector = rtVector (ix - rayOrigin.getMatrixData()[0][0], \
                                      iy - rayOrigin.getMatrixData()[0][1], \
                                      50 - rayOrigin.getMatrixData()[0][2]
                )
                tRay = rtRay(rayOrigin, rayVector)
                intersections = tRay.intersectionsWithSphere(aSphere)
                if len(intersections) >0:
                    try:
                        aCanvas.setPixel (ix + xOffset, iy + yOffset, rtf.newGreen())
                    except cv.outOfCanvasBounds:
                        # print ('%s,%s out of bounds' % (str(ix), str(iy)))
                        pass

                    
        aCanvas.saveAs ('/home/pi/Projects/rayTracing-git/rayTracing/outputs/ch5FlatGreenSphere.ppm')

if __name__== "__main__":


    aSceneCreator = sceneCreator()
    aSceneCreator.runIt()
#    cProfile.run ('aSceneCreator.runIt()')

    


