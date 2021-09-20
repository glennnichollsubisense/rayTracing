import sys
import json

import rtRay
import rtPoint as rtp
import rtVector as rtv
import rtSphere as rtsphere

class  rayTester():

    def __init__(self):
        self.name = 'rayTester'


if __name__== "__main__":

    ##  Testing scripts

    tTester = rayTester()

    if sys.argv[1] == 'testQuery':

        origin    = json.loads(sys.argv[2])
        direction = json.loads(sys.argv[3])

        rtOrigin = rtp.rtPoint(origin[0], origin[1], origin[2])
        rtDirection = rtv.rtVector(direction[0], direction[1], direction[2])

        ray = rtRay.rtRay(rtOrigin, rtDirection)

        res = {}
        res['origin']= ray.origin().getMatrixData()[0]
        res['direction']= ray.direction().getMatrixData()[0]

        print json.dumps(res)

    if sys.argv[1] == 'testPosition':

        origin    = json.loads(sys.argv[2])
        direction = json.loads(sys.argv[3])
        t = json.loads(sys.argv[4])

        rtOrigin = rtp.rtPoint(origin[0], origin[1], origin[2])
        rtDirection = rtv.rtVector(direction[0], direction[1], direction[2])

        ray = rtRay.rtRay(rtOrigin, rtDirection)

        res = {}
        newPosition= ray.position (t)
        res['tpoint'] = newPosition.getMatrixData()[0]

        print json.dumps(res)


    if sys.argv[1] == 'testComputations':

        origin    = json.loads(sys.argv[2])
        direction = json.loads(sys.argv[3])
        t = json.loads(sys.argv[4])

        rtOrigin = rtp.rtPoint(origin[0], origin[1], origin[2])
        rtDirection = rtv.rtVector(direction[0], direction[1], direction[2])

        ray = rtRay.rtRay(rtOrigin, rtDirection)
        
        sphere = rtsphere.rtSphere(1.0, None, 'Billy')

        computations = ray.detailedIntersectionWithShape (sphere, t)

        resComputations = {}
        resComputations['normalv'] = computations['normalv'].asDictionary()
        resComputations['eyev']    = computations['eyev'].asDictionary()
        resComputations['object']    = computations['object'].asDictionary()
        resComputations['t'] = computations['t']
        resComputations['point'] = computations['point'].asDictionary()

        print (json.dumps(resComputations))


    if sys.argv[1] == 'testComputationsInsideOutside':

        origin    = json.loads(sys.argv[2])
        direction = json.loads(sys.argv[3])
        t = json.loads(sys.argv[4])

        rtOrigin = rtp.rtPoint(origin[0], origin[1], origin[2])
        rtDirection = rtv.rtVector(direction[0], direction[1], direction[2])

        ray = rtRay.rtRay(rtOrigin, rtDirection)
        
        sphere = rtsphere.rtSphere(1.0, None, 'Billy')

        computations = ray.detailedIntersectionWithShape (sphere, t)

        resComputations = {}
        resComputations['normalv'] = computations['normalv'].asDictionary()
        resComputations['eyev']    = computations['eyev'].asDictionary()
        resComputations['object']    = computations['object'].asDictionary()
        resComputations['t'] = computations['t']
        resComputations['point'] = computations['point'].asDictionary()
        resComputations['inside'] = computations['inside']

        print (json.dumps(resComputations))
        
