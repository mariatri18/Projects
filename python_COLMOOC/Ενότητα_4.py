import statistics

list = []

def square(l,m,s):
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

for i in range (0, s):
    sq = m - my_list[i]
    ans1 = sq**2
    print('Tο τετράγωνα της διαφοράς κάθε τιμής από τον μέσο όρο είναι', ans1)


print('Μέγεθος της λίστας', s)