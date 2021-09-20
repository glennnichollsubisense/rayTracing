*** Settings ***
| Library | Process
| Library | Collections
| Library | json

*** Test Cases ***
| Test 1a - Make a point and check it is a point
| | ${result}= | run process | python | ./pointsAndVectorsTester.py | testIsPoint | [4.3, -4.2, 3.1]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | Should be equal as strings | ${json} | True

| Test 1b - Make a vector and check its a vector
| | ${result}= | run process | python | ./pointsAndVectorsTester.py | testIsVector | [1, 2, 3]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | Should be equal as strings | ${json} | True

| Test 3a - Make two vectors and add them together
| | ${result}= | run process | python | ./pointsAndVectorsTester.py | addVectors | [3, -2, 5] | [-2, 3, 1]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${resultvector}= | Collections.Get From List | ${json} | 0
| | ${resultX}= | Collections.Get From List | ${resultvector} | 0
| | Should be equal as numbers | ${resultX} | 1.0
| | ${resultY}= | Collections.Get From List | ${resultvector} | 1
| | Should be equal as numbers | ${resultY} | 1.0
| | ${resultZ}= | Collections.Get From List | ${resultvector} | 2
| | Should be equal as numbers | ${resultZ} | 6.0

| Test 3b - Make two points and add them together
| | ${result}= | run process | python | ./pointsAndVectorsTester.py | addPoints | [3, -2, 5] | [-2, 3, 1]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | Should be equal as strings | ${json} | badAddition correctly raised

| Test 3c - Add a point to a vector 
| | ${result}= | run process | python | ./pointsAndVectorsTester.py | addPointToAVector | [3, -2, 5] | [-2, 3, 1]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${resultvector}= | Collections.Get From List | ${json} | 0
| | ${resultX}= | Collections.Get From List | ${resultvector} | 0
| | Should be equal as numbers | ${resultX} | 1.0
| | ${resultY}= | Collections.Get From List | ${resultvector} | 1
| | Should be equal as numbers | ${resultY} | 1.0
| | ${resultZ}= | Collections.Get From List | ${resultvector} | 2
| | Should be equal as numbers | ${resultZ} | 6.0

| Test 7aa - Multiply a point by a scalar
| | ${result}= | run process | python | ./pointsAndVectorsTester.py | multiplyPointByScalar | [1, 2, 3] | 17
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | Should be equal as strings | ${json} | badScalarMultiplication correctly raised

| Test 7aab - Multiply a vector by a scalar
| | ${result}= | run process | python | ./pointsAndVectorsTester.py | multiplyVectorByScalar | [1, 2, 3] | 17
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${resultvector}= | Collections.Get From List | ${json} | 0
| | ${resultX}= | Collections.Get From List | ${resultvector} | 0
| | Should be equal as numbers | ${resultX} | 17.0
| | ${resultY}= | Collections.Get From List | ${resultvector} | 1
| | Should be equal as numbers | ${resultY} | 34.0
| | ${resultZ}= | Collections.Get From List | ${resultvector} | 2
| | Should be equal as numbers | ${resultZ} | 51.0

| Test 8a - Divide a point by a scalar
| | ${result}= | run process | python | ./pointsAndVectorsTester.py | dividePointByScalar | [1, 2, 3] | 17
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | Should be equal as strings | ${json} | badScalarDivision correctly raised

| Test 8b - Divide a vector by a scalar
| | ${result}= | run process | python | ./pointsAndVectorsTester.py | divideVectorByScalar | [51, 34, 17] | 17
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${resultvector}= | Collections.Get From List | ${json} | 0
| | ${resultX}= | Collections.Get From List | ${resultvector} | 0
| | Should be equal as numbers | ${resultX} | 3.0
| | ${resultY}= | Collections.Get From List | ${resultvector} | 1
| | Should be equal as numbers | ${resultY} | 2.0
| | ${resultZ}= | Collections.Get From List | ${resultvector} | 2
| | Should be equal as numbers | ${resultZ} | 1.0

| Test 9a - Magnitude of Point
| | ${result}= | run process | python | ./pointsAndVectorsTester.py | magnitudeOfPoint | [1, 2, 3] 
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | Should be equal as strings | ${json} | badMagnitude correctly raised

| Test 9b - Magnitude of Vector 1,0,0
| | ${result}= | run process | python | ./pointsAndVectorsTester.py | magnitudeOfVector | [1, 0, 0] 
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | Should be equal as numbers | ${json} | 1.0

| Test 9c - Magnitude of Vector 0,0,1
| | ${result}= | run process | python | ./pointsAndVectorsTester.py | magnitudeOfVector | [0, 0, 1] 
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | Should be equal as numbers | ${json} | 1.0

| Test 9d - Magnitude of Vector 0,1,0
| | ${result}= | run process | python | ./pointsAndVectorsTester.py | magnitudeOfVector | [0, 1, 0] 
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | Should be equal as numbers | ${json} | 1.0

| Test 9e - Magnitude of Vector 1,2,3
| | ${result}= | run process | python | ./pointsAndVectorsTester.py | magnitudeOfVector | [1,2,3] 
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | Should be equal as numbers | ${json} | 3.741657

| Test 9f - Magnitude of Vector -1, -2, -3
| | ${result}= | run process | python | ./pointsAndVectorsTester.py | magnitudeOfVector | [-1, -2, -3] 
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | Should be equal as numbers | ${json} | 3.741657

| Test 10 - Normalise Point
| | ${result}= | run process | python | ./pointsAndVectorsTester.py | normalisePoint | [1, 2, 3] 
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | Should be equal as strings | ${json} | badNormalise correctly raised

| Test 10b - Normalise Vector 4,0,0
| | ${result}= | run process | python | ./pointsAndVectorsTester.py | normaliseVector | [4, 0, 0] 
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${resultvector}= | Collections.Get From List | ${json} | 0
| | ${resultX}= | Collections.Get From List | ${resultvector} | 0
| | Should be equal as numbers | ${resultX} | 1.0
| | ${resultY}= | Collections.Get From List | ${resultvector} | 1
| | Should be equal as numbers | ${resultY} | 0.0
| | ${resultZ}= | Collections.Get From List | ${resultvector} | 2
| | Should be equal as numbers | ${resultZ} | 0.0

| Test 11a - Dot Product Point 
| | ${result}= | run process | python | ./pointsAndVectorsTester.py | dotProductPoint | [1, 2, 3] | [2, 3, 4]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | Should be equal as strings | ${json} | badDotProduct correctly raised

| Test 11b - Dot Product Vector 1,2,3 with 2,3,4 
| | ${result}= | run process | python | ./pointsAndVectorsTester.py | dotProductVector | [1, 2, 3] | [2, 3, 4]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | Should be equal as numbers | ${json} | 20

| Test 12a - Cross Product Point 
| | ${result}= | run process | python | ./pointsAndVectorsTester.py | crossProductPoint | [1, 2, 3] | [2, 3, 4]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | Should be equal as strings | ${json} | badCrossProduct correctly raised

| Test 12b - Cross Product Vector 1,2,3 with 2,3,4 
| | ${result}= | run process | python | ./pointsAndVectorsTester.py | crossProductVector | [1, 2, 3] | [2, 3, 4]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${resultvector}= | Collections.Get From List | ${json} | 0
| | ${resultX}= | Collections.Get From List | ${resultvector} | 0
| | Should be equal as numbers | ${resultX} | -1.0
| | ${resultY}= | Collections.Get From List | ${resultvector} | 1
| | Should be equal as numbers | ${resultY} | 2.0
| | ${resultZ}= | Collections.Get From List | ${resultvector} | 2
| | Should be equal as numbers | ${resultZ} | -1.0

| Test 12c - Cross Product Vector 2,3,4 with 1,2,3
| | ${result}= | run process | python | ./pointsAndVectorsTester.py | crossProductVector | [2, 3, 4] | [1, 2, 3]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${resultvector}= | Collections.Get From List | ${json} | 0
| | ${resultX}= | Collections.Get From List | ${resultvector} | 0
| | Should be equal as numbers | ${resultX} | 1.0
| | ${resultY}= | Collections.Get From List | ${resultvector} | 1
| | Should be equal as numbers | ${resultY} | -2.0
| | ${resultZ}= | Collections.Get From List | ${resultvector} | 2
| | Should be equal as numbers | ${resultZ} | 1.0


