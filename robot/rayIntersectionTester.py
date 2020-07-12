import sys
import math
import json

import rtSphere
from  rtRay import rtRay
from  rtVector import rtVector
import rtIntersection
import rtSphere
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
        transParams = json.loads(sys.argv[4])
        tfac = matrixTransformationFactory.rtMatrixTransformationFactory()
        translation = tfac.newTranslation (transParams[0],\
                                           transParams[1],\
                                           transParams[2])
        
        ray = rtRay()
        ray.setFromArrays(pt, vector)

        newRay = ray.translate(translation)

        res = {'ray': {}}
        res['ray']['origin'] = newRay.origin().getMatrixData()[0]
        res['ray']['direction'] = newRay.direction().getMatrixData()[0]
        print (json.dumps (res))
        
    if sys.argv[1] == 'testRayScaling':

        pt = json.loads(sys.argv[2])
        vector = json.loads(sys.argv[3])
        scalingParams = json.loads(sys.argv[4])
        tfac = matrixTransformationFactory.rtMatrixTransformationFactory()
        scaling = tfac.newScaling (scalingParams[0],\
                                           scalingParams[1],\
                                           scalingParams[2])
        
        ray = rtRay()
        ray.setFromArrays(pt, vector)

        newRay = ray.scale(scaling)

        res = {'ray': {}}
        res['ray']['origin'] = newRay.origin().getMatrixData()[0]
        res['ray']['direction'] = newRay.direction().getMatrixData()[0]
        print (json.dumps (res))
        
    if sys.argv[1] == 'testUnitSphereTransform':

        sphere = rtSphere.rtSphere()
        
        res = {'isIdentity': False}
        res['isIdentity'] = sphere.transform().isIdentity()
        print (json.dumps (res))
        
    if sys.argv[1] == 'testTransformedSphere':

        transformParams = json.loads(sys.argv[2])
        
        sphere = rtSphere.rtSphere()

        tfac = matrixTransformationFactory.rtMatrixTransformationFactory()
        translation = tfac.newTranslation (transformParams[0],\
                                           transformParams[1],\
                                           transformParams[2])
        
        sphere.applyTransform(translation)

        print (json.dumps (sphere.transform().asJSON()))
        
    if sys.argv[1] == 'testIntersectionsWithScaledSphere':

        rayOrigin     = json.loads(sys.argv[2])
        rayDirection  = json.loads(sys.argv[3])
        sphereScaling = json.loads(sys.argv[4])

        ray = rtRay()
        ray.setFromArrays(rayOrigin, rayDirection)
        sphere = rtSphere.rtSphere()
        tfac = matrixTransformationFactory.rtMatrixTransformationFactory()
        scaling = tfac.newScaling (sphereScaling[0],\
                                           sphereScaling[1],\
                                           sphereScaling[2])
        
        sphere.applyTransform (scaling)

        intersections = ray.intersectionsWithSphere (sphere)
        
        print (json.dumps (intersections))
        
    if sys.argv[1] == 'testIntersectionsWithTranslatedSphere':

        rayOrigin     = json.loads(sys.argv[2])
        rayDirection  = json.loads(sys.argv[3])
        sphereTranslation = json.loads(sys.argv[4])

        ray = rtRay()
        ray.setFromArrays(rayOrigin, rayDirection)
        sphere = rtSphere.rtSphere()
        tfac = matrixTransformationFactory.rtMatrixTransformationFactory()
        scaling = tfac.newTranslation (sphereTranslation[0],\
                                           sphereTranslation[1],\
                                           sphereTranslation[2])
        
        sphere.applyTransform (scaling)

        intersections = ray.intersectionsWithSphere (sphere)
        
        print (json.dumps (intersections))

        
    if sys.argv[1] == 'testNormals':

        normalDirection  = json.loads(sys.argv[2])

        sphere = rtSphere.rtSphere()
        normal = sphere.normalAtObjectPoint(normalDirection[0], normalDirection[1], normalDirection[2])

        

        normalData = normal.getMatrixData()

        print (json.dumps({'normal': [normalData[0][0], normalData[0][1], normalData[0][2]]}))

        
    if sys.argv[1] == 'testNormalsWithTranslation':

        normalDirection  = json.loads(sys.argv[2])
        translationData  = json.loads(sys.argv[3])
        tfac = matrixTransformationFactory.rtMatrixTransformationFactory()

        sphere = rtSphere.rtSphere()

        sphere.applyTransform(tfac.newTranslation(translationData[0], translationData[1], translationData[2]))

        normal = sphere.normalAtWorldPoint(normalDirection[0], normalDirection[1], normalDirection[2])

        normalData = normal.getMatrixData()

        print (json.dumps({'normal': [normalData[0][0], normalData[0][1], normalData[0][2]]}))


    if sys.argv[1] == 'testNormalsWithTransform':

        normalDirection  = json.loads(sys.argv[2])
        scalingData  = json.loads(sys.argv[3])
        rotationData  = json.loads(sys.argv[4])
        tfac = matrixTransformationFactory.rtMatrixTransformationFactory()

        scaling = tfac.newScaling(scalingData[0], scalingData[1], scalingData[2])


        rotation = tfac.newRotation('Z', rotationData[2])
        
        transform = scaling.multiplyWithAnother(rotation)

        
        sphere = rtSphere.rtSphere()
        sphere.applyTransform(transform)
        normal = sphere.normalAtWorldPoint(normalDirection[0], normalDirection[1], normalDirection[2])

        
        normalVector = normal.normalise()
        normalData = normalVector.getMatrixData()
        print (json.dumps({'normal': [normalData[0][0], normalData[0][1], normalData[0][2]]}))


    if sys.argv[1] == 'testNormalIsNormalised':

        normalDirection  = json.loads(sys.argv[2])

        sphere = rtSphere.rtSphere()
        normal = sphere.normalAtObjectPoint(normalDirection[0], normalDirection[1], normalDirection[2])

        normalisedVector = normal.normalise()
        areSame = "No"
        if normal.equalToAnother(normalisedVector):
            areSame = "Yes"

        print (json.dumps({'isNormalised': areSame}))

        
