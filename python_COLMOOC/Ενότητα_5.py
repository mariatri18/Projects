import statistics

with open('python_COLMOOC/inputdata.txt', 'r', encoding='utf-8') as fin:
    content = fin.read().splitlines()

numlist=[]
for i in content:
    numbers = i.split(',')
    for n in numbers:
        numlist.append(float(n))


print(numlist)
m = statistics.mean(numlist)

ta = statistics.stdev(numlist)

with open('python_COLMOOC/outputdata.txt', 'w', encoding='utf-8') as f:
    f.write('Μέσος όρος = ')
    f.write(str(m) + '\n')
    f.write('Τυπική απόκλιση = ')
    f.write(str(ta))