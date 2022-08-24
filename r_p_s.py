import random

print("================================")
print("Welcome to Rock, Paper, Scissors")
print("================================")

user_input = input("chooce bettwen Rock(r), Paper(p), Scisosre(s)")
computer_r = random.randint(1,3)


if (computer_r == 1):
    computer = "Rock"
elif (computer_r == 2):
    computer = "Paper"
else :
    computer = "Scissors"

if (user_input == "r"):
    user_ch = "Rock"
elif (user_input == "p"):
    user_ch = "Paper"
else :
    user_ch = "Scissors"
print ("Your choose "  + user_ch)

if (computer == user_ch):
    print ("i chose " + computer + " too!! soo it's a draw")

elif (computer == "Rock"):
    if (user_ch == "p"):
        print ("I chose " + computer + " I lose")
    else :
        print ("I chose " + computer + " I won")
elif (computer == "Paper"):
    if (user_ch == "r"):
        print ("I chose " + computer + " I won")
    else : 
        print ("I chose " + computer + " I lose")
else :
    if (user_ch == "r"):
        print ("I chose " + computer + " I lose")
    else:
        print ("I chose " + computer + " I won")
    
print("")        
print("**********************")
print("THANK YOU FOR PLAYING!")
print("**********************")









