#Odd/Even
def odd_even():
    for i in range(1,2001):
        if(i % 2 != 0):
            print "Number is "+str(i)+". This is an odd number."
        else:
            print "Number is "+str(i)+". This is an even number."
odd_even()
#Multiply
def multiply(a,b):
    c = []
    for i in a:
        c += [i*b]
    return c
a = [2,4,10,16]
print multiply(a,5)
#Hacker Challenge
def layered_multiples(arr):
    new_array = []
    for i in arr:
        inner_list = []
        for t in range(1,i+1):
            inner_list += [1]
        new_array.append(inner_list)
    return new_array
x = layered_multiples(multiply([2,4,5],3))
print x
