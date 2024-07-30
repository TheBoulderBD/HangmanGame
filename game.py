import random

def openFile(file): #creates a list of all the words in the file
    f = open(file)
    word_list = f.read().split()
    return word_list

def chooseWord(word_list): #randomly selects a word
    word = random.choice(words_list)
    return word

def numberDashes(word): #creats the spaces to place letters
    dashes = "_" * len(word)
    return dashes

def updateBoard(word, board, letter): #updates the spaces with correct letters
    for i in range(len(word)): 
        if word[i] == letter:
            board = board[:i] + letter + board[i+1:]
    return board

def checkWin(board): #checks to see if no letters are left
    if "_" not in board:
        return True
    else:
        return False

def drawHangman(guesses): #draws the stick man figure of the hangman
    head = ''
    body = ''
    left_arm = ''
    right_arm = ''
    left_leg = ''
    right_leg = ''
    if guesses < 6:
        head += 'O'
    if guesses == 4:
        body += ' |'
    if guesses < 4:
        left_arm = '/|'
    if guesses < 3:
        right_arm = "\\"
    if guesses < 2:
        left_leg = '/'
    if guesses < 1:
        right_leg = '\\'
    hangman = [
    " ________      ",
    "|        |     ",
    "|        " + head + "     ",
    "|       " + left_arm + body + right_arm + "     ",
    "|       " + left_leg + " " + right_leg + "     ",
    "|              ",
    "|              "
    ]
    for line in hangman:
        print(line)

def playHangman(): #Layout of the game itself
    word = chooseWord(words_list) 
    board = numberDashes(word)
    guesses = 6 #number of attempts
    guessed_letters = []  #stores letter attempts

    print("Welcome to Hangman!")
    print("The word has", len(word), "letters.")
    print(board)

    while guesses > 0:
        guess = input("Guess a letter or the entire word: ").lower()
        if guess == word: #user guessed complete word
            print("Congratulations! You won!")
            break
        elif len(guess) == 1: #user guessed a letter
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in word:
                board = updateBoard(word, board, guess)
                print(board)
                if checkWin(board):
                    print("Congratulations! You won!")
                    break
            else:
                guesses -= 1
                guessed_letters.append(guess)
                print("Wrong letter. You have", guesses, "guesses left.")
                drawHangman(guesses)
        else: #user guessed a wrong word
            guesses -= 1
            print("Wrong word. You have", guesses, "guesses left.")
            drawHangman(guesses)

    if not checkWin(board) and guess != word:
        print("Sorry, you lost. The word was", word)

def playGame(): # Loop for users that choose to play again
    playHangman()
    while True:
        play_again = input("Would you like to play again? y/n? ").lower()

        if play_again == 'y' or play_again == 'yes':
            playHangman()
        elif play_again == 'n' or play_again == 'no':
            break
        else:
            print('Invalid answer')
            break

words_list = openFile('words.txt')

playGame()