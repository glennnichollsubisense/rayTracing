import sys
import math
import json

import rtSphere
from  rtRay import rtRay
import rtIntersection
import matrixTransformationFactory


class RayIntersectionTester():

    def __init__(self):
        self.name = 'RayIntersectionTester'
    
if __name__== "__main__":

    ##  Testing scripts

    tTester = RayIntersectionTester()


    if sys.argv[1] == 'testIntersect1':

        pt = json.loads(sys.argv[2])
        vector = json.loads(sys.argv[3])

        ray = rtRay()
        ray.setFromArrays(pt, vector)

        sphere = sys.argv[4]

        tSphere = None
        if sphere == 'unitSphere':
            tSphere = rtSphere.rtSphere()
        else:
            tSphere = rtSphere.rtSphere(sphere)

        intersections = ray.intersectionsWithSphere(tSphere)
        res={'intersections': {}}

        if len(intersections) > 0:
            res['intersections']['near'] = intersections[0]
            res['intersections']['far'] = intersections[1]
        print (json.dumps(res))

    if sys.argv[1] == 'testIntersectionClass':

        tvalue = sys.argv[2]
        sphere = sys.argv[3]

        tSphere = None
        if sphere == 'unitSphere':
            tSphere = rtSphere.rtSphere()
        else:
            tSphere = rtSphere.rtSphere(sphere)

            
        intersection = rtIntersection.rtIntersection(tvalue, tSphere)
        
        res={'intersections': []}

        tIntersection = {}
        tIntersection['tvalue'] = intersection.tValue()
        tIntersection['object'] = intersection.object().asText()
        res['intersections'].append(tIntersection)

        print (json.dumps(res))

    if sys.argv[1] == 'testIntersectionSetClass':

        tvalue1 = sys.argv[2]
        tvalue2 = sys.argv[3]
        sphere = sys.argv[4]

        tSphere = None
        if sphere == 'unitSphere':
            tSphere = rtSphere.rtSphere()
        else:
            tSphere = rtSphere.rtSphere(sphere)

            
        intersection1 = rtIntersection.rtIntersection(tvalue1, tSphere)
        intersection2 = rtIntersection.rtIntersection(tvalue2, tSphere)

        iset = rtIntersection.rtIntersectionSet([intersection1, intersection2])
        res={'intersections': []}

        for i in iset.intersectionSet():
            res['intersections'].append ({'tvalue': i.tValue(), 'object': i.object().asText()})

        print (json.dumps(res))


    if sys.argv[1] == 'createIntersection':

        tValue = sys.argv[2]
        sphere = sys.argv[3]
        id = sys.argv[4]

        anInter = rtIntersection.rtIntersection()
        anInter.initFromJSON(json.dumps({'id': id, 'object': sphere, 'tvalue': tValue}))
        
        print (json.dumps (anInter.asDictionary()))

    if sys.argv[1] == 'testIntersectionSetHit1':

        iset = rtIntersection.rtIntersectionSet()
        
        anInter = rtIntersection.rtIntersection()
        anInter.initFromJSON('{"tvalue": "2", "object": "unitSphere", "id": "2"}')
        iset.addIntersection (anInter)
        anInter = rtIntersection.rtIntersection()
        anInter.initFromJSON('{"tvalue": "1", "object": "unitSphere", "id": "1"}')
        iset.addIntersection (anInter)

        print (json.dumps (iset.hit()))

    if sys.argv[1] == 'testIntersectionSetHit2':

        iset = rtIntersection.rtIntersectionSet()
        
        anInter = rtIntersection.rtIntersection()
        anInter.initFromJSON('{"tvalue": "-1", "object": "unitSphere", "id": "2"}')
        iset.addIntersection (anInter)
        anInter = rtIntersection.rtIntersection()
        anInter.initFromJSON('{"tvalue": "1", "object": "unitSphere", "id": "1"}')
        iset.addIntersection (anInter)

        print (json.dumps (iset.hit()))
        
    if sys.argv[1] == 'testIntersectionSetHit3':

        iset = rtIntersection.rtIntersectionSet()
        
        anInter = rtIntersection.rtIntersection()
        anInter.initFromJSON('{"tvalue": "-1", "object": "unitSphere", "id": "2"}')
        iset.addIntersection (anInter)
        anInter = rtIntersection.rtIntersection()
        anInter.initFromJSON('{"tvalue": "-2", "object": "unitSphere", "id": "1"}')
        iset.addIntersection (anInter)

        print (json.dumps (iset.hit()))
        
    if sys.argv[1] == 'testIntersectionSetHit4':

        iset = rtIntersection.rtIntersectionSet()
        
        anInter = rtIntersection.rtIntersection()
        anInter.initFromJSON('{"tvalue": "5", "object": "unitSphere", "id": "1"}')
        iset.addIntersection (anInter)
        anInter = rtIntersection.rtIntersection()
        anInter.initFromJSON('{"tvalue": "7", "object": "unitSphere", "id": "2"}')
        iset.addIntersection (anInter)
        anInter = rtIntersection.rtIntersection()
        anInter.initFromJSON('{"tvalue": "-3", "object": "unitSphere", "id": "3"}')
        iset.addIntersection (anInter)
        anInter = rtIntersection.rtIntersection()
        anInter.initFromJSON('{"tvalue": "2", "object": "unitSphere", "id": "4"}')
        iset.addIntersection (anInter)

        print (json.dumps (iset.hit()))
        
    if sys.argv[1] == 'testRayTranslation':

        pt = json.loads(sys.argv[2])
        vector = json.loads(sys.argv[3])
        transParams = json.loads(sys.argv[3])
        tfac = matrixTransformationFactory.rtMatrixTransformationFactory()
        translation = tfac.newTranslation (transParams[0],\
                                           transParams[1],\
                                           transParams[2])
        
        ray = rtRay()
        ray.setFromArrays(pt, vector)

        ray.showMe()
        newRay = ray.translate(translation)

        print ('^^^ %s' % str(newRay))
        newRay.showMe()
        

        print (json.dumps ([newRay.origin().matrix['data'], newRay.direction().matrix['data']]))
        
