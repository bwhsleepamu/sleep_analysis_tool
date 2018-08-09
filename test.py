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

L = [8,2,2,2,0,3,3,3]
print getLat(L,2)
print getLat(L,3)

if "." <= 3:
  print True