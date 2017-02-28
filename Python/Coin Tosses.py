import random
def toss():
    head_cnt = 0
    tails_cnt = 0
    for count in range(1,5001):
        heads_tails = round(random.random())
        if(heads_tails == 1):
            head_cnt += 1
            print "Throwing a coin... It's a head! ... Got "+str(head_cnt)+" head(s) so far and "+str(tails_cnt)+" tail(s) so far"
        else:
            tails_cnt += 1
            print "Throwing a coin... It's a tail! ... Got "+str(head_cnt)+" head(s) so far and "+str(tails_cnt)+" tail(s) so far"
toss()
