__author__ = 'Maxwell Crawford'
#CSC-131
#10/23/2014
#MineCleaner: A rebirth of Minesweeper for Python!

import time #for sleep ani's
import random #generates locations
import winsound #bg music, sounds
import math #for rounding down time

##Define core functions:

#Play Background Music:
def playBGM():
    winsound.PlaySound("Sounds\Battle Royale_short_edit_22k.wav",
                       winsound.SND_ASYNC | winsound.SND_LOOP) #play on async loop

#Stop Background Music:
def stopBGM():
    winsound.PlaySound(None, 0) #stop all

#Play bomb sound effect:
def playBomb():
    winsound.PlaySound("Sounds\_blast.wav", winsound.SND_ASYNC) #play once

#Play Game Win sound:
def playWin():
    winsound.PlaySound("Sounds\gamewin.wav", winsound.SND_ASYNC) #play once

#Play Game Over/Lose sound:
def playLose():
    winsound.PlaySound("Sounds\gamelose.wav", winsound.SND_ASYNC) #play once

#Play 'Thank You' sound:
def playThanks():
    winsound.PlaySound("Sounds\_thankyou.wav", winsound.SND_ASYNC) #play once

#Main Menu function:
def mainMenu():
    #Main Menu:
    mainChoice = 0

    while (mainChoice <= 0):
        print("\n\t* Please choose one of the game board sizes, ")
        print("\t* 1) (Easy) 5x5 ")
        print("\t* 2) (Normal) 6x6 ")
        print("\t* 3) (Hard) 8x8 ")

        try: #just in case number is not entered
            mainChoice = int(input("\n\t* Enter choice (1-3): "))
        except:
            mainChoice = 4

        if (mainChoice < 1) or (mainChoice > 3):
            mainChoice = 0 #reset
            print("\n\t -- Invalid choice. Please enter 1-3 ! --")

    return mainChoice #give int back to main

#Player Name Menu function:
def playerNameMenu():
    #Player Name Menu:
    playerName = ""
    while (len(playerName) != 3):
        playerName = input("\n\t* Please enter your initials[AAA]: ")

        if (len(playerName) != 3):
            print("\n\t\t -- Invalid input. Must be 3 letters long! --")
        else:
            playerName = playerName[:3].upper() #make sure only 3 letters are saved!

    print("\n\t* Your name is: " + playerName)

    return playerName

#Player Movement Menu function:
def playerMoveMenu(mainChoice):
    playerMovement = [0,0] #default spot
    playerInput = ""
    difficulty = mainChoice #store difficulty(1-3)

    #Input Loop (Column, A-J):
    while (playerInput.upper() != 'Q'):
        playerInput = input("\n\t** Please enter the Column[A] of desired spot (or 'Q' to quit):  ")

        #Check for Sentinel:
        if (playerInput.upper() == 'Q'):
            playerMovement = [-1, -1] #sentinel value
            return playerMovement

        #Difficulty Check:
        if (difficulty == 1):
            if (ord(playerInput[0].upper()) > ord('E')): #Easy difficulty
                print("\n\t\t -- Invalid input. Must be between A-E! --")
            else:
                #Check if user entered a letter:
                try:
                    testnum = int(playerInput) #should fail!
                    print("\n\t\t -- Invalid input. Must be a letter! --")
                    continue #skip this iteration
                except:
                    playerMovement[0] = playerInput[0].upper() #save column, only grab first char, as uppercase!
                    break #done
        elif (difficulty == 2):
            if (ord(playerInput[0].upper()) > ord('F')): #Normal difficulty
                print("\n\t\t -- Invalid input. Must be between A-F! --")
            else:
                #Check if user entered a letter:
                try:
                    testnum = int(playerInput) #should fail!
                    print("\n\t\t -- Invalid input. Must be a letter! --")
                    continue #skip this iteration
                except:
                    playerMovement[0] = playerInput[0].upper() #save column, only grab first char, as uppercase!
                    break #done
        elif (difficulty == 3):
            if (ord(playerInput[0].upper()) > ord('H')): #Hard difficulty
                print("\n\t\t -- Invalid input. Must be between A-H! --")
            else:
                #Check if user entered a letter:
                try:
                    testnum = int(playerInput) #should fail!
                    print("\n\t\t -- Invalid input. Must be a letter! --")
                    continue #skip this iteration
                except:
                    playerMovement[0] = playerInput[0].upper() #save column, only grab first char, as uppercase!
                    break #done

    #Input Loop (Row, 1-10):
    while (playerInput.upper() != 'Q'):
        playerInput = input("\n\t** Please enter the Row[#] of desired spot (or 'Q' to quit):  ")

        #Sentinel Check:
        if (playerInput.upper() == 'Q'):
            playerMovement = [-1, -1] #sentinel value
            return playerMovement

        #Difficulty Check:
        if (difficulty == 1):
            #Check if user entered a number:
            try:
                testnum = int(playerInput) / 2 #should fail if not a number
                playerMovement[1] = int(playerInput[0]) #save row, only grab first char, as lowercase!

                if (playerMovement[1] > 0 and playerMovement[1] < 6):
                    break #done
                else:
                    playerMovement[1] = 0 #reset
                    print("\n\t\t -- Invalid input. Must be between 1-5! --")
            except:
                print("\n\t\t -- Invalid input. Must be a number! --")
                continue #skip this iteration
        elif (difficulty == 2):
            #Check if user entered a number:
            try:
                testnum = int(playerInput) / 2 #should fail if not a number
                playerMovement[1] = int(playerInput[0]) #save row, only grab first char, as lowercase!

                if (playerMovement[1] > 0 and playerMovement[1] < 7):
                    break #done
                else:
                    playerMovement[1] = 0 #reset
                    print("\n\t\t -- Invalid input. Must be between 1-6! --")
            except:
                print("\n\t\t -- Invalid input. Must be a number! --")
                continue #skip this iteration
        elif (difficulty == 3):
            #Check if user entered a number:
            try:
                testnum = int(playerInput) / 2 #should fail if not a number
                playerMovement[1] = int(playerInput[0]) #save row, only grab first char, as lowercase!

                if (playerMovement[1] > 0 and playerMovement[1] < 9):
                    break #done
                else:
                    playerMovement[1] = 0 #reset
                    print("\n\t\t -- Invalid input. Must be between 1-8! --")
            except:
                print("\n\t\t -- Invalid input. Must be a number! --")
                continue #skip this iteration


    return playerMovement #finalized grid movement

#Restart Game Menu function:
def restartMenu():
    #Restart Game Menu:
    restartChoice = 0

    while (restartChoice <= 0):
        print("\n\t* Do you wish to start over, or quit the game? ")
        print("\t* 1) Restart ")
        print("\t* 2) Quit ")

        try: #just in case number is not entered
            restartChoice = int(input("\n\t* Enter choice (1-2): "))
        except:
            restartChoice = 3

        if (restartChoice < 1) or (restartChoice > 2):
            restartChoice = 0 #reset
            print("\n\t -- Invalid choice. Please enter 1-2 ! --")

    return restartChoice #give int back to main

#Create Game Board function:
def createBoard(mainChoice):
    #Select Board Size from Main Choice:
    if (mainChoice == 1):
        boardSize = 5
    elif (mainChoice == 2):
        boardSize = 6
    elif (mainChoice == 3):
        boardSize = 8
    else:
        boardSize = 6 #default

    #Use Board Size to Create Game Board:
    gameList = [0] * boardSize #init empty row

    if (boardSize == 5):
        gameBoard = {1:gameList[:], 2:gameList[:], 3:gameList[:], 4:gameList[:], 5:gameList[:]}
    elif (boardSize == 6):
        gameBoard = {1:gameList[:], 2:gameList[:], 3:gameList[:], 4:gameList[:], 5:gameList[:],
                     6:gameList[:]}
    elif (boardSize == 8):
        gameBoard = {1:gameList[:], 2:gameList[:], 3:gameList[:], 4:gameList[:], 5:gameList[:],
                     6:gameList[:], 7:gameList[:], 8:gameList[:]}

    #Setup variables for dimensions of grid...
    outer = len(gameBoard) #all keys
    inner = len(gameBoard[1]) #all rows in first key
    bombCount = 0 #amount of bombs generated...
    bombMax = 0 #set maximum amount of bombs for each difficulty...

    #Set max bombs:
    if (mainChoice == 1):
        bombMax = 7
    elif (mainChoice == 2):
        bombMax = 14
    elif (mainChoice == 3):
        bombMax = 22

    #Randomize bombs based on Main Choice (Difficulty):
    for row in range(1, outer+1):
        for elem in range(inner):
            #Randomize bombs as long as max isn't reached:
            if (bombCount < bombMax):
                gameBoard[row][elem] = random.randint(1,2) #randomize for empty/bomb state
            elif (bombCount >= bombMax):
                gameBoard[row][elem] = 1 #rest of spots will be empty/no more bombs allowed

            #Check if bomb was generated:
            if (gameBoard[row][elem] == 2):
                bombCount += 1 #add to count!

    return gameBoard, boardSize #send initialized board back to main

#Display Game Board function:
def displayBoard(gameBoard, boardSize, mainChoice):
    #Setup variables for length and formatting:
    outer = len(gameBoard) #all keys
    inner = len(gameBoard[1]) #all rows in first key
    centerSpace = int((78.0 / boardSize)) #compensate for varying board sizes...
    topStringMiddle = "| v |" #top divider
    bottomStringMiddle = "| ^ |" #bottom/end divider
    lineSpacerMiddle = '-' #division b/w lines

    #Setup variables for displaying spot types:
    gameEmpty = " " #empty, uncleared spots
    gameBomb = "!" #will be hidden from user until end of game!
    gameClear = "X" #user cleared spots

    #Change column headers depending on grid size:
    if (mainChoice == 1):
        columnLine = "| A |          | B |          | C |          | D |          | E |".center(76, ' ')
        topString = topStringMiddle.center(76, '=')
        bottomString = bottomStringMiddle.center(76, '=')
        lineSpacer = lineSpacerMiddle.center(76, '-')
    elif(mainChoice == 2):
        columnLine = "| A |        | B |        | C |        | D |        | E |        | F |".center(77, ' ')
        topString = topStringMiddle.center(77, '=')
        bottomString = bottomStringMiddle.center(77, '=')
        lineSpacer = lineSpacerMiddle.center(77, '-')
    elif(mainChoice == 3):
        columnLine = "| A |    | B |    | C |    | D |    | E |    | F |    | G |    | H |".center(72, ' ')
        topString = topStringMiddle.center(72, '=')
        bottomString = bottomStringMiddle.center(72, '=')
        lineSpacer = lineSpacerMiddle.center(72, '-')

    #Update screen with Game Board:
    print(topString)
    print(columnLine) #was 78
    for row in range(1, outer+1):
        for elem in range(inner):
            #Add all elements to unified string:
            myLine = " | " #spacer

            if (gameBoard[row][elem] == 1): #check for type of spot on board...
                myLine += gameEmpty
            elif (gameBoard[row][elem] == 2):
                myLine += gameEmpty #invisible!!
            elif (gameBoard[row][elem] == 3):
                myLine += gameBomb #visible
            elif (gameBoard[row][elem] == 4):
                myLine += gameClear

            myLine += " | " #spacer

            #Print finalized line (centered):
            print(myLine.center(centerSpace, ' '), end="")

        #Print row numbers:
        print(str(row), end="") #note: at end to avoid spacing issues after...

        #Spacer to divide Board rows:
        print("")
        if (row < outer):
            print(lineSpacer)

    print(bottomString) #end of board

#Display Rules/Intro function:
def displayIntro():
    print("""\n\t  == The rules of MineCleaner are simple;
    \t  == Don't directly 'step' on any mines, or it's game over!
    \n\t  == Clear the map to win the game, to do this you must choose spots
    \t  == adjacent/next to the mines without hitting them directly. """)

    wait_text1 = input("\n\t -- Press Enter to continue -- ")

    print("""\n\t  == Choosing a spot will 'clear' the spots above/below/next to that
    \t  == spot with a radius of 1.
    \n\t  == Cleared spots show up as an 'X' on the map.
    \n\t  == Some mines may reveal themselves as a '!',
    \t  == so be careful!
    \n\t  == Try to complete the game as fast as possible
    \t  == in order to get a high score!
    \t  == Good luck! """)
    wait_text2 = input("\n\t -- Press Enter to continue -- ")

#Display Bomb Animation function:
def displayBombing():
    #Load Frame 1:
    frame1file = open("Animations\gridbomb1.txt", "r")
    frame1 = frame1file.readlines()
    frame1file.close()

    #Play Frame 1:
    print("\n" * 25)
    for item in range(len(frame1)):
        print(frame1[item], end="")
    time.sleep(1)

    #Load Frame 2:
    frame2file = open("Animations\gridbomb2.txt", "r")
    frame2 = frame2file.readlines()
    frame2file.close()

    #Play Frame 2:
    print("\n" * 25)
    for item in range(len(frame2)):
        print(frame2[item], end="")
    time.sleep(1)

    #Load Frame 3:
    frame3file = open("Animations\gridbomb3.txt", "r")
    frame3 = frame3file.readlines()
    frame3file.close()

    #Play Frame 3:
    print("\n" * 25)
    for item in range(len(frame3)):
        print(frame3[item], end="")
    time.sleep(1)

    #Load Frame 4:
    frame4file = open("Animations\gridbomb4.txt", "r")
    frame4 = frame4file.readlines()
    frame4file.close()

    #Play Frame 4:
    print("\n" * 25)
    for item in range(len(frame4)):
        print(frame4[item], end="")
    time.sleep(1)

#Display Game Clear animation:
def displayWin():
    #Load Frame 1:
    frame1file = open("Animations\gridclear1.txt", "r")
    frame1 = frame1file.readlines()
    frame1file.close()

    #Play Frame 1:
    print("\n" * 25)
    for item in range(len(frame1)):
        print(frame1[item], end="")
    time.sleep(1)

    #Load Frame 2:
    frame2file = open("Animations\gridclear2.txt", "r")
    frame2 = frame2file.readlines()
    frame2file.close()

    #Play Frame 2:
    print("\n" * 25)
    for item in range(len(frame2)):
        print(frame2[item], end="")
    time.sleep(1)

    #Load Frame 3:
    frame3file = open("Animations\gridclear3.txt", "r")
    frame3 = frame3file.readlines()
    frame3file.close()

    #Play Frame 3:
    print("\n" * 25)
    for item in range(len(frame3)):
        print(frame3[item], end="")
    time.sleep(1)

    #Load Frame 4:
    frame4file = open("Animations\gridclear4.txt", "r")
    frame4 = frame4file.readlines()
    frame4file.close()

    #Play Frame 4:
    print("\n" * 25)
    for item in range(len(frame4)):
        print(frame4[item], end="")
    time.sleep(1)

    #Load Winner Text:
    winfile = open("Animations\winner.txt", "r")
    win = winfile.readlines()
    winfile.close()

    #Display Winner Text:
    print("\n" * 6)
    for item in range(len(win)):
        print(win[item], end="")
        time.sleep(1)


#Update Game Board function:
def updateBoard(gameBoard, playerMovement):
    #Invert Player Movement for Proper Board Spot Placement:
    temp_x = playerMovement[0]
    temp_y = playerMovement[1]
    playerMovement[0] = temp_y
    playerMovement[1] = temp_x

    #Convert Player Movement into Board Spot:
    if(playerMovement[1] == 'A'): #COLUMNS/KEY
        playerMovement[1] = 1
    elif(playerMovement[1] == 'B'):
        playerMovement[1] = 2
    elif(playerMovement[1] == 'C'):
        playerMovement[1] = 3
    elif(playerMovement[1] == 'D'):
        playerMovement[1] = 4
    elif(playerMovement[1] == 'E'):
        playerMovement[1] = 5
    elif(playerMovement[1] == 'F'):
        playerMovement[1] = 6
    elif(playerMovement[1] == 'G'):
        playerMovement[1] = 7
    elif(playerMovement[1] == 'H'):
        playerMovement[1] = 8
    elif(playerMovement[1] == 'I'):
        playerMovement[1] = 9
    elif(playerMovement[1] == 'J'):
        playerMovement[1] = 10

    #playerMovement[1] -= 1 #ROWS, go back a number...

    #Check type of spot on Game Board:
    x = playerMovement[0]
    y = (playerMovement[1] - 1)
    x_limit = len(gameBoard[1])
    y_limit = len(gameBoard[1])

    if (gameBoard[x][y] == 1): #Empty
        print("\n\t\t -= Nice, you cleared a spot! =-")
        time.sleep(1)

        #Clear spots on mark, above, below, left, and right (if applicable):
        try:
            gameBoard[x][y] = 4
        except:
            print("") #pass
        try:
            if (y <= y_limit): #don't go over limit
                gameBoard[x][y+1] = 4
        except:
            print("") #pass
        try:
            if (y > 0):
                gameBoard[x][y-1] = 4
        except:
            print("") #pass
        try:
            if (x > 1):
                gameBoard[x-1][y] = 4
        except:
            print("") #pass
        try:
            if (x < x_limit):
                gameBoard[x+1][y] = 4
        except:
            print("") #pass

        #Show 'hint' bomb spots on adjacent areas:
        try:
            if (gameBoard[x-1][y+1] == 2):
                gameBoard[x-1][y+1] = 3 #now visible!
        except:
            print("") #pass
        try:
            if (gameBoard[x-1][y-1] == 2):
                gameBoard[x-1][y-1] = 3 #now visible!
        except:
            print("") #pass
        try:
            if (gameBoard[x+1][y+1] == 2):
                gameBoard[x+1][y+1] = 3 #now visible!
        except:
            print("") #pass
        try:
            if (gameBoard[x+1][y-1] == 2):
                gameBoard[x+1][y-1] = 3 #now visible!
        except:
            print("") #pass

        #Check if all spots are cleared:
        all_clear = 0 #if this goes to 1 and stays 1, board is cleared!
        outer = len(gameBoard) #all keys
        inner = len(gameBoard[1]) #all rows in first key
        for row in range(1, outer+1):
            for elem in range(inner):
                if(gameBoard[row][elem] == 4):
                    all_clear = 1 #current spot is clear
                else:
                    all_clear = 0 #not clear
                break #done searching

        if (all_clear == 0):
            return 0
        elif (all_clear == 1): #WIN!
            stopBGM() #end music
            playWin() #congratulations sound!
            displayWin() #show winner animation!
            return 1

    elif (gameBoard[x][y] == 2) or (gameBoard[x][y] == 3): #Bomb
        stopBGM() #end music
        playBomb() #bomb blast
        displayBombing() #show bomb animation!
        playBomb() #bomb blast
        print("\n\t\t -- Oh no, you hit a bomb!! --")
        time.sleep(1)
        return 2
    elif (gameBoard[x][y] == 4): #Clear
        print("\n\t\t -- Spot already cleared!! --")
        time.sleep(1)
        return 0

#Read Scores function:
def readScores():
    #Get Current Scores from File:
    scoresList = []
    scoresFile = open("MineScores.txt", "r")
    myLines = scoresFile.readlines()
    scoresFile.close()

    for item in myLines:
        scoresList.append(item.split('\t'))

    return scoresList

#Post Score to Roster function:
def postScore(scoreRank, scoreName, scoreAmount, scoresList):
    #Iterate Thru Current Scores List and Replace Current Score:
    for scores in range(1, 6):
        if (scoreRank == scores):
            scoresList[scores][1] = scoreName
            scoresList[scores][2] = str(scoreAmount) + '\n'

    #Write Updated List to File:
    scoresFile = open("MineScores.txt", "w")
    outputText = ""
    for item in range(len(scoresList)):
        for items in range(len(scoresList[item])):
            outputText += scoresList[item][items].strip('\n')
            outputText += "\t"
        #print(" ") #spacer
        outputText += "\n"

    scoresFile.write(outputText)
    scoresFile.close()

    return scoresList

# Main Program Function:
def main():
    #Title:
    print("\n\t\t--=== Welcome to MineCleaner !! ===--")

    #Hold Status of Program (0=play, 1=quit):
    playStatus = 0

    #Main Program Loop:
    while (playStatus <= 0):
        #Hold Status of Game (0=neutral, 1=win, 2=lose/over):
        gameStatus = 0

        #Main Menu:
        mainChoice = mainMenu() #call func.

        #Player Name Menu:
        playerName = playerNameMenu() #call func.

        #Initialize Game Board from Menu Choice:
        gameBoard, boardSize = createBoard(mainChoice)

        #Initialize BGM:
        playBGM()

        #Display Rules/Intro:
        displayIntro()

        #Animate beginning text:
        begText1 = "\n\t\t--== Let the games ... ==--"
        begText2 = "\t\t--==    BEGIN !!!      ==--\n"
        print(begText1)
        time.sleep(1)
        print(begText2)
        time.sleep(3) #for dramatic effect...

        #Game Loop (depending on Status of Game):
        startTime = time.time() #STARTING TIME for scoring
        playTime = 0 #placeholder for ending time
        while (gameStatus == 0):
            #Display the Game Board:
            displayBoard(gameBoard, boardSize, mainChoice)

            #Player Movement Menu:
            playerMovement = playerMoveMenu(mainChoice) #call func. to list, to hold player's spot

            #Check for User Quit:
            if (playerMovement[0] == -1) and (playerMovement[1] == -1):
                gameStatus = 2 #end game!
            else:
                #Make movement on Game Board:
                gameStatus = updateBoard(gameBoard, playerMovement)

            #Check if Game Over/Win (0=neutral, 1=win, 2=lose/gameover):
            if (gameStatus != 0):
                break #end game loop

        #Game Win:
        if (gameStatus == 1):
            playTime = math.floor(time.time() - startTime) #ENDING TIME for scoring
            print("\n\t --== You won!! ==--\n")
            time.sleep(1)

        #Game Over:
        elif (gameStatus == 2):
            playTime = math.floor(time.time() - startTime) #ENDING TIME for scoring #COMMENT OUT LATER
            playLose() #gameover sound!
            print("\n\t --== You lost :( ==--\n")
            time.sleep(1)

        #Perform Scoring Operations (Only if player Won):
        if (gameStatus == 1):
            #Calculate Player's Score:
            scoreName = playerName[:] #grab previously used initials
            if (playTime < 10): #HIGHEST BONUS
                lastdigit = (playTime % 10)
                remainder = (10 - lastdigit) + 1
                scoreAmount = (remainder * 1500)

            elif (playTime >= 10) and (playTime < 30): #High Bonus
                remainder = 30 - playTime
                lastdigit = (playTime % 10)
                small_remainder = (10 - lastdigit) + 1
                scoreAmount = (remainder * 140) + (small_remainder * 25)

            elif (playTime >= 30) and (playTime < 100): #Smaller Bonus
                remainder = 100 - playTime
                lastdigit = (playTime % 10)
                small_remainder = (10 - lastdigit) + 1
                scoreAmount = (remainder * 25) + (small_remainder * 20)

            elif (playTime >= 100): #Scoring for all else/long play times
                lastdigit = (playTime % 10)
                small_remainder = (10 - lastdigit) + 1
                scoreAmount = math.ceil(playTime / 10) + (small_remainder * 60)

            #Display Current Score (Only if player Won):
            print("You played for: " + str(playTime) + " seconds!")
            print("Your name is " + scoreName + " and you scored " + str(scoreAmount) + " points!")
            scores_wait_text = input("\n\t -- Press Enter to continue -- ")

            #Check Current Score Against Roster:
            scoresList = readScores()
            scorePost = 0 #flag, 0=do not post, 1=post
            scoreRank = 0 #placeholder for scoreboard rank
            for scores in range(1, 6):
                if (scoreAmount > int(scoresList[scores][2].strip('\n'))): #remove newline chars, only check scores
                    scorePost = 1 #flag true
                    scoreRank = scores #rank on roster
                    break #end loop

            #Post Score (if applicable to Top 10):
            if (scorePost == 1):
                scoresList = postScore(scoreRank, scoreName, scoreAmount, scoresList)

            #Display New Score Roster:
            print("\n\t ===   TOP   SCORES   ===")
            for item in range(len(scoresList)):
                for items in range(len(scoresList[item])):
                    print(scoresList[item][items], end="\t") #print each separate item, formatted
                print(" ") #spacer
            time.sleep(2)

        #Restart Game Menu:
        restartChoice = restartMenu()
        if (restartChoice == 1):
            playStatus = 0
            #continue
        elif (restartChoice == 2):
            playStatus = 1 #end main loop!

    #Say Goodbye!:
    playThanks() #thank you sound!
    print("\n\n\t --------/--------/-------/--/--")
    time.sleep(1)
    print("\t ------/-/-----/-/--/-----/--/--")
    time.sleep(1)
    print("\t /----//----/-/--/--/-//----/---")
    time.sleep(1)
    print("\t /-/-/--/-//---/-///-////-////-/")
    time.sleep(1)
    print("\t ///-/////////-//////-//////-///")
    time.sleep(1)
    print("\t ///////////////////////////////")
    time.sleep(1)
    print("\t //// Thanks for playing! :) ///")


#Initiate program:
main()



