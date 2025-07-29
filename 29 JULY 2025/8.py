def reptation(example):
    ans = ""
    for i in range(len(example)):
        
        if(i == 0):
            ans+=example[i] 
        else:
            if(example[i]!=example[i-1]):
                ans+=example[i]
    
    return ans
s = "hhhheyyy this is aaaa verrrryyy shorrt wwwaaayyy"
print(reptation(s))


    