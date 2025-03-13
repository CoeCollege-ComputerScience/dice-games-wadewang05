import random

def rollDice():
    dice = []
    for i in range(10):
        dice.append(random.randint(1, 6))
    return dice

def playGame():
    players = ["Player 1", "Player 2", "Player 3"]
    
    while len(players) > 1:
        i = 0
        while i < len(players) and len(players) > 1:
            player = players[i]
            print(f"{player}'s turn:")

            target = random.randint(1, 6)
            print(f"{player} predicts: {target}")

            dice = rollDice()
            print(f"Rolled dice: {dice}")
            
            if dice.count(target) < 2:
                print(f"{player} is out!")
                players.pop(i)
            else:
                i += 1
            
            print("-")
    
    print(f"{players[0]} wins!")
playGame()