*** Settings ***
| Library | Process
| Library | Collections
| Library | json

*** Test Cases ***
| Test the basic construction and queries of a world - ch7 Test1
| | ${result}= | run process | python | ./worldTester.py | testEmptyWorld
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${resultObjects}= | Get From Dictionary | ${json} | objects
| | ${noofObjects}= | Get Length | ${resultObjects}
| | Should Be Equal as Integers | ${noofObjects} | 0
| | ${resultLightSources}= | Get From Dictionary | ${json} | lightsources
| | ${noofLightSources}= | Get Length | ${resultLightSources}
| | Should Be Equal as Integers | ${noofLightSources} | 0

| Test a world with two spheres and a single light source - ch7 Test 2
| | ${result}= | run process | python | ./worldTester.py | testTwoSpheres
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${noofObjects}= | Get From Dictionary | ${json} | noofobjects
| | Should Be Equal as Integers | ${noofObjects} | 2
| | ${noofLightSources}= | Get From Dictionary | ${json} | nooflightsources
| | Should Be Equal as Integers | ${noofLightSources} | 1

| Test interaction with a ray and a world with two spheres and a single light source - ch7 Test 3
| | ${result}= | run process | python | ./worldTester.py | testTwoSpheresAndRay
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${intersections}= | Get From Dictionary | ${json} | intersections
| | ${noofIntersections}= | Get Length | ${intersections}
| | Should Be Equal as Integers | ${noofIntersections} | 4
| | ${nearest}= | Get From List | ${intersections} | 0
| | ${secondnearest}= | Get From List | ${intersections} | 1
| | ${furthest}= | Get From List | ${intersections} | 3
| | Should Be Equal as Numbers | ${nearest} | 4.0
| | Should Be Equal as Numbers | ${secondnearest} | 4.5
| | Should Be Equal as Numbers | ${furthest} | 6.0


