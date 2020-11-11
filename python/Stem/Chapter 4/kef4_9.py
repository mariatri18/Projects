ak1 = int(input("Δώσε ένα ακέραιο: "))
ak2 = int(input("Δώσε έναν ακόμα ακέραιο: "))
sym = str(input("Δώσε την πράξη που θες ανάμεσα στα +, -, * και /: "))

if sym == "+":
    print(ak1 + ak2)
elif sym == "-":
    print(ak1 - ak2)
elif sym == "*":
    print(ak1 * ak2)
elif (sym == "/" and ak2 !=0):
    print(ak1 / ak2)        
elif (sym == "/" and ak2 == 0):
    print("Αδύνατη η διαίρεση")
else:
    print("Λάθος πράξη")    