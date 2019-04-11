# Tic Tac Toe for 2 human players
player1 = "x"
player2 = "o"

isWinner = False

playerTurn = 1
turns = 0
field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

# Rendering the field
def writeField(field):
    output = "-------------" + "\n"
    for z in field:
        output = output + "|"
        for y in z:
            output = output + " " + y + " |" 
        output = output + "\n" + "-------------" + "\n" 
    print (output)

# Check if someone has wone the game
def hasWon (field):
    # Check horizontal
    for row in field:
        if row[0] == row[1] and row[1] == row[2] and row[1] != " ":
            print ("End of the match. Winner is " + row[0])
            return True

    # Check vertical
    if (field[0][0] == field[1][0] and field[1][0] == field[2][0] and field [1][0] != " "):
        print ("End of the match. Winner is " + field[1][0])
        return True
    elif (field[0][1] == field[1][1] and field[1][1] == field[2][1] and field [1][1] != " "): 
        print ("End of the match. Winner is " + field[1][1])
        return True
    elif (field[0][2] == field[1][2] and field[1][2] == field[2][2] and field [1][2] != " "):
        print ("End of the match. Winner is " + field[1][2])
        return True

    # Check diagonal
    if (field[0][0] == field[1][1] and field[1][1] == field[2][2] and field [1][1] != " ") or (field[0][2] == field[1][1] and field[1][1] == field[2][0] and field [1][1] != " "):
        print ("End of the match. Winner is " + field[1][1])
        return True
    
    if turns == 9:
        print ("Unentschieden")
        return True

    return False

# Save the choice of the user
def saveChoice(choice, player):
    if choice == 1:
        field[0][0] = player
    if choice == 2:
        field[0][1] = player
    if choice == 3:
        field[0][2] = player
    if choice == 4:
        field[1][0] = player
    if choice == 5:
        field[1][1] = player
    if choice == 6:
        field[1][2] = player
    if choice == 7:
        field[2][0] = player
    if choice == 8:
        field[2][1] = player
    if choice == 9:
        field[2][2] = player

# Check free fields
def checkFreeFields(field):
    freeFields = ""
    if field[0][0] == " ":
         freeFields = freeFields + "1 "
    if field[0][1] == " ":
        freeFields = freeFields + "2 "
    if field[0][2] == " ":
        freeFields = freeFields + "3 "
    if field[1][0] == " ":
        freeFields = freeFields + "4 "
    if field[1][1] == " ":
        freeFields = freeFields + "5 "
    if field[1][2] == " ":
        freeFields = freeFields + "6 "
    if field[2][0] == " ":
        freeFields = freeFields + "7 "
    if field[2][1] == " ":
        freeFields = freeFields + "8 "
    if field[2][2] == " ":
        freeFields = freeFields + "9 "
    return freeFields

# Start playing
print("Let's play Tic Tac Toe!")
fieldrules = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
writeField(fieldrules)

while not isWinner:
    if playerTurn == 1:
        writeField(field)
        freeFields = checkFreeFields(field)
        choice = int(input("Player X: It's your turn. Please enter a number from the following: " + freeFields))
        saveChoice(choice, player1)
              
    if playerTurn == 2:
        writeField(field)
        freeFields = checkFreeFields(field)
        choice = int(input("Player O: It's your turn. Please enter a number from the following: " + freeFields))
        saveChoice(choice, player2)
          
    # Toggle player and count the turns
    if playerTurn == 1:
        playerTurn = 2
    else:
        playerTurn = 1

    turns = turns + 1

    # Check if there is a winner
    isWinner = hasWon(field)
    
writeField(field)   