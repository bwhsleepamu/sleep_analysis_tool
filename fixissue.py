# to find the problem with files 
# check if they have the right lights out/on sequences

import csv
from collections import defaultdict
from collections import OrderedDict
import glob
import codecs
import os
import time
import allfunctions as func
import shutil

try:
    # Python 3
    from itertools import zip_longest
except ImportError:
    # Python 2
    from itertools import izip_longest as zip_longest

# A Data object holds 2 properties:
# 1. value (str)
# 2. original position 

class Data(object):
    value=0
    pointer=-1

    def __init__(self, value, pointer):
        self.value = value
        self.pointer = pointer   
    
    def resetData(self, value, pointer):
        self.value = value
        self.pointer = pointer 

# multiple files:
inputpath = "/home/pwm4/Desktop/cg342/sleepprogram_redo/testing/"
csv_files = glob.glob(inputpath+"*.csv")

# dictionary for the final output
adict = OrderedDict()

output_header = ["Subject","SPn","latS1","latS2","latREM","latSWS","latPersistSLeep","S1",
"S2","S3","S4","Wake","REM","Other","WAPSO","FinalWake","NWake_1","NWake_2","NWake_5","Lout2Lon"]

# initialize the output dictionary keys
for column_name in output_header:
    adict[column_name] = []

for filename in csv_files:
    # read from files
    print filename
    with open(filename, 'r') as f:
        columns = defaultdict(list)
        # read rows into a dictionary format
        reader = csv.DictReader(f,  fieldnames=['subject', 'WPSP', 'labtime', 'sleepstate']) 
        try:
            for row in reader: # read a row as {column1: value1, column2: value2,...}
                for (k,v) in row.items(): # go over each column name and value 
                    columns[k].append(v)
        except:
            print("error: " + filename)

    WPSP = columns['WPSP']
    sleepstate = columns['sleepstate']
    slp_list = []
    slp_unit=[]

    # convert list of string to list of integers
    WPSP = list(map(int, WPSP))
    sleepstate = list(map(int, sleepstate))

    ind8 = [i for i, x in enumerate(sleepstate) if x == 8]
    ind9 = [i for i, x in enumerate(sleepstate) if x == 9]

    for a,b in zip(ind8,ind9):
        for i in range(a,b+1):
            slp_unit.append(Data(sleepstate[i], i)) # appending sleep stages
        slp_list.append(slp_unit) # slp_list: [Data1,Data2, Data3, ...]
        slp_unit=[]
    
    for unit in slp_list:
            
        spn = int(columns['WPSP'][unit[0].pointer])
        if spn < 0:
            # replace lights out time with scheduled sleep offset
            # find next positive Spn
            # print unit[0].pointer
            indof8 = unit[0].pointer
            # print indof8
            # print columns['WPSP'][unit[0].pointer]
            while True:
                indof8 += 1
                if columns['WPSP'][indof8] > 0:
                    unit[0].resetData(int(columns['sleepstate'][indof8]),indof8)
                    break
                # print unit[0].pointer
                # print unit[0].value
        # checking spn of 9
        spn9 = int(columns['WPSP'][unit[-1].pointer])
        if spn9 < 0:
            # replace lights out time with scheduled sleep offset
            # find next positive Spn
            # print unit[0].pointer
            indof9 = unit[-1].pointer
            # print indof8
            # print columns['WPSP'][unit[0].pointer]
            while True:
                indof9 -= 1
                if columns['WPSP'][indof9] > 0:
                    unit[-1].resetData(int(columns['sleepstate'][indof9]),indof9)
                    break
        newU = func.getDataValue(unit)
        # print newU[0]
        if 0 in newU:
            print "0"