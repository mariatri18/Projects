import random
secret = random.randrange(1, 101) 
print(secret)

guess = 0
dok = 0
while guess != secret:
    guess = int(input("Μαντεψε έναν αριθμό από το 1 ως 100: "))
    dok = dok + 1

    if guess > secret:
        print("Πολύ μεγάλος!")
    elif guess < secret:
        print("Πολύ μικρός!")
    else:
        print("To βρήκες!")

print("Oι προσπάθειες που έχει κάνει είναι: ", dok)