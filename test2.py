import os
#  getting # of minutes of each sleep states between 8 and 9
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
        


# a function to remove elements by index
# input: a list of Data, front or end, index number
# output: a list of Data trimmed
def resetList(L,frontOrEnd,ind):
  if frontOrEnd == 0:
    return L[ind:]
  elif frontOrEnd == 1:
    return L[:ind+1]

# getting the # of wake episodes >= 1 minute (2 consec epoch) (int)
# intput: list of sleep states, duration of 1,2, or 5 minutues
# output: an integer
def getNWake(L, duration):
    wake = 0
    onset = 0 # onset of wake
    cont = 0  # continuous count of wake
    count = 0 # count of bouts
    # i is index, j is value
    for i,j in enumerate(L):
      if j == 5:
        onset = 1
        cont += 1
        if i!=len(L)-1 and L[i+1]!=5 or i==len(L)-1 and onset == 1:
          onset = 0
          if cont >= duration*2:
            count += 1
          cont = 0

    return count



# L = [
#   5,5,1,
#   5,5,1,
#   5,5,1,
#   5,5,5,1,
#   5,5,5,5,1,
#   5,5,5,5,5,1,
#   5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,1,1,1,1,1,1,1,1,5,1,6,1,5,1,2,1,1,5]
# print getNWake(L,1)
# print getNWake(L,2)
# print getNWake(L,5)
inputpath = "/home/pwm4/Desktop/cg342/sleepprogram_redo/20180925_allsubjects_ready/2408HSlp.01.csv"
fname = os.path.basename(inputpath)
subject = fname[:fname.find('Slp')]

