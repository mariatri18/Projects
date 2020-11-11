import random

moves = ['Π','Ψ','Χ']
player_wins = ['ΠΨ','ΧΠ','ΨΧ']
computer_score = 0
player_score = 0
while True:
    player_move = input("Δώσε την κίνησή σου: ")
    if player_move == "ΤΕΛΟΣ":
        break
    computer_move = random.choice(moves)

    print("Εσύ διάλεξες:",player_move)
    print("Ο Υπολογιστής διάλεξε:",computer_move)

    if player_move == computer_move:
        print("Ισοπαλία")
    elif player_move + computer_move in player_wins:
        print("Νίκησες!")
        player_score = player_score + 1
    
    else:
        print("Έχασες!")
        computer_score = computer_score + 1    
    print(player_score)    
    print(computer_score)    

    if player_score == 10:
        print("Κέρδισες")
        break
    elif computer_score == 10:
        print("Έχασες")
        break