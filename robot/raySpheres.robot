*** Settings ***
| Library | Process
| Library | Collections
| Library | json

*** Test Cases ***
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






