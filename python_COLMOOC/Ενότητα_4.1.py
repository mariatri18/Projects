import statistics

def squares(l,m,s):
    for i in range(s):
        sq = m - l[i]
        ans = sq**2
        yield ans

print('Δώσε όσους αριθμούς θες! Για να σταματήσεις δώσε κάποιον χαρακτήρα')
try: 
    my_list = []     
    while True: 
        my_list.append(int(input()))          
except: 
    print(my_list)
    
sm = sum(my_list)
print('Tο άθρoισμα των αριθμών είναι', sm)
m = statistics.mean(my_list)
print('O μέσος όρος είναι', m)
s = len(my_list)

for x in squares(my_list,m,s):
    print('Tο τετράγωνα της διαφοράς κάθε τιμής από τον μέσο όρο είναι', x)
print('Μέγεθος της λίστας', s)