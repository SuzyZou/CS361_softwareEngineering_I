import random
import time

numberOfQuestions = 5

def welcomeScreen():
    print(f"\n\n\n\t\tWelcome to my game\n")
    print(f"The way this game works is that you will be presented with {numberOfQuestions} math questions")
    print("The purpose of this game is to allow for keeping the brain sharp and quick")
    print(f"The math questions will contain + - and *")
    print(f"The scores will be calculated based off of difficulty")
    print(f"\t-multiplication will result in two points added to your score for a correct answer")
    print(f"\t-addition and subtraction will result in one point added to your score for a correct answer")
    print("During the game, you can press 'r' to return back to the main menue")

    print("Would you like to immediately jump into the game, or would you like to go to the options screen first?")
    print("Type '1' to immediately going to game, type '2' to first go options screen")
 
    while True:
        userInput = input()
        try:
            userInput = int(userInput)
            if userInput in [1,2]:
                break
            print("That was not one of the valid options.")
            print("Type '1' to immediately going to game, type '2' to first go options screen")
        except:
            print("That was not one of the valid options.")
            print("Type '1' to immediately going to game, type '2' to first go options screen")


    if userInput == 1:
        playGame()
    else:
        optionsScreen()


def gameInformation():
    print("Game Information:")
    print("\tThe purpose of this game is to allow the user to practice their quick thinking mental math")
    print("\tAs we age, it is important to keep working the mind such that it does not start to deteriorate.")
    print("\tThis game attempts to allow users a simple method of playing quick and short matches such that it is accessable for a little bit each day.")
    userInput = input("\n\ntype any number to go back to the option menue\n")
    optionsScreen()

def advancedOptions():
    global numberOfQuestions

    print("Advanced Options:")
    print("\t1. Adjust number of rounds per game")
    print("\t2. Go back")

    
    while True:
        userInput = input("Please select the option you would like\n")
        try:
            userInput =  int(userInput)
            if userInput in [1, 2]:
                break
            else:
                print("Sorry, that was not a valid option, please type one of the numbers corresponding to the option you wish to select")

        except:
            print("Sorry, that was not a valid option, please type one of the numbers corresponding to the option you wish to select")

    if userInput == 1:
        while True:
            userInput = input("How many rounds would you like to play per game (enter a number between 1 and 20)\n")
            try:
                userInput = int(userInput)
                if userInput < 20 and userInput > 0:
                    break
                else:
                    print("Sorry, those numbers are outside of the bounds of the acceptable range. Please select a number between 1 and 20")
            except:
                print("Sorry, that was not an acceptable response. Please enter an integer number between 1 and 20")

        numberOfQuestions = userInput
        print("The number of rounds per game has been updated. Now returning to the options screen")
    optionsScreen()


def optionsScreen():
    print(f"Welcome to the Options Screen")
    print("Please type a number corresponding to the option you wish to select:")
    print("1. Play Game")
    print("2. Read game Information")
    print("3. Advanced Options")
    print("4. More questions")
    print("5. Quit the game")

    while True:
        userInput = input()
        try:
            userInput =  int(userInput)
            if userInput in [1, 2, 3, 4,5]:
                break
            else:
                print("Sorry, that was not a valid option, please type one of the numbers corresponding to the option you wish to select")

        except:
            print("Sorry, that was not a valid option, please type one of the numbers corresponding to the option you wish to select")

    if int(userInput) == 1:
        playGame()
    if int(userInput) == 2:
        gameInformation()
    if int(userInput) == 3:
        advancedOptions()
    if int (userInput) == 4:
        AskMorequestions()
    if int(userInput) == 5:
        quit()

       
def AskMorequestions():
    while True:
        diffapproach = input("Select the option you would like \n1. Print Our Contact Information\n2. Leave your message here \n")
        if diffapproach == "1":
            print("24 hours emergency line:1134556")
            userOption = input("Do you want to go back the game?(yes/no): ").lower().strip()
            if userOption == "yes":
                optionsScreen()
            else:
                print("Thank you for playing the Math Game!")
                break 
        elif diffapproach == '2':
            userResponse = input("Are you sure you want to leave your feedback here? (yes/no): ").lower().strip()
            if userResponse == "yes":
                question = input("Please type your questions here: ")
                with open("user_questions.txt", "a") as file:
                    file.write(question + "\n")
                print("Your questions have been sumbited, an agent will deal with your questons soon.")
                print("Thanks for your time!")
                userOption = input("Do you want to go back the game?(yes/no): ").lower().strip()
                if userOption == "yes":
                    optionsScreen()
                else:
                    print("Thank you for playing the Math Game!")
                    break 
            elif userResponse == "no":
                print("Thank you for playing the Math Game!")
                break
            else:
                print("Invalid input. Please answer with 'yes' or 'no'.")
        else:
            print("Invalid input. Please answer with '1' or '2'.")

def generateQuestion(questionNumber, score):
    operator = random.choice(['+', '-', '*'])
    
    if operator == '*':
        firstNumber = random.randint(1,10)
        secondNumber = random.randint(1,10)
    else:
        firstNumber = random.randint(1,20)
        secondNumber = random.randint(1,20)

    
    #get answer from user and verify that it is an int
    while True:
        userAnswer = input(f"Question {questionNumber + 1}: {firstNumber} {operator} {secondNumber} = ")
        if userAnswer == 'r':
            print("Are you sure you want to end this game?")
            print("Ending the game will erase your current score?")
            userInput = input("Type 1 for yes, type 2 for no\n")
            if userInput == '1':
                optionsScreen()
            continue
        try:
            userAnswer =  int(userAnswer)
            break

        except:
            print("Answer must be an integer value")

    answer = calculateAnswer(firstNumber, secondNumber, operator)

    if int(answer) == int(userAnswer):
        print("Correct!")

        if(operator == '*'):
            score = score + 2
        else:
            score = score + 1

    else:
        print("Incorrect")

    return score


def calculateAnswer(firstNumber, secondNumber, operator):
    #find the operator
    if operator == '+':
        return firstNumber + secondNumber
    
    if operator == '-':
        return firstNumber - secondNumber
    
    if operator == '*':
        return firstNumber * secondNumber
    

def playGame():
    score = 0
    for i in range(numberOfQuestions):
        score = generateQuestion(i, score)

    print("Game finished")
    print(f"Your score is: {score}")

    optionsScreen()

    
def main():
    welcomeScreen()
    


if __name__ == "__main__":
    main()
    