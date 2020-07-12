import sys
import math
import json

import rtSphere
from  rtRay import rtRay
from  rtVector import rtVector
from  rtPoint import rtPoint
import rtIntersection
import rtSphere
import matrixTransformationFactory
import colours
from rtColourFactory import rtColourFactory
import pointLightSource
import rtLighting
import material

if __name__== "__main__":

    ##  Testing scripts


    if sys.argv[1] == 'testReflect':

        vectorValues1 = json.loads(sys.argv[2])
        vectorValues2 = json.loads(sys.argv[3])

        vector1 = rtVector(vectorValues1[0], vectorValues1[1], vectorValues1[2])
        vector2 = rtVector(vectorValues2[0], vectorValues2[1], vectorValues2[2])
        reflectedVector = vector1.reflectWithAnother(vector2)

        res = {'reflection': reflectedVector.getMatrixData()}
        print (json.dumps(res))

    elif sys.argv[1] == 'testLightSource':

        colourValues1 = json.loads(sys.argv[2])
        positionValues1 = json.loads(sys.argv[3])

        position1   = rtPoint(positionValues1[0], positionValues1[1], positionValues1[2])
        colour1  = colours.rtColour(colourValues1[0], colourValues1[1], colourValues1[2])

        lightSource = pointLightSource.PointLightSource(colour1, position1)
        res = {'position': lightSource.getPoint().getMatrixData()}
        res['colour'] = lightSource.getColour().getRGB()

        print (json.dumps(res))

    elif sys.argv[1] == 'testMaterial':

        colourValues1 = json.loads(sys.argv[2])
        ambient   = sys.argv[3]
        diffuse   = sys.argv[4]
        specular  = sys.argv[5]
        shininess = sys.argv[6]

        colour1  = colours.rtColour(colourValues1[0], colourValues1[1], colourValues1[2])

        material1 = material.rtMaterial(None, diffuse, specular, shininess, ambient)
        material1.setColour(colour1)

        res = {'ambient': material1.getAmbient()}
        res['diffuse'] = material1.getDiffuse()
        res['specular'] = material1.getSpecular()
        res['shininess'] = material1.getShininess()
        res['colour'] = material1.getColour().getRGB()

        print (json.dumps(res))

    elif sys.argv[1] == 'testMaterialonSphere':


        tSphere = rtSphere.rtSphere()
        material1 = tSphere.getMaterial()
        
        res = {'ambient': material1.getAmbient()}
        res['diffuse'] = material1.getDiffuse()
        res['specular'] = material1.getSpecular()
        res['shininess'] = material1.getShininess()
        res['colour'] = material1.getColour().getRGB()

        print (json.dumps(res))

    elif sys.argv[1] == 'testMaterialonSphere2':

        materialType = sys.argv[2]


        tSphere = rtSphere.rtSphere()

        if materialType == 'grass':
            grass1 = material.rtMaterial()
            grass1.setGrassValues()
            tSphere.setMaterial(grass1)

        material1 = tSphere.getMaterial()
        
        res = {'ambient': material1.getAmbient()}
        res['diffuse'] = material1.getDiffuse()
        res['specular'] = material1.getSpecular()
        res['shininess'] = material1.getShininess()
        res['colour'] = material1.getColour().getRGB()

        print (json.dumps(res))

    elif sys.argv[1] == 'testEyeAtZero':

        material1 = material.rtMaterial()
        material1.setDefaultValues()
        material1.sAmbient = 0.1
        position1 = rtPoint()
        eyeVector = rtVector(0, 0, -1)
        normalVector = rtVector(0, 0, -1)
        lightPoint = rtPoint(0, 0, -10)
        rtf = rtColourFactory()
        lightSource = pointLightSource.PointLightSource(None, lightPoint)
        lightSource.setColour(rtf.newWhite())

        res = rtLighting.rtLighting(material1, lightSource, position1, eyeVector, normalVector)

        print (json.dumps(res.getColour()))
        

    elif sys.argv[1] == 'testEyeAt45':

        root2over2 = 0.707106781
#        root2over2 = sqrt(2.0) / 2.0
        material1 = material.rtMaterial()
        material1.setDefaultValues()
        position1 = rtPoint()
        eyeVector = rtVector(0, root2over2, root2over2*-1)
        normalVector = rtVector(0, 0, -1)
        lightPoint = rtPoint(0, 0, -10)
        lightSource = pointLightSource.PointLightSource(None, lightPoint)

        res = rtLighting.rtLighting(material1, lightSource, position1, eyeVector, normalVector)

        print (json.dumps(res.getColour()))
        


    elif sys.argv[1] == 'testLightAt45':

        material1 = material.rtMaterial()
        material1.setDefaultValues()
        position1 = rtPoint()
        eyeVector = rtVector(0, 0, -1)
        normalVector = rtVector(0, 0, -1)
        lightPoint = rtPoint(0, 10, -10)
        lightSource = pointLightSource.PointLightSource(None, lightPoint)

        res = rtLighting.rtLighting(material1, lightSource, position1, eyeVector, normalVector)

        print (json.dumps(res.getColour()))
        

    elif sys.argv[1] == 'testLightAndEyeAt45':

        minroot2over2 = -0.707106781
        material1 = material.rtMaterial()
        material1.setDefaultValues()
        position1 = rtPoint()
        eyeVector = rtVector(0, minroot2over2, minroot2over2)
        normalVector = rtVector(0, 0, -1)
        lightPoint = rtPoint(0, 10, -10)
        lightSource = pointLightSource.PointLightSource(None, lightPoint)

        res = rtLighting.rtLighting(material1, lightSource, position1, eyeVector, normalVector)

        print (json.dumps(res.getColour()))
        

    elif sys.argv[1] == 'testLightBehind':

        material1 = material.rtMaterial()
        material1.setDefaultValues()
        position1 = rtPoint()
        eyeVector = rtVector(0, 0, -1)
        normalVector = rtVector(0, 0, -1)
        lightPoint = rtPoint(0, 0, 10)
        lightSource = pointLightSource.PointLightSource(None, lightPoint)

        res = rtLighting.rtLighting(material1, lightSource, position1, eyeVector, normalVector)

        print (json.dumps(res.getColour()))
        


    else:

        print ('bad argument')
        
