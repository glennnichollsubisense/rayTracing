import rtPoint

class rtPointFactory():

    def __init__(self):
        pass

    def newOriginPoint(self):
        return rtPoint.rtPoint()
    
    def newPoint(self, x=0, y=0, z=0):
        return rtPoint.rtPoint(x, y, z)
    
    
