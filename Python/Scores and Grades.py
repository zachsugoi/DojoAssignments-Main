import random
def score_grade():
    for count in range(1,11):
        score = int(round(random.random()*40))+60
        if(score > 90):
            print "Score: "+str(score)+"; Your grade is A"
        elif(score > 80):
            print "Score: "+str(score)+"; Your grade is B"
        elif(score > 70):
            print "Score: "+str(score)+"; Your grade is C"
        else:
            print "Score: "+str(score)+"; Your grade is D"
score_grade()
