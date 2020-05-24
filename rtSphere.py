import math

import rtPoint
from   rtPointFactory import rtPointFactory

class rtSphere(object):

    def __init__(self, pRadius=1.0, pOrigin=None, pID='1'):

        if pOrigin == None:
            tfac = rtPointFactory()
            self.sOrigin = tfac.newOriginPoint()
        else:            
            self.sOrigin = pOrigin

        self.sRadius = pRadius
        self.sObjectID = pID

    def origin(self):
        return self.sOrigin
        
    def radius(self):
        return self.sRadius

    def asText(self):
        return 'Sphere %s' % str(self.sObjectID)
    
    def showMe(self):
        print ('origin %s' % str(self.sOrigin.matrix['data']))
        print ('radius %s' % str(self.sRadius))
