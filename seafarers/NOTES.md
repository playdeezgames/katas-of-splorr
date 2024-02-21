# Common Approach

Test #1: Add ```X``` and ```Y``` to ```Ship``` class
* flex: I can add a field/property with a default value and check that field/property 

Test #2: Add ```Heading``` to ```Ship``` class with a default value
* flex: I can add a field/property with a default value and check that field/property

Test #3: Add ```SetHeading``` method to ```Ship``` class and do wrap around boundaries with 0 and 360
* flex: I can add a method that takes a parameter
* flex: I can use modulo to round, or equivalent logic
  * Python's ```%``` works like a champ here

Test #4: Add ```Speed``` to ```Ship``` class with a default value
* flex: I can add a field/property with a default value and check that field/property

Test #5: Add ```SetSpeed``` method to ```Ship``` class and do clamp limits with 0 and 1
* flex: I can add a method that takes a parameter
* flex: I can clamp a value
  * Used ```min``` and ```max``` for "canonical" implementation

Test #6: Add ```Move``` method to ```Ship``` class
* flex: I can convert degrees to radians
* flex: I know what ```cos``` and ```sin``` do

Test #7: Add ```Island``` class that initializes ```X``` and ```Y```
* flex: I can create a class
* flex: I can add a constructor
* flex: I can add a field/property with a default value and check that field/property

Test #8: ```Ship``` can see ```Island``` at a maximum distance
* flex: I can add a method that takes a parameter
* flex: I know the distance formula

  TODO: send a list of islands to the ship, and return a list that is visible

Test #9: ```Ship``` can determine dockworthiness to an ```Island``` at a maximum distance
* flex: I can add a method that takes a parameter
* flex: I know the distance formula

  TODO: send a list of islands to the ship, and return a list that can be docked at

Test #10: ```Ship``` cannot move when docked to an ```Island```
* flex: I can add a method that takes a parameter
* flex: I can add a field/property with a default value and check that field/property
* flex: Modify method to add conditional behavior

  TODO: an ```Undock``` action is implied, so make it explicit

Test #11: ```Ship``` can determine heading towards ```Island```
* flex: I can add a method that takes a parameter
* flex: I know how ```math.atan2``` works

Test #12: ```Ship``` can determine distance to ```Island```
* flex: I can add a method that takes a parameter
* flex: I know the distance formula

Test #13: ```Ship``` counts moves made
* flex: I can add a field/property with a default value and check that field/property
* flex: Modify method to add behavior

Test #14: ```Ship``` counts visits with ```Island```
* flex: I can add a field/property with a default value and check that field/property
* flex: I can add a method that interprets/calculates an aggregate

Test #15: ```Ship``` tracks the time it visits an ```Island```
* flex: I can add a method that interprets/calculates an aggregate
* flex: I can refactor a field/property to add new functionality

# Trial Run #1: BH

Got as far as "Ship should move"

Flew through the "add a field/property" and "setter method" tests.

Discovered the amazing thing that is Python's ```%```

Used ```min``` and ```max``` to clamp speed

Major snag was hit during the move function, because BH ain't a trig person.

Important Lesson: Just because I hang out with game devs that all know trig, that doesn't mean I can assume that trig knowledge is common place in other areas of software development.

# Trial Run #2: AL

Got as far as "Ship should move"

Flew through the "add a field/property" and "setter method" tests.

Used an ```if``` and ```elif``` chain for wrapping around the heading.

Used an ```if``` and ```elif``` chain for clamping speed

AL was also not a trig person, so hit the same snag during the move test.

# "Improvements?"

Use compass points instead of degrees?

Floating point rounding errors required strange test fixture values like ```6.123233995736766e-17```