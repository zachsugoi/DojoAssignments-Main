#Find and Replace
str = "If monkeys like bananas, then I must be a monkey!"
print str.find("monkey"), str.rfind("monkey")
new_str = str.replace("monkey","alligator")
#Min and Max
x = [2,54,-2,7,12,98]
print min(x), max(x)
#First and last
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0], x[len(x)-1]
new_x = []
new_x += [x[0],x[len(x)-1]
#New List
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
negatives = [-3,-2]
x.remove(-3)
x.remove(-2)
x.insert(0,negatives)
