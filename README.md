# MasterMind
It's a code-breaker game, that intended to be a Player vs Player game, originally invented as a board game 
in 1970 by Mordecai Meirowitz. As it's a virtual version of this game, the player that was responsible to 
make a code is replaced by an AI.

The game contains things like:

 - A decoding board 
    - equipped with a cover at one end which hides the generated code (of 4 colors),
    - up to 12 rows of attempts' holes for *code pegs*
    - each row has a space for *key pegs* 
 - Code pegs - used for decoding
 - Key pegs - used as hint of correctness

## Rules
- Players decide how many rounds will be played (must be even number)
- A Codemaker (AI in this case) chooses a pattern of four code pegs (colors may repeat)
- A code is placed in covered holes so the Codebreaker won't see it
- Codebreaker tries to guess hidden code in both color and order within up to 12 rounds
- Once a Codebreaker places the code on board a codemaker provides feedback by placing from zero to four *key pegs*
- One black *key peg* indicates that one of the *code pegs* is placed correctly both in position and color
- One white *key peg* indicates that one color of *code pegs* is in the code, but is in the wrong position
- If there are duplicate colors in the guess, they cannot all be awarded a *key peg* unless there is 
the same ammount of same *code pegs* in both, hidden code and guess code
- Once feedback is provided, another attempt is made
- The Codemaker gets one point for each guess the Codebreaker makes.
- If Codebreaker is unable to geuss the code Codemaker gets an extra point
- The winner is the one who has the most points after the agreed-upon number of games.

In this solution it was decided that a player gets a point every attempt of guess he makes. The less points 
player get the better the result is.

### To do
- [ ] Write tests that checks every rule using `unittest`
- [ ] Write tests that covers every *key peg* feedback using `unittest`
- [x] Implement (hidden) code generator
- [ ] Implement codebraker's guessing board
- [ ] Implement codemaker's feedback
- [ ] Implement observer pattern
- [ ] Implement console interface
- [ ] Implement GUI