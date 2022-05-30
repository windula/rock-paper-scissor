import random
item_list = ['R', 'P', 'S']
print("WELCOME TO ROCK-PAPER-SCISSOR")
# player1 = name of the human player
# player2 = computer player
player1 = input("Enter your name : ")
print("Welcome To The game {}".format(str(player1)))
print("Instructions :\n 1. To choose ROCK please enter R \n 2. To choose PAPER please select P \n 3. To choose SCISSOR please enter C")
# start the game
player1_total = 0
player2_total = 0
for i in range (0,10):
    # player1 turn
    print("\nROUND NUMBER : {}".format(i))
    item = input("Choose ROCK or PAPER or SCISSOR : ")
    choice1 = str(item)
    # player2 turn
    random_item = random.choice(item_list)
    print ("Input from the opponent : " + str(random_item))
    choice2 = str(random_item)
    if choice1 == choice2:
        print("DRAW")
    else:
        if (choice1 == 'R' and choice2 == 'S') or (choice1 == 'P' and choice2 == 'R') or (choice1 == 'S' and choice2 == 'P'):
            print("{} wins the round".format(player1))
            player1_total = player1_total + 1
        if (choice1 == 'R' and choice2 == 'P') or (choice1 == 'P' and choice2 == 'S') or (choice1 == 'S' and choice2 == 'R'):
            print("Your Opponent Wins the Round")
            player2_total = player2_total + 1
# Final results
if player1_total > player2_total:
    print("\nWinner of the Game : {}".format(player1))
elif player1_total < player2_total:
    print("\nWinner of the Game : Computer")
else:
    print("\nThe Game is Draw")