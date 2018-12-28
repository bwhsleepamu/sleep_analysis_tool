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

# getting the time of sleep (12346) uninterrupted by first wake(5) before 9
# -> getting the time of wake(5) uninterrupted by sleep (12346) before 9
# input: a list of sleep states
# output: float (minutes)
def getFinalWake(L):
  sleep = [1,2,3,4,6]
  count = 0
  for i,j in enumerate(reversed(L)):
      if j == 5:
        count += 1
      elif j in sleep:
        return count/2.0
        
L=[1,2,2,5,5,5,1,1,9]
print getFinalWake(L)