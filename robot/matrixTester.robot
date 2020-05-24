*** Settings ***
| Library | Process
| Library | Collections
| Library | json

*** Test Cases ***
| Check the identity matrix 
| | ${result}= | run process | python | ./matrixTester.py | testIdentityFalse
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${result} | Collections.Get From Dictionary | ${json} | result
| | Should be equal as strings | ${result} | False

| | ${result}= | run process | python | ./matrixTester.py | testIdentityTrue
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${result} | Collections.Get From Dictionary | ${json} | result
| | Should be equal as strings | ${result} | True

