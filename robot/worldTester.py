import sys
import json
import rtWorld
import material
import colours
import rtSphere
import rtRay
import matrixTransformationFactory

class worldTester():

    def __init__(self):
        self.name = 'worldTester'

if __name__ == "__main__":

    tTester = worldTester()
    if sys.argv[1] == 'testEmptyWorld':
        tWorld = rtWorld.rtWorld()
        res = {}
        res['objects'] = tWorld.getObjects()
        res['lightsources'] = tWorld.getLightSources()
        print json.dumps(res)

    if sys.argv[1] == 'testTwoSpheres':

        # Make a world and give it a default light source
        tWorld = rtWorld.rtWorld()
        tWorld.addDefaultLightSource()

        # Add two spheres, both at the origin
        tMaterial = material.rtMaterial(None, 0.7, 0.2)
        tMaterial.setColour(colours.rtColour(0.8, 1.0, 0.6, 'Lime Green'))

        outerSphere = rtSphere.rtSphere(1.0, None, 'OuterSphere')
        outerSphere.setMaterial (tMaterial)
        
        innerSphere = rtSphere.rtSphere(0.5, None, 'InnerSphere')

        tWorld.addObject(innerSphere)
        tWorld.addObject(outerSphere)

        res = {}
        res['noofobjects'] = len(tWorld.getObjects())
        res['nooflightsources'] = len(tWorld.getLightSources())
        print json.dumps(res)
        
    if sys.argv[1] == 'testTwoSpheresAndRay':

        # Make a world and give it a default light source
        tWorld = rtWorld.rtWorld()
        tWorld.addDefaultLightSource()

        # Add two spheres, both at the origin
        tMaterial = material.rtMaterial(None, 0.7, 0.2)
        tMaterial.setColour(colours.rtColour(0.8, 1.0, 0.6, 'Lime Green'))

        outerSphere = rtSphere.rtSphere(1.0, None, 'OuterSphere')
        outerSphere.setMaterial (tMaterial)
        
        innerSphere = rtSphere.rtSphere(0.5, None, 'InnerSphere')

        tWorld.addObject(innerSphere)
        tWorld.addObject(outerSphere)


        tRay = rtRay.rtRay()
        tRay.setFromArrays ([0, 0, -5], [0, 0, 1])

        res = {'intersections': tRay.intersectionsWithWorld(tWorld)}
        print json.dumps(res)
        
        
        
