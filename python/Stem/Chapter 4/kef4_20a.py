import random

tux = random.randrange(1, 100)
pai = int(input("Πες μου έναν αριθμό: "))

if tux > pai:
    print("Πολύ μεγάλος!")
elif (tux < pai):
    print("Πολύ μικρός!")
else:
    print("Το βρήκες!")      

print(tux)      