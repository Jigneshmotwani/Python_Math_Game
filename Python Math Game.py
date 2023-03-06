import random
import operator
import turtle
import time
import threading
import random
n = 0
ti = 20 # set timer


def countdown():
    # global ti control the loop from main function
    # global switch not neccesary 
    global ti
    ti = 20
    # timer countdown
    # if timer is still counting, run loop
    while ti > 0:
        # display time in 24hr format
        mins, secs = divmod(ti, 60)
        timer = ''
        # time displayed to 2d.p.
        timer = '{:02d}:{:02d}\n'.format(mins, secs)
        print(timer)
        # ensure time runs like actual clock
        # prevents time from deducting too fast
        time.sleep(1)
        # time reduced by 1 second everytime 
        # it passes through loop
        ti = ti - 1
    # when timer runs out, escape loop and print the following
    print("\nTime is up!! Key in any number to continue")

# function for addition level 1
def addition_1():
    # create a dictionary with addition operator
    operators = {'+': operator.add}
    # generate 2 random numbers
    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    # generate a random operator
    operation = random.choice(list(operators.keys()))
    # answer when combining the randomly generated number and operator
    answer = (operators.get(operation)(num_1, num_2))
    print(f"What is {num_1} {operation} {num_2}?")
    return answer

def addition_2():
    operators = {'+': operator.add}

    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)
    operation = random.choice(list(operators.keys()))
    answer = (operators.get(operation)(num_1, num_2))
    print(f"What is {num_1} {operation} {num_2}?")
    return answer

def addition_3():
    operators = {'+': operator.add}

    num_1 = random.randint(1, 1000)
    num_2 = random.randint(1, 1000)
    operation = random.choice(list(operators.keys()))
    answer = (operators.get(operation)(num_1, num_2))
    print(f"What is {num_1} {operation} {num_2}?")
    return answer

def subtraction_1():
    operators = {'-': operator.sub}

    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    operation = random.choice(list(operators.keys()))
    answer = (operators.get(operation)(num_1, num_2))
    print(f"What is {num_1} {operation} {num_2}?")
    return answer

def subtraction_2():
    operators = {'-': operator.sub}

    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)
    operation = random.choice(list(operators.keys()))
    answer = (operators.get(operation)(num_1, num_2))
    print(f"What is {num_1} {operation} {num_2}?")
    return answer

def subtraction_3():
    operators = {'-': operator.sub}

    num_1 = random.randint(1, 1000)
    num_2 = random.randint(1, 1000)
    operation = random.choice(list(operators.keys()))
    answer = (operators.get(operation)(num_1, num_2))
    print(f"What is {num_1} {operation} {num_2}?")
    return answer

def multiplication_1():
    operators = {'*': operator.mul}

    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    operation = random.choice(list(operators.keys()))
    answer = (operators.get(operation)(num_1, num_2))
    print(f"What is {num_1} {operation} {num_2}? Leave your answer to 1d.p.")
    return answer

def multiplication_2():
    operators = {'*': operator.mul}

    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)
    operation = random.choice(list(operators.keys()))
    answer = (operators.get(operation)(num_1, num_2))
    print(f"What is {num_1} {operation} {num_2}? Leave your answer to 1d.p.")
    return answer

def multiplication_3():
    operators = {'*': operator.mul}

    num_1 = random.randint(1, 1000)
    num_2 = random.randint(1, 1000)
    operation = random.choice(list(operators.keys()))
    answer = (operators.get(operation)(num_1, num_2))
    print(f"What is {num_1} {operation} {num_2}? Leave your answer to 1d.p.")
    return answer

def division_1():
    operators = {'/': operator.truediv}

    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    operation = random.choice(list(operators.keys()))
    answer = round(operators.get(operation)(num_1, num_2), 1)
    print(f"What is {num_1} {operation} {num_2}? Leave your answer to 1d.p.")
    return answer

def division_2():
    operators = {'/': operator.truediv}

    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)
    operation = random.choice(list(operators.keys()))
    answer = round(operators.get(operation)(num_1, num_2), 1)
    print(f"What is {num_1} {operation} {num_2}? Leave your answer to 1d.p.")
    return answer

def division_3():
    operators = {'/': operator.truediv}

    num_1 = random.randint(1, 1000)
    num_2 = random.randint(1, 1000)
    operation = random.choice(list(operators.keys()))
    answer = round(operators.get(operation)(num_1, num_2), 1)
    print(f"What is {num_1} {operation} {num_2}? Leave your answer to 1d.p.")
    return answer

def mixed_1():
    operators = {'+': operator.add,
                 '-': operator.sub,
                 '*': operator.mul,
                 '/': operator.truediv,
                 }

    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)
    operation = random.choice(list(operators.keys()))
    answer = operators.get(operation)(num_1, num_2)
    print(f"What is {num_1} {operation} {num_2}?")
    return answer

def mixed_2():
    operators = {'+': operator.add,
                 '-': operator.sub,
                 '*': operator.mul,
                 '/': operator.truediv,
                 }

    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)
    num_3 = random.randint(1, 100)
    operation1 = random.choice(list(operators.keys()))
    operation2 = random.choice(list(operators.keys()))
    answer1 = operators.get(operation1)(num_1, num_2)
    answer = operators.get(operation2)(answer1, num_3)
    print(f"What is {num_1} {operation1} {num_2} {operation2} {num_3}?")
    return answer

def mixed_3():
    operators = {'+': operator.add,
                 '-': operator.sub,
                 '*': operator.mul,
                 '/': operator.truediv,
                 }

    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)
    num_3 = random.randint(1, 100)
    num_4 = random.randint(1, 100)
    operation1 = random.choice(list(operators.keys()))
    operation2 = random.choice(list(operators.keys()))
    operation3 = random.choice(list(operators.keys()))
    answer1 = operators.get(operation1)(num_1, num_2)
    answer2 = operators.get(operation2)(answer1, num_3)
    answer = operators.get(operation3)(answer2, num_4)
    print(
        f"What is {num_1} {operation1} {num_2} {operation2} {num_3} {operation3} {num_4}?")
    return answer

def ask_question(difficulty, operator_type):
    # addition
    # if user inputs "A" and 1 
    if operator_type == "A" and difficulty == 1:
        # initialise function addition_1()
        answer = addition_1()
        # user's input will be assigned to guess variable 
        guess = float(input())
        # if user's input matches correct answer
        # return a boolean True
        return guess == answer
    elif operator_type == "A" and difficulty == 2:
        answer = addition_2()
        guess = float(input())
        return guess == answer
    elif operator_type == "A" and difficulty == 3:
        answer = addition_3()
        guess = float(input())
        return guess == answer
    # subtraction
    elif operator_type == "B" and difficulty == 1:
        answer = subtraction_1()
        guess = float(input())
        return guess == answer
    elif operator_type == "B" and difficulty == 2:
        answer = subtraction_2()
        guess = float(input())
        return guess == answer
    elif operator_type == "B" and difficulty == 3:
        answer = subtraction_3()
        guess = float(input())
        return guess == answer
    # multiplication
    if operator_type == "C" and difficulty == 1:
        answer = multiplication_1()
        guess = float(input())
        return guess == answer
    elif operator_type == "C" and difficulty == 2:
        answer = multiplication_2()
        guess = float(input())
        return guess == answer
    elif operator_type == "C" and difficulty == 3:
        answer = multiplication_3()
        guess = float(input())
        return guess == answer
    # division
    elif operator_type == "D" and difficulty == 1:
        answer = division_1()
        guess = float(input())
        return guess == answer
    elif operator_type == "D" and difficulty == 2:
        answer = division_2()
        guess = float(input())
        return guess == answer
    elif operator_type == "D" and difficulty == 3:
        answer = division_3()
        guess = float(input())
        return guess == answer
    # mixed
    elif operator_type == "E" and difficulty == 1:
        answer = mixed_1()
        guess = float(input())
        return guess == answer
    elif operator_type == "E" and difficulty == 2:
        answer = mixed_2()
        guess = float(input())
        return guess == answer
    elif operator_type == "E" and difficulty == 3:
        answer = mixed_3()
        guess = float(input())
        return guess == answer
    else:
        return "Invalid input!"

# objected oriented programming
class Player:
    def __init__(self):
        # initialization of the player which has two attributes, name and score
        self.name = input("Please key your name: ")
        self.score = 0
    def get_difficulty(self):
        # get's the player to select difficulty
        difficulty = int(input("{}! Please input your difficulty level (1, 2, 3):".format(self.name)))
        if difficulty == 1 or difficulty == 2 or difficulty == 3:
            # if difficulty is valid, return the difficulty
            return difficulty
        else:
            print("Invalid. Please try again.")
            # if invalid input, get user to input difficulty again.
            return self.get_difficulty()
    def get_operator(self):
        # same as difficulty just with operator
        operator = input("{}! Do you want addition(A), subtraction(B), multiplication(C) or division(D) or mixed(E) questions?".format(self.name))
        if operator ==  "A" or operator ==  "B" or operator ==  "C" or operator ==  "D" or operator ==  "E":
            return operator
        else:
            print("Invalid. Please try again.")
            return self.get_operator()
    def add_score(self):
        # function to add score
        self.score += 1
        return self.score

    def get_score(self):
        # gets the score of player and returns it in the form of a string
        printed_statement = "{}, your score is {}".format(self.name , self.score)
        return printed_statement


def game():
    global ti
    print("Welcome to The Game!\n")
    # creates two objects, player 1 and player 2
    player1 = Player()
    player2 = Player()
    while True:
        # initialize 
        # gets the type of operator player 1 wants
        operator_type = player1.get_operator()
        # gets the difficulty player 1 wants
        difficulty = player1.get_difficulty()
        
        # game start
        # start timer
        countdown_thread = threading.Thread(target=countdown)
        countdown_thread.start()
        while ti > 0:
            for i in range(10):
                # function "ask_question" take in an input and checks if input answer is correct
                if ask_question(difficulty, operator_type) == True:
                    # if ti is >0 when the answer is being input, 1 point is added to the player's score
                    if ti > 0:
                        player1.add_score()
                        print("You are correct!")
                    # if ti is 0, break the loop
                    elif ti == 0:
                        break
                else:
                    if ti ==0:
                        # if wrong answer is given after the game has ended, break the loop
                        break
                    print("Incorrect!!")
                    
            if ti == 0:
                break
        
        ti = 0
        
        # gets the operator type for player2
        operator_type = player2.get_operator()
        # gets the difficulty of player2
        difficulty = player2.get_difficulty()
        countdown_thread = threading.Thread(target=countdown)
        countdown_thread.start()
        while ti > 0:
        # initialize for player 2
            for i in range(10):
                if ask_question(difficulty, operator_type) == True:
                    if ti>0:
                        # if ti is >0 when the answer is being input, 1 point is added to the player's score
                        player2.add_score()
                        print("You are correct!")
                    elif ti == 0:
                        # if ti is 0, break the loop
                        break
                else:
                    # if wrong answer is given after the game has ended, break the loop
                    if ti == 0:
                        break
                    #incorrect is printed if answer is wrong and ti is not 0
                    print("Incorrect!!")
                    
            if ti == 0:
                break
        
        ti = 0
        
        # print out score and check if user want to reset
        print(player1.get_score())
        print(player2.get_score())
        # break to reset score to 0 for new game
        break
    # ask user if want to continue game
    cont = input("Do you want to play again? Yes/No")
    if cont == "No":
            print("Thank You for Playing!")
    # if user wants to continue game
    elif cont == "Yes":
        # restart game
        game()

game()
