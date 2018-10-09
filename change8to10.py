# to find the problem with files 
# check if they have the right lights out/on sequences

import csv
from collections import defaultdict
from collections import OrderedDict
import glob
import codecs
import os
import os.path

try:
    # Python 3
    from itertools import zip_longest
except ImportError:
    # Python 2
    from itertools import izip_longest as zip_longest


        
class aLine(object):
    content=[]
    pointer=-1

    def __init__(self, content, pointer):
        self.content = content
        self.pointer = pointer

    # def resetData(self, value, pointer):
    #     self.value = value
    #     self.pointer = pointer    
inputpath = "/home/pwm4/Desktop/cg342/sleepprogram_redo/20180925_allsubjects_tobeready/"
csv_files = glob.glob(inputpath+"*.csv")

aaa = ["2015HS3T","1712MX","1745MX"]

# check if a string contains a list of substrings
def checkgo(aaa,astring):
    for aa in aaa:
        if aa in astring:
            return 0 # when contains, do not proceed
    return 1

# write line to file       
def writeline(line, filename):

    dirpath = '/home/pwm4/Desktop/cg342/sleepprogram_redo/20180925_allsubjects_ready/'
    filepath = dirpath + filename
    with open(filepath, 'a') as out:
        out.write(line+"\n")
        
for filename in csv_files:

    if checkgo(aaa,filename) == 1:
        with open(filename, 'r') as f:
            d = dict() # {1: 1; 2: 6; 3: 1; ....}
            listoflinelist = []
            linecount = -1

            for line in f:
                linecount += 1
                singleline = line.rstrip()
                listofline = singleline.split(',')
                listoflinelist.append(aLine(listofline, linecount))
                
                if "8" in listofline[-1]:
                    spn = abs(int(listofline[1]))
                    if d.has_key(spn):
                        d[spn][0] += 1 # count of 8
                        d[spn][1].append(linecount)
                    else:
                        d[spn] = [1,[linecount]] # last list records all the line numbers


            for key, value in d.iteritems():
                if value[0]>2:
                    # for lc in d[spn][1]:
                    # print os.path.basename(filename), key, value
                    for i in value[1][:-1]:
                        # listoflinelist[i].content[3]=10
                        listoflinelist[i].content[3] = " 10"
            # print ','.join(listoflinelist[1].content)

        
            # if '21C3' in filename:
            #     print listoflinelist[1364].content
            #     print listoflinelist[1581].content
            #     print listoflinelist[2470].content        
            #         # litsoflinelist[value[1]][3]=10 # except the last one!

                    
            for currline in listoflinelist:
                newline = ','.join(currline.content)
                writeline(newline, os.path.basename(filename))
            
            
