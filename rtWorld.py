from rtPoint import rtPoint
from rtVector import rtVector
from rtSphere import rtSphere
from pointLightSource import PointLightSource

class rtWorld(object):

    def __init__(self, pOrigin=None):

        self.sOrigin=rtPoint()
        if pOrigin != None:
            self.sOrigin.setFromAnother (pOrigin)

        self.sObjects=[]
        self.sLightSources=[]

        ptFrom = rtPoint(0, 0, 0)
        ptTo = rtPoint(0, 0, -1)
        vcUp = rtVector (0, 1, 0)

    def getObjects(self):
        return self.sObjects

    def getObjectByName(self, pName):
        for i in self.sObjects:
            if i.sObjectID == pName:
                return i

    def addObject(self, aObject):
        self.sObjects.append(aObject)

    def getLightSources(self):
        return self.sLightSources

    def addLightSource(self, aLightSource):
        self.sLightSources.append(aLightSource)

    def addDefaultLightSource(self):
        aLightSource = PointLightSource(None, rtPoint(-10, -10, -10))
        self.addLightSource(aLightSource)
        

    def showMe(self, name=None):
        if name != None:
            print ('*** %s *** ' % name)
        for i in self.getObjects():
            i.showMe()
        for i in self.getLightSources():
            i.showMe()
        
    
        

        
            
