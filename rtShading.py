import colours
import rtColourFactory
import rtLighting


class rtShading(object):

    def __init__(self, pRay=None, pWorld=None):
        self.sRay = pRay
        self.sWorld = pWorld

    def setRay(self, pRay):
        self.sRay = pRay

    def setWorld(self, pWorld):
        self.sWorld = pWorld

    def getShade(self, pObjectID=None):


        def getColourFromInteraction(tObject):
            interaction = self.sRay.detailedIntersectionWithShape (tObject, None)
            if interaction == {}:
                return {'found': False, 'colour': rtColourFactory.rtColourFactory().newBlack()}

            aLighting = rtLighting.rtLighting(tObject.getMaterial(), self.sWorld.getLightSources()[0], interaction['point'], interaction['eyev'], interaction['normalv'])
        
            # GNGN is this the best way to return this colour ??
            pixelColour = aLighting.getColour()['colour']
            return {'found': True, 'colour': colours.rtColour(pixelColour[0], pixelColour[1], pixelColour[2])}

            
        tObject = None
        if pObjectID != None:
            tObject = self.sWorld.getObjectByName(pObjectID)
            return getColourFromInteraction(tObject)['colour']
        else:
            for iObject in self.sWorld.getObjects():
                res = getColourFromInteraction(iObject)
                if res['found'] == True:
                    return res['colour']
                
        return rtColourFactory.rtColourFactory().newBlack()

    
    def showMe(self):

        if self.sRay != None:
            self.sRay.showMe('the ray')
        if self.sWorld != None:
            self.sWorld.showMe('the world')


