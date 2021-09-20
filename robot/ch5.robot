*** Settings ***
| Library | Process
| Library | Collections
| Library | json

*** Test Cases ***
| Test 1 - Test the basic construction and query
| | ${result}= | run process | python | ./rayTester.py | testQuery | [1, 2, 3] | [4, 5, 6]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${resultOrigin}= | Get From Dictionary | ${json} | origin
| | ${resultX}= | Collections.Get From List | ${resultOrigin} | 0
| | Should be equal as numbers | ${resultX} | 1.0
| | ${resultY}= | Collections.Get From List | ${resultOrigin} | 1
| | Should be equal as numbers | ${resultY} | 2.0
| | ${resultZ}= | Collections.Get From List | ${resultOrigin} | 2
| | Should be equal as numbers | ${resultZ} | 3.0
| | ${resultDirection}= | Get From Dictionary | ${json} | direction
| | ${resultX}= | Collections.Get From List | ${resultDirection} | 0
| | Should be equal as numbers | ${resultX} | 4.0
| | ${resultY}= | Collections.Get From List | ${resultDirection} | 1
| | Should be equal as numbers | ${resultY} | 5.0
| | ${resultZ}= | Collections.Get From List | ${resultDirection} | 2
| | Should be equal as numbers | ${resultZ} | 6.0

| Test 2a - Test the position r(0)
| | ${result}= | run process | python | ./rayTester.py | testPosition | [2, 3, 4] | [1, 0, 0] | 0
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${resultOrigin}= | Get From Dictionary | ${json} | tpoint
| | ${resultX}= | Collections.Get From List | ${resultOrigin} | 0
| | Should be equal as numbers | ${resultX} | 2.0
| | ${resultY}= | Collections.Get From List | ${resultOrigin} | 1
| | Should be equal as numbers | ${resultY} | 3.0
| | ${resultZ}= | Collections.Get From List | ${resultOrigin} | 2
| | Should be equal as numbers | ${resultZ} | 4.0

| Test 2b - Test the position r(1)
| | ${result}= | run process | python | ./rayTester.py | testPosition | [2, 3, 4] | [1, 0, 0] | 1
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${resultOrigin}= | Get From Dictionary | ${json} | tpoint
| | ${resultX}= | Collections.Get From List | ${resultOrigin} | 0
| | Should be equal as numbers | ${resultX} | 3.0
| | ${resultY}= | Collections.Get From List | ${resultOrigin} | 1
| | Should be equal as numbers | ${resultY} | 3.0
| | ${resultZ}= | Collections.Get From List | ${resultOrigin} | 2
| | Should be equal as numbers | ${resultZ} | 4.0

| Test 2c - Test the position r(-1)
| | ${result}= | run process | python | ./rayTester.py | testPosition | [2, 3, 4] | [1, 0, 0] | -1
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${resultOrigin}= | Get From Dictionary | ${json} | tpoint
| | ${resultX}= | Collections.Get From List | ${resultOrigin} | 0
| | Should be equal as numbers | ${resultX} | 1.0
| | ${resultY}= | Collections.Get From List | ${resultOrigin} | 1
| | Should be equal as numbers | ${resultY} | 3.0
| | ${resultZ}= | Collections.Get From List | ${resultOrigin} | 2
| | Should be equal as numbers | ${resultZ} | 4.0

| Test 2d - Test the position r(2.5)
| | ${result}= | run process | python | ./rayTester.py | testPosition | [2, 3, 4] | [1, 0, 0] | 2.5
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${resultOrigin}= | Get From Dictionary | ${json} | tpoint
| | ${resultX}= | Collections.Get From List | ${resultOrigin} | 0
| | Should be equal as numbers | ${resultX} | 4.5
| | ${resultY}= | Collections.Get From List | ${resultOrigin} | 1
| | Should be equal as numbers | ${resultY} | 3.0
| | ${resultZ}= | Collections.Get From List | ${resultOrigin} | 2
| | Should be equal as numbers | ${resultZ} | 4.0

| Test 3 - Test the detailed computations we get back from interacting with a sphere
| | ${result}= | run process | python | ./rayTester.py | testComputations | [0, 0, -5] | [0, 0, 1] | 4
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${respoint}= | Get From Dictionary | ${json} | point
| | ${resnormalv}= | Get From Dictionary | ${json} | normalv
| | ${resobject}= | Get From Dictionary | ${json} | object
| | ${restvalue}= | Get From Dictionary | ${json} | t
| | ${reseyev}= | Get From Dictionary | ${json} | eyev
| | ${pointelement}= | Get From Dictionary | ${respoint} | Point
| | ${pointelementX}= | Get From List | ${pointelement} | 0
| | ${pointelementY}= | Get From List | ${pointelement} | 1
| | ${pointelementZ}= | Get From List | ${pointelement} | 2
| | Should be equal as numbers | ${pointelementX} | 0.0
| | Should be equal as numbers | ${pointelementY} | 0.0
| | Should be equal as numbers | ${pointelementZ} | -1.0
| | ${eyeelement}= | Get From Dictionary | ${reseyev} | Vector
| | ${eyeelementX}= | Get From List | ${eyeelement} | 0
| | ${eyeelementY}= | Get From List | ${eyeelement} | 1
| | ${eyeelementZ}= | Get From List | ${eyeelement} | 2
| | Should be equal as numbers | ${eyeelementX} | 0.0
| | Should be equal as numbers | ${eyeelementY} | 0.0
| | Should be equal as numbers | ${eyeelementZ} | 1.0
| | ${normalelement}= | Get From Dictionary | ${resnormalv} | Vector
| | ${normalelementX}= | Get From List | ${normalelement} | 0
| | ${normalelementY}= | Get From List | ${normalelement} | 1
| | ${normalelementZ}= | Get From List | ${normalelement} | 2
| | Should be equal as numbers | ${normalelementX} | 0.0
| | Should be equal as numbers | ${normalelementY} | 0.0
| | Should be equal as numbers | ${normalelementZ} | -1.0
| | ${objectelement}= | Get From Dictionary | ${resobject} | Sphere
| | ${sphereid}= | Get From Dictionary | ${objectelement} | id
| | Should be equal as strings | ${sphereid} | Billy
| | ${tvalue}= | Get From Dictionary | ${restvalue} | tvalue
| | Should be equal as numbers | ${tvalue} | 4


| Test 4 - Test the detailed computations showing as being outside the sphere
| | ${result}= | run process | python | ./rayTester.py | testComputationsInsideOutside | [0, 0, -5] | [0, 0, 1] | 4
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${resinside}= | Get From Dictionary | ${json} | inside
| | Should be equal as strings | ${resinside} | False

| Test 5 - Test the detailed computations showing as being inside the sphere
| | ${result}= | run process | python | ./rayTester.py | testComputationsInsideOutside | [0, 0, 0] | [0, 0, 1] | 4
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${resinside}= | Get From Dictionary | ${json} | inside
| | Should be equal as strings | ${resinside} | True

| Test the intersect where the ray is in front of the sphere
| | ${result}= | run process | python | ./rayIntersectionTester.py | testIntersect1 | [0, 0, -5] | [0, 0, 1] | unitSphere
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${intersections}= | Get From Dictionary | ${json} | intersections
| | ${near}= | Get From Dictionary | ${intersections} | near
| | ${far}= | Get From Dictionary | ${intersections} | far
| | Should be equal as numbers | ${near} | 4.0
| | Should be equal as numbers | ${far} | 6.0

| Test the intersect where the ray touches at a tangent
| | ${result}= | run process | python | ./rayIntersectionTester.py | testIntersect1 | [0, 1, -5] | [0, 0, 1] | unitSphere
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${intersections}= | Get From Dictionary | ${json} | intersections
| | ${near}= | Get From Dictionary | ${intersections} | near
| | ${far}= | Get From Dictionary | ${intersections} | far
| | Should be equal as numbers | ${near} | 5.0
| | Should be equal as numbers | ${far} | 5.0

| Test the intersect where the ray misses completely
| | ${result}= | run process | python | ./rayIntersectionTester.py | testIntersect1 | [0, 2, -5] | [0, 0, 1] | unitSphere
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${intersections}= | Get From Dictionary | ${json} | intersections
| | ${length}= | Get Length | ${intersections}
| | Should be equal as numbers | ${length} | 0

| Test the intersect where the ray originates inside the sphere
| | ${result}= | run process | python | ./rayIntersectionTester.py | testIntersect1 | [0, 0, 0] | [0, 0, 1] | unitSphere
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${intersections}= | Get From Dictionary | ${json} | intersections
| | ${near}= | Get From Dictionary | ${intersections} | near
| | ${far}= | Get From Dictionary | ${intersections} | far
| | Should be equal as numbers | ${near} | -1.0
| | Should be equal as numbers | ${far} | 1.0

| Test the intersect where the ray originates behind the sphere
| | ${result}= | run process | python | ./rayIntersectionTester.py | testIntersect1 | [0, 0, 5] | [0, 0, 1] | unitSphere
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${intersections}= | Get From Dictionary | ${json} | intersections
| | ${near}= | Get From Dictionary | ${intersections} | near
| | ${far}= | Get From Dictionary | ${intersections} | far
| | Should be equal as numbers | ${near} | -6.0
| | Should be equal as numbers | ${far} | -4.0

| Test the rtIntersection class creation and reference
| | ${result}= | run process | python | ./rayIntersectionTester.py | testIntersectionClass | 3.5 | unitSphere
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${intersections}= | Get From Dictionary | ${json} | intersections
| | ${length}= | Get Length | ${intersections}
| | Should be equal as numbers | ${length} | 1
| | ${theintersection}= | Get From List | ${intersections} | 0
| | ${tvalue}= | Get From Dictionary | ${theintersection} | tvalue
| | Should be equal as numbers | ${tvalue} | 3.5
| | ${tvalue}= | Get From Dictionary | ${theintersection} | object
| | Should be equal as strings | ${tvalue} | Sphere 1

| Test the rtIntersectionSet class creation and reference
| | ${result}= | run process | python | ./rayIntersectionTester.py | testIntersectionSetClass | 1 | 2 | unitSphere
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${intersections}= | Get From Dictionary | ${json} | intersections
| | ${length}= | Get Length | ${intersections}
| | Should be equal as numbers | ${length} | 2
| | ${theintersection}= | Get From List | ${intersections} | 0
| | ${tvalue}= | Get From Dictionary | ${theintersection} | tvalue
| | Should be equal as numbers | ${tvalue} | 1
| | ${object}= | Get From Dictionary | ${theintersection} | object
| | Should be equal as strings | ${object} |  Sphere 1
| | ${theintersection}= | Get From List | ${intersections} | 1
| | ${tvalue}= | Get From Dictionary | ${theintersection} | tvalue
| | Should be equal as numbers | ${tvalue} | 2
| | ${object}= | Get From Dictionary | ${theintersection} | object
| | Should be equal as strings | ${object} | Sphere 1

| Test the rtIntersectionSet class for hits where both tvalues are positive
| | ${result}= | run process | python | ./rayIntersectionTester.py | testIntersectionSetHit1
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${hit}= | Get From Dictionary | ${json} | hit
| | Should be equal as strings | ${hit} | 1

| Test the rtIntersectionSet class for hits where one tvalue is positive and one negative
| | ${result}= | run process | python | ./rayIntersectionTester.py | testIntersectionSetHit2
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${hit}= | Get From Dictionary | ${json} | hit
| | Should be equal as strings | ${hit} | 1

| Test the rtIntersectionSet class for hits where both tvalues are negative
| | ${result}= | run process | python | ./rayIntersectionTester.py | testIntersectionSetHit3
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${hit}= | Get From Dictionary | ${json} | hit
| | Should be equal as strings | ${hit} | None

| Test the rtIntersectionSet class for hits with several values, some + and some -
| | ${result}= | run process | python | ./rayIntersectionTester.py | testIntersectionSetHit4
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${hit}= | Get From Dictionary | ${json} | hit
| | Should be equal as strings | ${hit} | 4

| Test transforming a ray - translation
| | ${result}= | run process | python | ./rayIntersectionTester.py | testRayTranslation | [1,2,3] | [0,1,0] | [3,4,5]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${ray}= | Get From Dictionary | ${json} | ray
| | ${origin}= | Get From Dictionary | ${ray} | origin
| | ${direction}= | Get From Dictionary | ${ray} | direction
| | ${resultX}= | Collections.Get From List | ${origin} | 0
| | Should be equal as numbers | ${resultX} | 4.0
| | ${resultY}= | Collections.Get From List | ${origin} | 1
| | Should be equal as numbers | ${resultY} | 6.0
| | ${resultZ}= | Collections.Get From List | ${origin} | 2
| | Should be equal as numbers | ${resultZ} | 8.0
| | ${resultX}= | Collections.Get From List | ${direction} | 0
| | Should be equal as numbers | ${resultX} | 0.0
| | ${resultY}= | Collections.Get From List | ${direction} | 1
| | Should be equal as numbers | ${resultY} | 1.0
| | ${resultZ}= | Collections.Get From List | ${direction} | 2
| | Should be equal as numbers | ${resultZ} | 0.0

| Test transforming a ray - scaling
| | ${result}= | run process | python | ./rayIntersectionTester.py | testRayScaling | [1,2,3] | [0,1,0] | [2,3,4]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${ray}= | Get From Dictionary | ${json} | ray
| | ${origin}= | Get From Dictionary | ${ray} | origin
| | ${direction}= | Get From Dictionary | ${ray} | direction
| | ${resultX}= | Collections.Get From List | ${origin} | 0
| | Should be equal as numbers | ${resultX} | 2.0
| | ${resultY}= | Collections.Get From List | ${origin} | 1
| | Should be equal as numbers | ${resultY} | 6.0
| | ${resultZ}= | Collections.Get From List | ${origin} | 2
| | Should be equal as numbers | ${resultZ} | 12.0
| | ${resultX}= | Collections.Get From List | ${direction} | 0
| | Should be equal as numbers | ${resultX} | 0.0
| | ${resultY}= | Collections.Get From List | ${direction} | 1
| | Should be equal as numbers | ${resultY} | 3.0
| | ${resultZ}= | Collections.Get From List | ${direction} | 2
| | Should be equal as numbers | ${resultZ} | 0.0

| Check a default sphere's transform is the identity transform 
| | ${result}= | run process | python | ./rayIntersectionTester.py | testUnitSphereTransform
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${isIdentity}= | Get From Dictionary | ${json} | isIdentity
| | Should be equal as strings | ${isIdentity} | True

| Start with a default sphere and translate it - checks its transform is the translation transform we started with
| | ${result}= | run process | python | ./rayIntersectionTester.py | testTransformedSphere | [2,3,4]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${transform}= | Get From Dictionary | ${json} | matrix
| | ${row0}= | Get From List | ${transform} | 0
| | ${row1}= | Get From List | ${transform} | 1
| | ${row2}= | Get From List | ${transform} | 2
| | ${x}= | Get From List | ${row0} | 3
| | ${y}= | Get From List | ${row1} | 3
| | ${z}= | Get From List | ${row2} | 3
| | Should be equal as integers | ${x} | 2
| | Should be equal as integers | ${y} | 3
| | Should be equal as integers | ${z} | 4


| Test the rtIntersectionSet for when a ray intersects a scaled sphere - ray is transformed with the inverse transform of the sphere first
| | ${result}= | run process | python | ./rayIntersectionTester.py | testIntersectionsWithScaledSphere | [0, 0, -5] | [0, 0, 1] | [2, 2, 2]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${hit0}= | Get From List | ${json} | 0
| | ${hit1}= | Get From List | ${json} | 1
| | Should be equal as integers | ${hit0} | 3
| | Should be equal as integers | ${hit1} | 7

| Test the rtIntersectionSet for when a ray intersects a translated sphere - ray is transformed with the inverse transform of the sphere first
| | ${result}= | run process | python | ./rayIntersectionTester.py | testIntersectionsWithTranslatedSphere | [0, 0, -5] | [0, 0, 1] | [5, 0, 0]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${length}= | Get Length | ${json}
| | Should be equal as numbers | ${length} | 0

| Test the normal of the sphere when x=1, y=0, z=0
| | ${result}= | run process | python | ./rayIntersectionTester.py | testNormals | [1, 0, 0]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${normal}= | Get From Dictionary | ${json} | normal
| | ${x}= | Get From List | ${normal} | 0
| | ${y}= | Get From List | ${normal} | 1
| | ${z}= | Get From List | ${normal} | 2
| | Should be equal as numbers | ${x} | 1
| | Should be equal as numbers | ${y} | 0
| | Should be equal as numbers | ${z} | 0

| Test the normal of the sphere when x=0, y=1, z=0
| | ${result}= | run process | python | ./rayIntersectionTester.py | testNormals | [0, 1, 0]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${normal}= | Get From Dictionary | ${json} | normal
| | ${x}= | Get From List | ${normal} | 0
| | ${y}= | Get From List | ${normal} | 1
| | ${z}= | Get From List | ${normal} | 2
| | Should be equal as numbers | ${x} | 0
| | Should be equal as numbers | ${y} | 1
| | Should be equal as numbers | ${z} | 0

| Test the normal of the sphere when x=0, y=0, z=1
| | ${result}= | run process | python | ./rayIntersectionTester.py | testNormals | [0, 0, 1]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${normal}= | Get From Dictionary | ${json} | normal
| | ${x}= | Get From List | ${normal} | 0
| | ${y}= | Get From List | ${normal} | 1
| | ${z}= | Get From List | ${normal} | 2
| | Should be equal as numbers | ${x} | 0
| | Should be equal as numbers | ${y} | 0
| | Should be equal as numbers | ${z} | 1

| Test the normal of the sphere when x=3^0.5/3, y=3^0.5/3, z=3^0.5/3
# root 3 / 3
| | Set Suite Variable | ${root3over3} | 0.577
| | ${result}= | run process | python | ./rayIntersectionTester.py | testNormals | [${root3over3}, ${root3over3}, ${root3over3}]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${normal}= | Get From Dictionary | ${json} | normal
| | ${x}= | Get From List | ${normal} | 0
| | ${y}= | Get From List | ${normal} | 1
| | ${z}= | Get From List | ${normal} | 2
| | Should be equal as numbers | ${x} | ${root3over3}
| | Should be equal as numbers | ${y} | ${root3over3}
| | Should be equal as numbers | ${z} | ${root3over3}

| Test the normal of the sphere when x=3^0.5/3, y=3^0.5/3, z=3^0.5/3 is a normalised number
# root 3 / 3
| | Set Suite Variable | ${root3over3} | 0.577
| | ${result}= | run process | python | ./rayIntersectionTester.py | testNormalIsNormalised | [${root3over3}, ${root3over3}, ${root3over3}]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${yesno}= | Get From Dictionary | ${json} | isNormalised
| | Should be equal as strings | ${yesno} | Yes

| Test the normal of the sphere when x=0, y=2^0.5/2, z=2^0.5/2
# root 2 / 2
| | Set Suite Variable | ${root2over2} | 0.707
# root (2 / 2) +1
| | Set Suite Variable | ${root2over2plusone} | 1.707
| | Set Suite Variable | ${root2over2plustwo} | 2.707
| | Set Suite Variable | ${minusroot2over2} | -0.707
| | ${result}= | run process | python | ./rayIntersectionTester.py | testNormalsWithTranslation | [0, ${root2over2plusone} , ${minusroot2over2}] | [0, 1, 0]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${normal}= | Get From Dictionary | ${json} | normal
| | ${x}= | Get From List | ${normal} | 0
| | ${y}= | Get From List | ${normal} | 1
| | ${z}= | Get From List | ${normal} | 2
| | Should be equal as numbers | ${x} | 0
| | Should be equal as numbers | ${y} | ${root2over2}
| | Should be equal as numbers | ${z} | ${minusroot2over2}

| Test the normal of the sphere when x=0, y=2^0.5/2, z=-2^0.5/2 and the transform is a scale and a rotation
# root 2 / 2
| | Set Suite Variable | ${root2over2} | 0.707
# root (2 / 2) * -1
| | Set Suite Variable | ${minusroot2over2} | -0.707
# pi / 5
| | Set Suite Variable | ${piover5} | 0.62832
| | ${result}= | run process | python | ./rayIntersectionTester.py | testNormalsWithTransform | [0, ${root2over2} , ${minusroot2over2}] | [1, 0.5, 1] | [0, 0, ${piover5}]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${normal}= | Get From Dictionary | ${json} | normal
| | ${x}= | Get From List | ${normal} | 0
| | ${y}= | Get From List | ${normal} | 1
| | ${z}= | Get From List | ${normal} | 2
| | Should be equal as numbers | ${x} | 0
| | Should be equal as numbers | ${y} | 0.970143
| | Should be equal as numbers | ${z} | -0.242536
