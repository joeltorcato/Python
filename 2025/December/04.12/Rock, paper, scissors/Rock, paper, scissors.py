a = "paper"
b = "scissors"
c = "rock"

player1 = ""
player2 = ""

while player1 not in (a, b, c):
    player1 = input("player 1 (enter rock, paper, or scissors): ").lower()
while player2 not in (a, b, c):
    player2 = input("player 2, (enter rock, paper, or scissors): ").lower()

if player1 == player2:
    print("it's a tie!")
elif (player1 == a and player2 == c) or (player1 == b and player2 == a) or (player1 == c and player2 == b):
    print("player 1 wins!")
else:
    print("player 2 wins!")

