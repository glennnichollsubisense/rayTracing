import sys
import json

import rtRay
import rtPoint  as rtp
import rtVector as rtv
import rtSphere
import rtWorld  as rtworld
import rtShading as rtshading
import material
import colours
import pointLightSource


class shadeTester():

    def __init__(self):
        self.name = 'ShadeTester'
        self.sWorld = None

    def buildWorld(self):

        world = rtworld.rtWorld()

        # Add two spheres, both at the origin
        tMaterial = material.rtMaterial(None, 0.7, 0.2)
        tMaterial.setColour(colours.rtColour(0.8, 1.0, 0.6, 'Lime Green'))

        outerSphere = rtSphere.rtSphere(1.0, None, 'OuterSphere')
        outerSphere.setMaterial (tMaterial)
        
        innerSphere = rtSphere.rtSphere(0.5, None, 'InnerSphere')

        world.addObject(outerSphere)
        world.addObject(innerSphere)

        self.sWorld = world

        return self.sWorld
        

    def getWorld(self):

        return self.sWorld
    
if __name__== "__main__":

    ##  Testing scripts

    tTester = shadeTester()

    if sys.argv[1] == 'testOutsideHit':

        origin    = json.loads(sys.argv[2])
        direction = json.loads(sys.argv[3])

        rtOrigin = rtp.rtPoint(origin[0], origin[1], origin[2])
        rtDirection = rtv.rtVector(direction[0], direction[1], direction[2])

        ray = rtRay.rtRay(rtOrigin, rtDirection)        
        world = tTester.buildWorld()
        world.addDefaultLightSource()
        
        shader = rtshading.rtShading(ray, world)
        
        print (json.dumps({'colour': shader.getShade('OuterSphere').getRGB()}))
    

    elif sys.argv[1] == 'testInsideHit':

        origin    = json.loads(sys.argv[2])
        direction = json.loads(sys.argv[3])

        rtOrigin = rtp.rtPoint(origin[0], origin[1], origin[2])
        rtDirection = rtv.rtVector(direction[0], direction[1], direction[2])

        ray = rtRay.rtRay(rtOrigin, rtDirection)

        world = tTester.buildWorld()

        # make a light source inside the inner sphere
        lightposition = rtp.rtPoint(0.0, 0.25, 0.0)
        lightSource = pointLightSource.PointLightSource(None, lightposition)
        
        world.addLightSource(lightSource)
        
        shader = rtshading.rtShading(ray, world)
        
        print (json.dumps({'colour': shader.getShade('InnerSphere').getRGB()}))
    
    elif sys.argv[1] == 'testDefaultWorldWithVector':

        origin    = json.loads(sys.argv[2])
        direction = json.loads(sys.argv[3])

        rtOrigin = rtp.rtPoint(origin[0], origin[1], origin[2])
        rtDirection = rtv.rtVector(direction[0], direction[1], direction[2])

        ray = rtRay.rtRay(rtOrigin, rtDirection)        
        world = tTester.buildWorld()
        world.addDefaultLightSource()
        
        shader = rtshading.rtShading(ray, world)
        
        print (json.dumps({'colour': shader.getShade('OuterSphere').getRGB()}))

    elif sys.argv[1] == 'testDefaultWorldInsideOuterSphere':

        origin    = json.loads(sys.argv[2])
        direction = json.loads(sys.argv[3])

        rtOrigin = rtp.rtPoint(origin[0], origin[1], origin[2])
        rtDirection = rtv.rtVector(direction[0], direction[1], direction[2])

        ray = rtRay.rtRay(rtOrigin, rtDirection)        
        world = tTester.buildWorld()
        world.addDefaultLightSource()
        
        shader = rtshading.rtShading(ray, world)
        
        print (json.dumps({'colour': shader.getShade('InnerSphere').getRGB()}))

    else:
        print ('unknown option')

        
