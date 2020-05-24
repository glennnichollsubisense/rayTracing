*** Settings ***
| Library | Process
| Library | Collections
| Library | json

*** Test Cases ***
| Piecemeal rotate
| | ${result}= | run process | python | ./transformTester.py | testRotatePoint | quarter | X | [1, 0, 1]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${resultPoint}= | Get From List | ${json} | 0
| | ${resultX}= | Collections.Get From List | ${resultPoint} | 0
| | Should be equal as numbers | ${resultX} | 1.0
| | ${resultY}= | Collections.Get From List | ${resultPoint} | 1
| | Should be equal as numbers | ${resultY} | -1.0
| | ${resultZ}= | Collections.Get From List | ${resultPoint} | 2
| | Should be equal as numbers | ${resultZ} | 0.0

| Piecemeal scaling
| | ${result}= | run process | python | ./transformTester.py | testScalePoint | [5, 5, 5] | [1, -1, 0]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${resultPoint}= | Get From List | ${json} | 0
| | ${resultX}= | Collections.Get From List | ${resultPoint} | 0
| | Should be equal as numbers | ${resultX} | 5.0
| | ${resultY}= | Collections.Get From List | ${resultPoint} | 1
| | Should be equal as numbers | ${resultY} | -5.0
| | ${resultZ}= | Collections.Get From List | ${resultPoint} | 2
| | Should be equal as numbers | ${resultZ} | 0.0

| Piecemeal translation
| | ${result}= | run process | python | ./transformTester.py | testTranslate | [10, 5, 7] | [5, -5, 0]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${resultPoint}= | Get From List | ${json} | 0
| | ${resultX}= | Collections.Get From List | ${resultPoint} | 0
| | Should be equal as numbers | ${resultX} | 15.0
| | ${resultY}= | Collections.Get From List | ${resultPoint} | 1
| | Should be equal as numbers | ${resultY} | 0.0
| | ${resultZ}= | Collections.Get From List | ${resultPoint} | 2
| | Should be equal as numbers | ${resultZ} | 7.0

| Chained transforms
| | ${result}= | run process | python | ./transformTester.py | testChained | [1, 0, 1]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${resultPoint}= | Get From List | ${json} | 0
| | ${resultX}= | Collections.Get From List | ${resultPoint} | 0
| | Should be equal as numbers | ${resultX} | 15.0
| | ${resultY}= | Collections.Get From List | ${resultPoint} | 1
| | Should be equal as numbers | ${resultY} | 0.0
| | ${resultZ}= | Collections.Get From List | ${resultPoint} | 2
| | Should be equal as numbers | ${resultZ} | 7.0

| Chained transforms, run twice
| | ${result}= | run process | python | ./transformTester.py | testChainedRunTwice | [1, 0, 1]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${resultPoint}= | Get From List | ${json} | 0
| | ${resultX}= | Collections.Get From List | ${resultPoint} | 0
| | Should be equal as numbers | ${resultX} | 15.0
| | ${resultY}= | Collections.Get From List | ${resultPoint} | 1
| | Should be equal as numbers | ${resultY} | 0.0
| | ${resultZ}= | Collections.Get From List | ${resultPoint} | 2
| | Should be equal as numbers | ${resultZ} | 7.0


