import random

def rollDice():
    d1= random.randint(1, 6)
    d2= random.randint(1, 6)
    return max(d1, d2) * 10 + min(d1, d2)

def playGame():
    p1Score = 0
    p2Score = 0

    while max(p1Score, p2Score) < 100:
        p1Roll = rollDice()
        p2Roll = rollDice()
        print(f"Player 1: {p1Roll}, Player 2: {p2Roll}")
        
        if p1Roll > p2Roll:
            p1Score += p1Roll
        elif p2Roll > p1Roll:
            p2Score += p2Roll
        else:
            print("It's a tie! No points awarded.")

        print(f"Scores: Player 1 - {p1Score}, Player 2 - {p2Score}")
    
    winner = "Player 1" if p1Score > p2Score else "Player 2"
    print(f"{winner} wins!")

playGame()