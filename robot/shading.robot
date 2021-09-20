*** Settings ***
| Library | Process
| Library | Collections
| Library | json

*** Test Cases ***
| Test the colour hitting a sphere from the outside
| | ${result}= | run process | python | ./shadeTester.py | testOutsideHit | [0, 0, -5] | [0, 0, 1]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${colour}= | Get From Dictionary | ${json} | colour
| | ${red}= | Get From List | ${colour} | 0
| | ${green}= | Get From List | ${colour} | 1
| | ${blue}= | Get From List | ${colour} | 2
| | Should be equal as numbers | ${red} | 0.38066   | precision=5
| | Should be equal as numbers | ${green} | 0.47583 | precision=5
| | Should be equal as numbers | ${blue} | 0.2855   | precision=5

| Test the colour hitting a sphere from the inside
| | ${result}= | run process | python | ./shadeTester.py | testInsideHit | [0, 0, 0] | [0, 0, 1]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${colour}= | Get From Dictionary | ${json} | colour
| | ${red}= | Get From List | ${colour} | 0
| | ${green}= | Get From List | ${colour} | 1
| | ${blue}= | Get From List | ${colour} | 2
| | Should be equal as numbers | ${red} | 0.90498   | precision=5
| | Should be equal as numbers | ${green} | 0.90498 | precision=5
| | Should be equal as numbers | ${blue} | 0.90498  | precision=5

| Test the default world with the vector not hitting anything
| | ${result}= | run process | python | ./shadeTester.py | testDefaultWorldWithVector | [0, 0, -5] | [0, 1, 0]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${colour}= | Get From Dictionary | ${json} | colour
| | ${red}= | Get From List | ${colour} | 0
| | ${green}= | Get From List | ${colour} | 1
| | ${blue}= | Get From List | ${colour} | 2
| | Should be equal as numbers | ${red} | 0.000   | precision=3
| | Should be equal as numbers | ${green} | 0.000 | precision=3
| | Should be equal as numbers | ${blue} | 0.000  | precision=3

| Test the default world with the vector hitting the outside sphere
| | ${result}= | run process | python | ./shadeTester.py | testDefaultWorldWithVector | [0, 0, -5] | [0, 0, 1]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${colour}= | Get From Dictionary | ${json} | colour
| | ${red}= | Get From List | ${colour} | 0
| | ${green}= | Get From List | ${colour} | 1
| | ${blue}= | Get From List | ${colour} | 2
| | Should be equal as numbers | ${red} | 0.38066   | precision=5
| | Should be equal as numbers | ${green} | 0.47583 | precision=5
| | Should be equal as numbers | ${blue} | 0.2855   | precision=5

| Test the default world with the vector hitting the inside sphere
| | ${result}= | run process | python | ./shadeTester.py | testDefaultWorldInsideOuterSphere | [0, 0, 0.75] | [0, 0, -1]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${colour}= | Get From Dictionary | ${json} | colour
| | ${red}= | Get From List | ${colour} | 0
| | ${green}= | Get From List | ${colour} | 1
| | ${blue}= | Get From List | ${colour} | 2
| | Should be equal as numbers | ${red} | 0.38066   | precision=5
| | Should be equal as numbers | ${green} | 0.47583 | precision=5
| | Should be equal as numbers | ${blue} | 0.2855   | precision=5
