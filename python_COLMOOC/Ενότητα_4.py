import statistics

list = []


def square(sm):
    
    yield
    
   
    
# n = int(input("Enter number of elements : ")) 
# for i in range(0, n): 
#     ele = int(input())
#     list.append(ele)
# print(list)     


print('Δώσε όσους αριθμούς θες! Για να σταματήσεις δώσε κάποιον χαρακτήρα')

try: 
    my_list = [] 
      
    while True: 
        my_list.append(int(input())) 
          
# if input is not-integer, just print the list 
except: 
    print(my_list)

sm = sum(my_list)
print('Tο άθρoισμα των αριθμών είναι', sm)

m = statistics.mean(my_list)
print('O μέσος όρος είναι', m)

s = len(my_list)

for i in range (0, s):
    sq = m - my_list[i]
    ans = sq**2
    print('Tο τετράγωνα της διαφοράς κάθε τιμής από τον μέσο όρο', ans)

print('Μέγεθος της λίστας', s)