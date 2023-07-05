file = open('numbers.txt', 'r')
Lines = file.readlines()
count = 0 
evens = 0 
sums = 0 
for line in Lines:
    count += 1
    aa=line.split()
    sums += int(aa[1])
    if((int(aa[1]))%2 == 0):
        evens += 1


print("count = ",count)
print("sum = ",sums)
print("evens = ",evens)
print("average = ",sums/count)
