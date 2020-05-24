import sys
import math
import json

import rtVector as rtv
import rtPoint as rtp
import pointsVectors as pv
import matrices as mx
import matrixTransformationFactory as mtFactory

class TransformTester():

    def __init__(self):
        self.name = 'TransformTester'

    
if __name__== "__main__":

    ##  Testing scripts

    tTester = TransformTester()
    mtf = mtFactory.rtMatrixTransformationFactory()

    if sys.argv[1] == 'testTranslate':

        pt = json.loads(sys.argv[2])
        translation = json.loads(sys.argv[3])

        rtPt = rtp.rtPoint(pt[0], pt[1], pt[2])

        testTranslation = mtf.newTranslation (translation[0], translation[1], translation[2])
        print json.dumps(testTranslation.transform(rtPt.transpose()).transpose().matrix['data'])

    if sys.argv[1] == 'testInverseTranslate':

        pt = json.loads(sys.argv[2])
        translation = json.loads(sys.argv[3])

        rtPt = rtp.rtPoint(pt[0], pt[1], pt[2])
        testTranslation = mtf.newTranslation (translation[0], translation[1], translation[2])

        print json.dumps(testTranslation.inverse().transform(rtPt.transpose()).transpose().matrix['data'])

        
    if sys.argv[1] == 'testTranslateVector':

        vec = json.loads(sys.argv[2])
        translation = json.loads(sys.argv[3])

        rtVec = rtv.rtVector(vec[0], vec[1], vec[2])

        testTranslation = mtf.newTranslation (translation[0], translation[1], translation[2])

        print json.dumps(testTranslation.transform(rtVec.transpose()).transpose().matrix['data'])

    if sys.argv[1] == 'testScalePoint':

        pt = json.loads(sys.argv[2])
        scaling = json.loads(sys.argv[3])

        rtPt = rtp.rtPoint(pt[0], pt[1], pt[2])

        testScaling = mtf.newScaling (scaling[0], scaling[1], scaling[2])

        print json.dumps(testScaling.transform(rtPt.transpose()).transpose().matrix['data'])

    if sys.argv[1] == 'testScaleVector':

        vec = json.loads(sys.argv[2])
        scaling = json.loads(sys.argv[3])

        rtVec = rtv.rtVector(vec[0], vec[1], vec[2])

        testScaling = mtf.newScaling (scaling[0], scaling[1], scaling[2])

        print json.dumps(testScaling.transform(rtVec.transpose()).transpose().matrix['data'])

    if sys.argv[1] == 'testInverseScaleVector':

        vec = json.loads(sys.argv[2])
        scaling = json.loads(sys.argv[3])

        rtVec = rtv.rtVector(vec[0], vec[1], vec[2])

        testScaling = mtf.newScaling (scaling[0], scaling[1], scaling[2]).inverse()

        print json.dumps(testScaling.transform(rtVec.transpose()).transpose().matrix['data'])


    if sys.argv[1] == 'testNegativeScalePoint':

        pt = json.loads(sys.argv[2])
        scaling = json.loads(sys.argv[3])

        rtPt = rtp.rtPoint(pt[0], pt[1], pt[2])

        testScaling = mtf.newScaling (scaling[0], scaling[1], scaling[2])

        print json.dumps(testScaling.transform(rtPt.transpose()).transpose().matrix['data'])

    if sys.argv[1] == 'testRotatePoint':

        rotation = sys.argv[2]
        axis = sys.argv[3]
        pt = json.loads(sys.argv[4])

        rtPt = rtp.rtPoint(pt[0], pt[1], pt[2])

        testRotation = None
        if rotation == 'quarter':
            if axis == 'X':
                testRotation = mtf.newRotation ('X', math.pi/2.0)
            if axis == 'Y':
                testRotation = mtf.newRotation ('Y', math.pi/2.0)
            if axis == 'Z':
                testRotation = mtf.newRotation ('Z', math.pi/2.0)
        elif rotation == 'half-quarter':
            if axis == 'X':
                testRotation = mtf.newRotation ('X', math.pi/4.0)
            if axis == 'Y':
                testRotation = mtf.newRotation ('Y', math.pi/4.0)
            if axis == 'Z':
                testRotation = mtf.newRotation ('Z', math.pi/4.0)

        print json.dumps(testRotation.transform(rtPt.transpose()).transpose().matrix['data'])


    if sys.argv[1] == 'testShearPoint':

        shearComponents = json.loads(sys.argv[2])
        pt = json.loads(sys.argv[3])

        rtPt = rtp.rtPoint(pt[0], pt[1], pt[2])
        testShear = mtf.newShearing (shearComponents)

        print json.dumps(testShear.transform(rtPt.transpose()).transpose().matrix['data'])



    if sys.argv[1] == 'testChained':

        pt = json.loads(sys.argv[2])
        rtPt = rtp.rtPoint(pt[0], pt[1], pt[2])

        tr1 = mtf.newRotation('X', math.pi/2.0)
        tr2 = mtf.newScaling(5,5,5)
        tr3 = mtf.newTranslation (10, 5, 7)
        chainedTransform = tr3.transform(tr2).transform(tr1)
        print json.dumps(chainedTransform.transform(rtPt.transpose()).transpose().matrix['data'])
        
    
    if sys.argv[1] == 'testChainedRunTwice':

        pt = json.loads(sys.argv[2])
        rtPt = rtp.rtPoint(pt[0], pt[1], pt[2])

        tr1 = mtf.newRotation('X', math.pi/2.0)
        tr2 = mtf.newScaling(5,5,5)
        tr3 = mtf.newTranslation (10, 5, 7)
        chainedTransform = tr3.transform(tr2).transform(tr1)
        chainedTransform = tr3.transform(tr2).transform(tr1)
        print json.dumps(chainedTransform.transform(rtPt.transpose()).transpose().matrix['data'])
        
    

    

    
