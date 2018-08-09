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


