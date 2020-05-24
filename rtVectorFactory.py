import rtVector

def rtVectorFactory():

    def __init__(self):
        pass


    def newVector(self, x, y, z):
        return rtVector(x,y,z)

    def newUnitVector(self):
        return rtVector(1, 1, 1)

    def newNullVector(self):
        return rtVector(0, 0, 0)
