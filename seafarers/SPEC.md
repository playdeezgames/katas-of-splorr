# Seafarers of SPLORR!! Kata

* User Story: As a player, I want to explore a rich, open ocean filled with islands using my ship
  * Ships Exist
    * Ships have an (x,y) position 
      * defaults to (0,0)
    * Ships have a heading (in degrees) that 
      * defaults to 0: 
      * greater than or equal to 0 
      * less than 360 (in degrees)
      * values outside of this range should "wrap around"
        * i.e. 360 == 0, 361 == 1, -1 == 359, etc
    * Ships have a speed
      * defaults to 1
      * greater than or equal to 0 
      * less than or equal to 1
      * Values outside of this range should clamp.
    * Ship should move according to heading and direction
      * With a speed of 1
        * a heading of 0 moves the ship +1 y
        * a heading of 90 moves the ship +1 x
        * a heading of 180 moves the ship -1 y
        * a heading of 270 moves the ship -1 x
        * ```hint: deltax = sin(heading) * speed```
        * ```hint: deltay = cos(heading) * speed```
  * Islands Exist
    * Islands have an (x,y) position 
      * must be defined when the island is created
  * Ships with Islands
    * A Ship can "see" an island that is no more than 10 units away
      * ```hint: c ^ 2 = a ^ 2 + b ^ 2```
    * A Ship can "dock" with an island that is no more than 1 unit away
    * A Ship cannot move when docked
      * ```hint: probably want to have a way to 'undock'?```
    * A Ship can determine a valid heading that will lead to a given island
      * ```hint: math.atan2(deltax, deltay)```
    * A Ship can determine a distance to a given island
    * A Ship counts the number of moves it has made
    * A Ship tracks how many visits it has made to a given island. 
      * A visit is counted as docking with the island.
    * A Ship tracks which move it last visited an island.