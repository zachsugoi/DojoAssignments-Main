def draw_stars(arr):
    for i in arr:
        if(i*0 == 0):
            print "*"*i
        else:
            print i[0].lower()*len(i)
draw_stars([3,7,"Cat","Hello"])
