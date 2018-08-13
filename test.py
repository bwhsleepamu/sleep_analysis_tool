def getPS (L):
    ps=[]
    epo=20
    desired=[1,2,3,4,6]
    count = 0
    # i is index, j is value
    for i,j in enumerate(L):
      if j in desired:
        count += 1 
        # count < 20 and not the last element and next element is not continuous
        if count < epo and i!=len(L)-1 and (L[i+1] not in desired):
          count = 0                         
        elif count >= epo:
          ps.append(L[i-epo+1])
          ps.append(i-epo+1)    
          return ps


# L = [8,5,5,5,5,5,5,5,5,5,5,5,5,5,5,2,1,1,1,1,1,4,1,2,1,1,1,1,1,1,1,1,3,3,3,3,3,1,1]
# a = getPS(L)
# print a

# testing gitignore file


class Data(object):
    value=0
    pointer=-1

    def __init__(self, value, pointer):
        self.value = value
        self.pointer = pointer   

def getLat(L, sleepstate):
    
    lat = next((L.index(i) for i in L if i==sleepstate), None)
    if lat is None:
      return "."
    else:
      if 0 in L[:lat]:
        return "."
      else:
        return lat/2.0

L = [2,5,2,2,0,3,3,3,4,1,3,3,3,3]

# getting the time of sleep (12346) uninterrupted by first wake(5) before 9
# input: a list of sleep states
# output: float (minutes)
def getFinalWake(L):
  sleep = [1,2,3,4,6]
  count = 0
  for i,j in enumerate(reversed(L)):
      if j in sleep:
        count += 1
      elif j==5:
        return count

def lastFunction(L):
  sleep = [1,2,3,4,6]
  has9 = False
  has5 = False
  if L[-1]!=9:
    for sleepstage in reversed(L):
          
      if has5:
        if sleepstage in sleep:
          return sleepstage
      if sleepstage==5:
        has5 = True
      
  else:  
    for sleepstage in reversed(L):
          
      if has9 and has5:
        if sleepstage in sleep:
          return sleepstage
      if sleepstage==9:
        has9 = True
      elif sleepstage==5:
        has5 = True

# print getFinalWake(L)

print lastFunction(L)