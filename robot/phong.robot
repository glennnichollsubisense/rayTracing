*** Settings ***
| Library | Process
| Library | Collections
| Library | json


*** Test Cases ***


| Test the reflection of one vector with another at 45 degs
| | ${result}= | run process | python | ./phongTester.py | testReflect | [1, -1, 0] | [0, 1, 0]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${reflection}= | Get From Dictionary | ${json} | reflection
| | ${row}= | Get From List | ${reflection} | 0
| | ${x}= | Get From List | ${row} | 0
| | ${y}= | Get From List | ${row} | 1
| | ${z}= | Get From List | ${row} | 2
| | Should be equal as numbers | ${x} | 1.0
| | Should be equal as numbers | ${y} | 1.0
| | Should be equal as numbers | ${z} | 0.0


| Test the reflection of one vector with another at an oblique angle
# root 2 / 2
| | Set Suite Variable | ${root2over2} | 0.7071
| | ${result}= | run process | python | ./phongTester.py | testReflect | [0, -1, 0] | [${root2over2}, ${root2over2}, 0]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${reflection}= | Get From Dictionary | ${json} | reflection
| | ${row}= | Get From List | ${reflection} | 0
| | ${x}= | Get From List | ${row} | 0
| | ${x}= | Convert To Number | ${x} | 0
| | ${y}= | Get From List | ${row} | 1
| | ${y}= | Convert To Number | ${y} | 0
| | ${z}= | Get From List | ${row} | 2
| | ${z}= | Convert To Number | ${z} | 0
| | Should be equal as numbers | ${x} | 1
| | Should be equal as numbers | ${y} | 0
| | Should be equal as numbers | ${z} | 0

| Make a light source and check the components 
| | ${result}= | run process | python | ./phongTester.py | testLightSource | [1, 1, 1] | [0, 0, 0]
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${position}= | Get From Dictionary | ${json} | position
| | ${row}= | Get From List | ${position} | 0
| | ${x}= | Get From List | ${row} | 0
| | ${x}= | Convert To Number | ${x} | 0
| | ${y}= | Get From List | ${row} | 1
| | ${y}= | Convert To Number | ${y} | 0
| | ${z}= | Get From List | ${row} | 2
| | ${z}= | Convert To Number | ${z} | 0
| | Should be equal as numbers | ${x} | 0
| | Should be equal as numbers | ${y} | 0
| | Should be equal as numbers | ${z} | 0
| | ${colour}= | Get From Dictionary | ${json} | colour
| | ${red}= | Get From List | ${row} | 0
| | ${red}= | Convert To Number | ${red} | 0
| | ${green}= | Get From List | ${row} | 1
| | ${green}= | Convert To Number | ${green} | 0
| | ${blue}= | Get From List | ${row} | 2
| | ${blue}= | Convert To Number | ${blue} | 0
| | Should be equal as numbers | ${red} | 0
| | Should be equal as numbers | ${green} | 0
| | Should be equal as numbers | ${blue} | 0

| Make a material and check the components 
| | ${result}= | run process | python | ./phongTester.py | testMaterial | [1, 1, 1] | 0.1 | 0.5 | 0.9 | 200.0
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${colour}= | Get From Dictionary | ${json} | colour
| | ${red}= | Get From List | ${colour} | 0
| | ${red}= | Convert To Number | ${red} | 0
| | ${green}= | Get From List | ${colour} | 1
| | ${green}= | Convert To Number | ${green} | 0
| | ${blue}= | Get From List | ${colour} | 2
| | ${blue}= | Convert To Number | ${blue} | 0
| | Should be equal as numbers | ${red} | 1
| | Should be equal as numbers | ${green} | 1
| | Should be equal as numbers | ${blue} | 1
| | ${ambient}= | Get From Dictionary | ${json} | ambient
| | Should be equal as numbers | ${ambient} | 0.1
| | ${specular}= | Get From Dictionary | ${json} | specular
| | Should be equal as numbers | ${specular} | 0.9
| | ${diffuse}= | Get From Dictionary | ${json} | diffuse
| | Should be equal as numbers | ${diffuse} | 0.5
| | ${shininess}= | Get From Dictionary | ${json} | shininess
| | Should be equal as numbers | ${shininess} | 200.0


| Make a sphere and check it has a default material
| | ${result}= | run process | python | ./phongTester.py | testMaterialonSphere
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${colour}= | Get From Dictionary | ${json} | colour
| | ${red}= | Get From List | ${colour} | 0
| | ${red}= | Convert To Number | ${red} | 1
| | ${green}= | Get From List | ${colour} | 1
| | ${green}= | Convert To Number | ${green} | 1
| | ${blue}= | Get From List | ${colour} | 2
| | ${blue}= | Convert To Number | ${blue} | 1
| | Should be equal as numbers | ${red} | 1.0
| | Should be equal as numbers | ${green} | 1.0
| | Should be equal as numbers | ${blue} | 1.0
| | ${ambient}= | Get From Dictionary | ${json} | ambient
| | Should be equal as numbers | ${ambient} | 0.1
| | ${specular}= | Get From Dictionary | ${json} | specular
| | Should be equal as numbers | ${specular} | 0.9
| | ${diffuse}= | Get From Dictionary | ${json} | diffuse
| | Should be equal as numbers | ${diffuse} | 0.9
| | ${shininess}= | Get From Dictionary | ${json} | shininess
| | Should be equal as numbers | ${shininess} | 200.0

| Make a sphere, and assign a material and check it
| | ${result}= | run process | python | ./phongTester.py | testMaterialonSphere2 | grass
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${colour}= | Get From Dictionary | ${json} | colour
| | ${red}= | Get From List | ${colour} | 0
| | ${red}= | Convert To Number | ${red} | 0
| | ${green}= | Get From List | ${colour} | 1
| | ${green}= | Convert To Number | ${green} | 0
| | ${blue}= | Get From List | ${colour} | 2
| | ${blue}= | Convert To Number | ${blue} | 0
| | Should be equal as numbers | ${red} | 0
| | Should be equal as numbers | ${green} | 1
| | Should be equal as numbers | ${blue} | 0
| | ${ambient}= | Get From Dictionary | ${json} | ambient
| | Should be equal as numbers | ${ambient} | 0.5
| | ${specular}= | Get From Dictionary | ${json} | specular
| | Should be equal as numbers | ${specular} | 0.2
| | ${diffuse}= | Get From Dictionary | ${json} | diffuse
| | Should be equal as numbers | ${diffuse} | 0.8
| | ${shininess}= | Get From Dictionary | ${json} | shininess
| | Should be equal as numbers | ${shininess} | 50.0

| Check the reflected light when the eye is between the light and the normal from the object
| | ${result}= | run process | python | ./phongTester.py | testEyeAtZero
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${colour}= | Get From Dictionary | ${json} | colour
| | ${red}= | Get From List | ${colour} | 0
| | ${red}= | Convert To Number | ${red} | 1
| | ${green}= | Get From List | ${colour} | 1
| | ${green}= | Convert To Number | ${green} | 1
| | ${blue}= | Get From List | ${colour} | 2
| | ${blue}= | Convert To Number | ${blue} | 1
| | Should be equal as numbers | ${red} | 1.9
| | Should be equal as numbers | ${green} | 1.9
| | Should be equal as numbers | ${blue} | 1.9

| Check the reflected light when the eye is 45 degs away from the normal from the object
| | ${result}= | run process | python | ./phongTester.py | testEyeAt45
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${colour}= | Get From Dictionary | ${json} | colour
| | ${red}= | Get From List | ${colour} | 0
| | ${red}= | Convert To Number | ${red} | 4
| | ${green}= | Get From List | ${colour} | 1
| | ${green}= | Convert To Number | ${green} | 4
| | ${blue}= | Get From List | ${colour} | 2
| | ${blue}= | Convert To Number | ${blue} | 4
| | Should be equal as numbers | ${red} | 1.0
| | Should be equal as numbers | ${green} | 1.0
| | Should be equal as numbers | ${blue} | 1.0

| Check the reflected light when the eye is straight on but the light source is 45 degs away from the normal from the object
| | ${result}= | run process | python | ./phongTester.py | testLightAt45
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${colour}= | Get From Dictionary | ${json} | colour
| | ${red}= | Get From List | ${colour} | 0
| | ${red}= | Convert To Number | ${red} | 4
| | ${green}= | Get From List | ${colour} | 1
| | ${green}= | Convert To Number | ${green} | 4
| | ${blue}= | Get From List | ${colour} | 2
| | ${blue}= | Convert To Number | ${blue} | 4
| | Should be equal as numbers | ${red} | 0.7364
| | Should be equal as numbers | ${green} | 0.7364
| | Should be equal as numbers | ${blue} | 0.7364

| Check the reflected light when the eye is 45 degs from the normal and the light source is 45 degs away from the normal from the object in the opposite direction
| | ${result}= | run process | python | ./phongTester.py | testLightAndEyeAt45
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${colour}= | Get From Dictionary | ${json} | colour
| | ${red}= | Get From List | ${colour} | 0
| | ${red}= | Convert To Number | ${red} | 4
| | ${green}= | Get From List | ${colour} | 1
| | ${green}= | Convert To Number | ${green} | 4
| | ${blue}= | Get From List | ${colour} | 2
| | ${blue}= | Convert To Number | ${blue} | 4
| | Should be equal as numbers | ${red} | 1.6364
| | Should be equal as numbers | ${green} | 1.6364
| | Should be equal as numbers | ${blue} | 1.6364

| Check the reflected light when the eye is in line with the normal vector but the light source is behind it
| | ${result}= | run process | python | ./phongTester.py | testLightBehind
| | ${json}= | evaluate | json.loads('''${result.stdout}''') | json
| | ${colour}= | Get From Dictionary | ${json} | colour
| | ${red}= | Get From List | ${colour} | 0
| | ${red}= | Convert To Number | ${red} | 1
| | ${green}= | Get From List | ${colour} | 1
| | ${green}= | Convert To Number | ${green} | 1
| | ${blue}= | Get From List | ${colour} | 2
| | ${blue}= | Convert To Number | ${blue} | 1
| | Should be equal as numbers | ${red} | 0.1
| | Should be equal as numbers | ${green} | 0.1
| | Should be equal as numbers | ${blue} | 0.1
