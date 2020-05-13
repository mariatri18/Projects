def disekto(year):
    year = int(year)
    if ((year % 4 == 0) and (year %100 !=0)) or year % 400 == 0:
        return True
    return False

etos = input("Για πιο έτος θέλετε να μάθετε αν είναι δίσκετο; ")
if disekto(etos):
    print(f"Το έτος {etos} ειναι δίσεκτο")
else:
    print(f"Το έτος {etos} δεν είναι δίσεκτο")

print(disekto(etos))
print(disekto(etos))
