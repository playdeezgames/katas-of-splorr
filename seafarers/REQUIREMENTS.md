# Seafarers of SPLORR!! Kata

## User Story: As a player, I want to explore a rich, open ocean filled with islands using my ship

### Ships Exist

#### Ships have an (x,y) position that defaults to (0,0)

#### Ships have a heading that defaults to 0: greater than or equal to 0 and less than 360 (in degrees), values outside of this range should wrap around

#### Ships have a speed that defaults to 1: greater than or equal to 0 and less than or equal to 1. Values outside of this range should clamp.

#### Ship should move according to heading and direction. With a speed of 1, a heading of 0 moves the ship +1 y, a heading of 90 moves the ship +1 x.