#Importing random
import random

#creating a list of elements of game and define variable.
elements = ["Stone","Scissor","Paper"]
global human #global for using the variabe in function
global com 
human = 0
com = 0

#added variable to store the difficulty level
difficulty = 1  # default level

#for displaying choices.
def display_choices():
    print("Now you're going to play Stone Paper Scissor game.")
    print("You need 10 points to win the match.")
    print("Here are your Choices :- ")
    print("Stone   : 1")
    print("Scissor : 2")
    print("Paper   : 3")
    print()
    #showing extra options for difficulty
    print("Choose Difficulty Level :- ")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

#function to decide computer's choice based on selected difficulty
def get_computer_choice(diff, last_human_choice):
    #easy = totally random, medium = sometimes smart, hard = always tries to counter
    if diff == 1:
        return random.randint(1, 3)
    elif diff == 2:
        #in medium mode, computer sometimes tries to counter your previous move
        if last_human_choice and random.random() < 0.5:
            return counter_move(last_human_choice)
        else:
            return random.randint(1, 3)
    else:
        #in hard mode, computer always tries to beat your previous move
        if last_human_choice:
            return counter_move(last_human_choice)
        else:
            return random.randint(1, 3)

#function for finding the move that can beat user's last move
def counter_move(choice):
    if choice == 1:
        return 3
    elif choice == 2:
        return 1
    elif choice == 3:
        return 2

#main gameplay.     
def play_game(human,com):
    global difficulty
    global last_human_choice
    
    #humanc =  int(input("Enter the choice here 1-3 : "))
    num = int(input("Enter the choice here 1-3 : "))
    humanc = validate(num)
    
    #getting computer choice according to difficulty selected
    comc = get_computer_choice(difficulty, last_human_choice)
    last_human_choice = humanc

    display_result(humanc, comc)
    
    winner(humanc, comc)
   
    points()

#for decide who is winner.
def winner(c1,c2):
    global com
    global human 
    if c1 == c2:
        print("Draw")
        return None
    elif c1 < c2 :
        if c1 == 2 and c2==3:
            human += 1
            print("Congratulations!...You Win.")
            return None
        elif c2 != 3:
            human += 1
            print("Congratulations!...You Win.")
            #print(f"P1 : {human}")
            return None
        else:
            com+=1
            print("Oops!...Best of luck next time.")
            # print(f"P2 : {com}")
            return None
    elif c2 < c1 :
        if c2 == 2 and c1==3:
            com += 1
            print("Oops!...Best of luck next time.")
            return None
        elif c1 != 3:
            print("Oops!...Best of luck next time.")
            com += 1
            #print(f"P1 : {human}")
            return None
        else:
            human+=1
            print("Congratulations!...You Win.")
            # print(f"P2 : {com}")
            return None

#for desplaying result.    
def display_result(c1,c2):
    
    print(f"You choose : {elements[c1-1]}") 
    print(f"Computer choose : {elements[c2-1]}") 

#validating the entered choice.    
def validate(num):
    if num < 0 or num > 3:
        num = int(input(("Enter the valid choice : ")))
        num = validate(num)

    return num

#Calculating points.
def points():
    print(f"Your Points     :{human}")
    print(f"Computer Points :{com}")

#final result 
def final(p1,p2):
    if (p1 == 10 ):
        print(f"You win by {p1-p2}")
    elif (p2 == 10):
        print(f"You lose by {p2-p1}")
    return None
# def get_choice():    
# human_choice : int(input("Enter the choice here 1-3 : "))
#     return human_choice
 
# def get_random():
#     com_choice = random.randint(1,3)
#     return com_choice

display_choices()

#asking player to choose game difficulty
difficulty = int(input("Enter difficulty (1-3): "))
if difficulty not in [1,2,3]:
    print("Invalid choice. Default (Medium) selected.")
    difficulty = 2
else:
    if difficulty == 1:
        print("Difficulty set to Easy mode.")
    elif difficulty == 2:
        print("Difficulty set to Medium mode.")
    else:
        print("Difficulty set to Hard mode.")

i =30
last_human_choice = None
#loop for playing the match 
while(i < 40):
    if human == 10 or com == 10:
        i = 40
        print()
        final(human,com)        
    else:   
        print()
        play_game(human,com)
