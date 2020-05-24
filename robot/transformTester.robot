*** Settings ***
| Library | Process
| Library | Collections
| Library | json

*** Test Cases ***
| Check a translate for a point
| | ${result}= | run process | python | ./transformTester.py | testTranslate | [-3, 4, 5] | [5, -3, 2]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${resultPoint}= | Get From List | ${json} | 0
| | ${resultX}= | Collections.Get From List | ${resultPoint} | 0
| | Should be equal as numbers | ${resultX} | 2.0
| | ${resultY}= | Collections.Get From List | ${resultPoint} | 1
| | Should be equal as numbers | ${resultY} | 1.0
| | ${resultZ}= | Collections.Get From List | ${resultPoint} | 2
| | Should be equal as numbers | ${resultZ} | 7.0

| Check an inverse translate for a point
| | ${result}= | run process | python | ./transformTester.py | testInverseTranslate | [-3, 4, 5] | [5, -3, 2]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${resultPoint}= | Get From List | ${json} | 0
| | ${resultX}= | Collections.Get From List | ${resultPoint} | 0
| | Should be equal as numbers | ${resultX} | -8.0
| | ${resultY}= | Collections.Get From List | ${resultPoint} | 1
| | Should be equal as numbers | ${resultY} | 7.0
| | ${resultZ}= | Collections.Get From List | ${resultPoint} | 2
| | Should be equal as numbers | ${resultZ} | 3.0

| Check a translate for a vector
| | ${result}= | run process | python | ./transformTester.py | testTranslateVector | [-3, 4, 5] | [5, -3, 2]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${resultPoint}= | Get From List | ${json} | 0
| | ${resultX}= | Collections.Get From List | ${resultPoint} | 0
| | Should be equal as numbers | ${resultX} | -3.0
| | ${resultY}= | Collections.Get From List | ${resultPoint} | 1
| | Should be equal as numbers | ${resultY} | 4.0
| | ${resultZ}= | Collections.Get From List | ${resultPoint} | 2
| | Should be equal as numbers | ${resultZ} | 5.0

| Check a scaling for a point
| | ${result}= | run process | python | ./transformTester.py | testScalePoint | [-4, 6, 8] | [2, 3, 4]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${resultPoint}= | Get From List | ${json} | 0
| | ${resultX}= | Collections.Get From List | ${resultPoint} | 0
| | Should be equal as numbers | ${resultX} | -8.0
| | ${resultY}= | Collections.Get From List | ${resultPoint} | 1
| | Should be equal as numbers | ${resultY} | 18.0
| | ${resultZ}= | Collections.Get From List | ${resultPoint} | 2
| | Should be equal as numbers | ${resultZ} | 32.0

| Check a scaling for a vector
| | ${result}= | run process | python | ./transformTester.py | testScaleVector | [-4, 6, 8] | [2, 3, 4]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${resultPoint}= | Get From List | ${json} | 0
| | ${resultX}= | Collections.Get From List | ${resultPoint} | 0
| | Should be equal as numbers | ${resultX} | -8.0
| | ${resultY}= | Collections.Get From List | ${resultPoint} | 1
| | Should be equal as numbers | ${resultY} | 18.0
| | ${resultZ}= | Collections.Get From List | ${resultPoint} | 2
| | Should be equal as numbers | ${resultZ} | 32.0

| Check an inverse scaling for a vector
| | ${result}= | run process | python | ./transformTester.py | testInverseScaleVector | [-4, 6, 8] | [2, 3, 4]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${resultPoint}= | Get From List | ${json} | 0
| | ${resultX}= | Collections.Get From List | ${resultPoint} | 0
| | Should be equal as numbers | ${resultX} | -2.0
| | ${resultY}= | Collections.Get From List | ${resultPoint} | 1
| | Should be equal as numbers | ${resultY} | 2.0
| | ${resultZ}= | Collections.Get From List | ${resultPoint} | 2
| | Should be equal as numbers | ${resultZ} | 2.0

| Check an negative scaling for a point
| | ${result}= | run process | python | ./transformTester.py | testNegativeScalePoint | [2, 3, 4] | [-1, 1, 1]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${resultPoint}= | Get From List | ${json} | 0
| | ${resultX}= | Collections.Get From List | ${resultPoint} | 0
| | Should be equal as numbers | ${resultX} | -2.0
| | ${resultY}= | Collections.Get From List | ${resultPoint} | 1
| | Should be equal as numbers | ${resultY} | 3.0
| | ${resultZ}= | Collections.Get From List | ${resultPoint} | 2
| | Should be equal as numbers | ${resultZ} | 4.0

| Check an half-quarter rotation about X for a point 
| | ${result}= | run process | python | ./transformTester.py | testRotatePoint | half-quarter | X | [0, 1, 0]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${resultPoint}= | Get From List | ${json} | 0
| | ${resultX}= | Collections.Get From List | ${resultPoint} | 0
| | Should be equal as numbers | ${resultX} | 0.0
| | ${resultY}= | Collections.Get From List | ${resultPoint} | 1
| | Should be equal as numbers | ${resultY} | 0.707107
| | ${resultZ}= | Collections.Get From List | ${resultPoint} | 2
| | Should be equal as numbers | ${resultZ} | 0.707107

| Check an quarter rotation about X for a point 
| | ${result}= | run process | python | ./transformTester.py | testRotatePoint | quarter | X | [0, 1, 0]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${resultPoint}= | Get From List | ${json} | 0
| | ${resultX}= | Collections.Get From List | ${resultPoint} | 0
| | Should be equal as numbers | ${resultX} | 0.0
| | ${resultY}= | Collections.Get From List | ${resultPoint} | 1
| | Should be equal as numbers | ${resultY} | 0.0
| | ${resultZ}= | Collections.Get From List | ${resultPoint} | 2
| | Should be equal as numbers | ${resultZ} | 1.0

| Check an half-quarter rotation about Y for a point 
| | ${result}= | run process | python | ./transformTester.py | testRotatePoint | half-quarter | Y | [0, 0, 1]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${resultPoint}= | Get From List | ${json} | 0
| | ${resultX}= | Collections.Get From List | ${resultPoint} | 0
| | Should be equal as numbers | ${resultX} | 0.707107
| | ${resultY}= | Collections.Get From List | ${resultPoint} | 1
| | Should be equal as numbers | ${resultY} | 0.0
| | ${resultZ}= | Collections.Get From List | ${resultPoint} | 2
| | Should be equal as numbers | ${resultZ} | 0.707107

| Check an quarter rotation about Y for a point 
| | ${result}= | run process | python | ./transformTester.py | testRotatePoint | quarter | Y | [0, 0, 1]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${resultPoint}= | Get From List | ${json} | 0
| | ${resultX}= | Collections.Get From List | ${resultPoint} | 0
| | Should be equal as numbers | ${resultX} | 1.0
| | ${resultY}= | Collections.Get From List | ${resultPoint} | 1
| | Should be equal as numbers | ${resultY} | 0.0
| | ${resultZ}= | Collections.Get From List | ${resultPoint} | 2
| | Should be equal as numbers | ${resultZ} | 0.0

| Check an half-quarter rotation about Z for a point 
| | ${result}= | run process | python | ./transformTester.py | testRotatePoint | half-quarter | Z | [0, 1, 0]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${resultPoint}= | Get From List | ${json} | 0
| | ${resultX}= | Collections.Get From List | ${resultPoint} | 0
| | Should be equal as numbers | ${resultX} | -0.707107
| | ${resultY}= | Collections.Get From List | ${resultPoint} | 1
| | Should be equal as numbers | ${resultY} | 0.707107
| | ${resultZ}= | Collections.Get From List | ${resultPoint} | 2
| | Should be equal as numbers | ${resultZ} | 0.0

| Check an quarter rotation about Z for a point 
| | ${result}= | run process | python | ./transformTester.py | testRotatePoint | quarter | Z | [0, 1, 0]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${resultPoint}= | Get From List | ${json} | 0
| | ${resultX}= | Collections.Get From List | ${resultPoint} | 0
| | Should be equal as numbers | ${resultX} | -1.0
| | ${resultY}= | Collections.Get From List | ${resultPoint} | 1
| | Should be equal as numbers | ${resultY} | 0.0
| | ${resultZ}= | Collections.Get From List | ${resultPoint} | 2
| | Should be equal as numbers | ${resultZ} | 0.0

| Check an x=>y shear on a point 
| | ${result}= | run process | python | ./transformTester.py | testShearPoint | [1, 0, 0, 0, 0, 0] | [2, 3, 4]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${resultPoint}= | Get From List | ${json} | 0
| | ${resultX}= | Collections.Get From List | ${resultPoint} | 0
| | Should be equal as numbers | ${resultX} | 5.0
| | ${resultY}= | Collections.Get From List | ${resultPoint} | 1
| | Should be equal as numbers | ${resultY} | 3.0
| | ${resultZ}= | Collections.Get From List | ${resultPoint} | 2
| | Should be equal as numbers | ${resultZ} | 4.0
