*** Settings ***
| Library | Process
| Library | Collections
| Library | json

*** Test Cases ***
| Test the basic construction and query
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

| Test the position r(0)
| | ${result}= | run process | python | ./rayTester.py | testPosition | [2, 3, 4] | [1, 0, 0] | 0
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${resultOrigin}= | Get From Dictionary | ${json} | tpoint
| | ${resultX}= | Collections.Get From List | ${resultOrigin} | 0
| | Should be equal as numbers | ${resultX} | 2.0
| | ${resultY}= | Collections.Get From List | ${resultOrigin} | 1
| | Should be equal as numbers | ${resultY} | 3.0
| | ${resultZ}= | Collections.Get From List | ${resultOrigin} | 2
| | Should be equal as numbers | ${resultZ} | 4.0

| Test the position r(1)
| | ${result}= | run process | python | ./rayTester.py | testPosition | [2, 3, 4] | [1, 0, 0] | 1
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${resultOrigin}= | Get From Dictionary | ${json} | tpoint
| | ${resultX}= | Collections.Get From List | ${resultOrigin} | 0
| | Should be equal as numbers | ${resultX} | 3.0
| | ${resultY}= | Collections.Get From List | ${resultOrigin} | 1
| | Should be equal as numbers | ${resultY} | 3.0
| | ${resultZ}= | Collections.Get From List | ${resultOrigin} | 2
| | Should be equal as numbers | ${resultZ} | 4.0

| Test the position r(-1)
| | ${result}= | run process | python | ./rayTester.py | testPosition | [2, 3, 4] | [1, 0, 0] | -1
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${resultOrigin}= | Get From Dictionary | ${json} | tpoint
| | ${resultX}= | Collections.Get From List | ${resultOrigin} | 0
| | Should be equal as numbers | ${resultX} | 1.0
| | ${resultY}= | Collections.Get From List | ${resultOrigin} | 1
| | Should be equal as numbers | ${resultY} | 3.0
| | ${resultZ}= | Collections.Get From List | ${resultOrigin} | 2
| | Should be equal as numbers | ${resultZ} | 4.0

| Test the position r(2.5)
| | ${result}= | run process | python | ./rayTester.py | testPosition | [2, 3, 4] | [1, 0, 0] | 2.5
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${resultOrigin}= | Get From Dictionary | ${json} | tpoint
| | ${resultX}= | Collections.Get From List | ${resultOrigin} | 0
| | Should be equal as numbers | ${resultX} | 4.5
| | ${resultY}= | Collections.Get From List | ${resultOrigin} | 1
| | Should be equal as numbers | ${resultY} | 3.0
| | ${resultZ}= | Collections.Get From List | ${resultOrigin} | 2
| | Should be equal as numbers | ${resultZ} | 4.0

