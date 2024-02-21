# Seafarers of SPLORR!! Kata

| Compass Point | Delta X | Delta Y |
|---------------|---------|---------|
| 0             | 0.0000  | 1.0000  |
| 1             | 0.1951  | 0.9808  |
| 2             | 0.3827  | 0.9239  |
| 3             | 0.5556  | 0.8315  |
| 4             | 0.7071  | 0.7071  |
| 5             | 0.8315  | 0.5556  |
| 6             | 0.9239  | 0.3827  |
| 7             | 0.9808  | 0.1951  |
| 8             | 1.0000  | 0.0000  |
| 9             | 0.9808  | -0.1951 |
| 10            | 0.9239  | -0.3827 |
| 11            | 0.8315  | -0.5556 |
| 12            | 0.7071  | -0.7071 |
| 13            | 0.5556  | -0.8315 |
| 14            | 0.3827  | -0.9239 |
| 15            | 0.1951  | -0.9808 |
| 16            | 0.0000  | -1.0000 |
| 17            | -0.1951 | -0.9808 |
| 18            | -0.3827 | -0.9239 |
| 19            | -0.5556 | -0.8315 |
| 20            | -0.7071 | -0.7071 |
| 21            | -0.8315 | -0.5556 |
| 22            | -0.9239 | -0.3827 |
| 23            | -0.9808 | -0.1951 |
| 24            | -1.0000 | -0.0000 |
| 25            | -0.9808 | 0.1951  |
| 26            | -0.9239 | 0.3827  |
| 27            | -0.8315 | 0.5556  |
| 28            | -0.7071 | 0.7071  |
| 29            | -0.5556 | 0.8315  |
| 30            | -0.3827 | 0.9239  |
| 31            | -0.1951 | 0.9808  |

* User Story: As a player, I want to explore a rich, open ocean filled with islands using my ship
  * Ships Exist
    * Ships have an (x,y) position 
      * defaults to (0,0)
    * Ships have a heading (in compass points) that 
      * defaults to 0 (due north): 
      * greater than or equal to 0 
      * less than 32
      * is an integer!
      * values outside of this range should "wrap around"
        * i.e. 32 == 0, 33 == 1, -1 == 31, etc
    * Ships have a speed
      * defaults to 1
      * greater than or equal to 0 
      * less than or equal to 1
      * Values outside of this range should clamp.
    * Ship should move according to heading and direction
      * With a speed of 1
        * a heading of 0 moves the ship +speed y
        * a heading of 8 moves the ship +speed x
        * a heading of 16 moves the ship -speed y
        * a heading of 24 moves the ship -speed x
        * TODO: lookup table for compass point to deltax/deltay
  * Islands Exist
    * Islands have an (x,y) position 
      * must be defined when the island is created
  * Ships with Islands
    * A Ship can "see" an island that is no more than 10 units away
      * ```hint: c ^ 2 = a ^ 2 + b ^ 2```
    * A Ship can "dock" with an island that is less than 2 units away
    * A Ship cannot move when docked
    * A Ship must "undock" to move again once it has docked 
    * A Ship can determine a rough heading that will lead to a given island
      * Need only return compass points 0 (north), 4 (north-east), 8 (east), 12 (south-east), 16 (south), 20 (southwest), 24 (west), or 28 (northwest) 
    * A Ship can determine a distance to a given island
    * A Ship counts the number of moves it has made
    * A Ship tracks how many visits it has made to a given island. 
      * A visit is counted as docking with the island.
    * A Ship tracks which move it last visited an island.