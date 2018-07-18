# this function is to fill all the data of the missing SPn

from collections import OrderedDict
import csv
import time
folderpath = "/home/pwm4/Desktop/cg342/sleepprogram_redo/20180627/data_all/output_20180713-144743/"
inputfile = folderpath + "output_unfilled_part2.csv"


# D is a dictionary to hold all the rows
# key: subject code values: list of lists
# e.g., D['3319GX'] = [[1,106,,,], [2,20.5,,,], [3,80.5,,,]]
D = OrderedDict()

# a list for all subject codes
sublist = []

with open(inputfile, 'r') as f:
  next(f)
  # read each line of file
  for line in f:
    # get a list out of each row
    linelist = line.rstrip().split(",")
    # first element is subject
    # process by subject code
    if linelist[0] not in sublist:
      sublist.append(linelist[0])
      # initialize the list to be the value of D[key]
      D[linelist[0]]=[]
    D[linelist[0]].append(linelist[1:])
  
for x in sublist:
#    start = int(D[x][0][0])     
    cur = 1
    # for looping D[x] all SPn's
    for idx, val in enumerate(D[x]):
      try:
        if cur != int(val[0]):
         toadd=[cur, ".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."]
         D[x].insert(idx,toadd)
      except:
        print val
      cur += 1
      

##print D['3319GX']

timestr = time.strftime("%Y%m%d-%H%M%S")
with open(folderpath + timestr + "_" + "output_filled_part2.csv", 'wb') as out:
     
    for x in sublist:
      for row in D[x]:
        
        writer = csv.writer(out)
        out.write(x + ",")
        writer.writerow(row)


