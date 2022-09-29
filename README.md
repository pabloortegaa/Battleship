# Battleship
Each player's fleet contains 5 different ships:

  •	Carrier (5 holes)
  
  •	Battleship (4 holes)
  
  •	Cruiser (3 holes)
  
  •	Destroyer (2 holes)
  
Rules for placing ships:
  •	Place each ship in any horizontal or vertical position but not diagonally.
  •	Don't place a ship so that any part of it overlaps letters, numbers, the edge of the grid or another ship.
  •	Don't change the position of any ships once the game has begun.
You and your opponent will alternate turns, calling out one shot per turn to try to hit each other's ships. On your turn, pick a target hole and call out its location by letter and number. When you call a shot, your opponent must tell you whether your shot is a hit or a miss.
  •	Hit: Your opponent tells you which ship you have hit (cruiser, submarine, battleship, etc..). Record your hit by placing a red peg on your target grid. Your opponent places a red peg in the corresponding hole of the ship on his ocean grid.
  •	Miss: Record your miss by placing a white peg in the corresponding target hole on your target grid, so you will remember this location and won't call this shot again.
Once all the holes in any one ship are filled with red pegs, the ship will sink. The owner of that ship must announce which ship was sunk. If you are the first player to sink your opponent's entire fleet of 5 ships, you win the game.
Algorithms and Databases that we have to include:
  •	Arrays and sequential search
  •	Insert sort and bubble sort
  •	Linked lists
  •	Recursion, divide and conquer
  •	Binary search
  •	Merge sort
  •	Multidimensional arrays
  •	Matrix: Matrices can be included as the representation of the board of the game. 2D array. 
  •	Stacks and queues
  When the player misses their shot, it stacks that slot (For example, if A5 is water it takes it out of the game (We can't shoot that slot again) and stacks it)
  Every time the player clicks on a square, it gets queued and at the end of the game shows the path (every square hit by the player). Let's say the player wins the game after 47 tries, the output then shows every single attempt the player made.
  •	Library
  Converts letters to numbers (For easier user input and understanding). Instead of writing [1,1], the user will give [A,1] as an input which is transformed into the matrix format with numbers.
  •	Heaps
  Place ships for both player and computer as well as getting the randomness of the computer choices
 

