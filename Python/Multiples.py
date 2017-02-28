#Multiples: Part I
for odds in range(1,1001):
    if(odds % 2 != 0):
        print odds
#Multiples: Part II
for fives in range(5,1000001):
    if(fives % 5 == 0):
        print fives
#Sum List
a = [1,2,5,10,255,3]
sum = 0
for values in a:
    sum += values
print sum
#Average List
a = [1,2,5,10,255,3]
sum = 0
for i in a:
    sum += i
print sum/len(a)
