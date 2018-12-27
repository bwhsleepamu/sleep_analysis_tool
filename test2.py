# getting # of minutes of each sleep states between 8 and 9
# input: a list of sleep states
# [S1, S2, S3, ..., Other]        
def getCount(L):
    ct1, ct2, ct3, ct4, ctWake, ctRem, ctOther=(0,)*7
    interested = [1,2,3,4,5,6,7,0]
    for i in L:
      # if i in interested:
        if i==1:
          ct1+=1
        elif i==2:
          ct2+=1
        elif i==3:
          ct3+=1
        elif i==4:
          ct4+=1
        elif i==5:
          ctWake+=1
        elif i==6:
          ctRem+=1
        elif i not in [1,2,3,4,5,6,10,8,9]: # anything that is not 1-6 should be counted as Other
          if i not in [0,7]:
                print i + " --> other (edge case)"
          ctOther+=1
    l = [ct1, ct2, ct3, ct4, ctWake, ctRem, ctOther]
    return [x/2.0 for x in l]

    