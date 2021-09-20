import json
import rtSphere

class rtIntersection(object):

    def __init__(self, pTValue=0.0, pObject=None, pID=1):

        self.sTValue = pTValue
        self.sObject = pObject
        self.sID = pID


    def initFromJSON(self, pJSON):

        proto = json.loads(pJSON)
        self.sID=proto['id']
        self.sTValue = proto['tvalue']
        if proto['object'] == 'unitSphere':
            self.sObject = rtSphere.rtSphere()

        
    def tValue(self):
        return self.sTValue
        
    def object(self):
        return self.sObject

    def intersectionID(self):
        return self.sID

    def asDictionary(self):

        res = {'id': self.intersectionID(), 'object': self.object().asText(), 'tvalue': self.tValue()}
        return res

        
    def showMe(self):
        print ('id %s' % str(self.sID))
        print ('object %s' % str(self.sObject))
        print ('tvalue %s' % str(self.sTValue))


class rtIntersectionSet(object):

    def __init__(self, intersections=[]):

        self.sIntersections=[]
        for i in intersections:
            self.sIntersections.append(i)


    def noOfIntersections(self):
        return len(self.sIntersections)


    def intersectionSet(self):
        return self.sIntersections

    def addIntersection(self, pIntersection):
        self.sIntersections.append(pIntersection)

    def clearIntersections(self):
        self.sIntersections=[]

        
    def showMe(self):
        print ('rtIntersectionSet: %s ' % str(self.noOfIntersections()))
        for i in self.intersectionSet():
            i.showMe()

    def hit(self):

        # i had this as integers initially but that cannot be right
        interID = None
        interTValue = 1000000000.0
        for iInter in self.sIntersections:
            if (float(iInter.tValue()) < float(interTValue)) and (float(iInter.tValue())>0.0):
                interTValue = float(iInter.tValue())
                interID = iInter.intersectionID()

        return {'hit': interID, 'tvalue': interTValue}

    
