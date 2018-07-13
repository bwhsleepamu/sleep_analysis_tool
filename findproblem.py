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

# multiple files:
inputpath = "/home/pwm4/Desktop/cg342/sleepprogram_redo/20180627/data_missed/"
csv_files = glob.glob(inputpath+"*.csv")



class Data(object):
    value=0
    pointer=-1

    def __init__(self, value, pointer):
        self.value = value
        self.pointer = pointer   


# dictionary for the final output
adict = OrderedDict()

output_header = ["Subject","SPn","latS1","latS2","latREM","latSWS","latPersistSLeep","S1",
"S2","S3","S4","Wake","REM","Other","WAPSO","FinalWake","NWake_1","NWake_2","NWake_5","Lout2Lon"]

# initialize the output dictionary keys
for column_name in output_header:
    adict[column_name] = []

for filename in csv_files:
    # read from files
#    print filename
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
    if len(ind8) != len(ind9):
        print filename + " with lights  out/on issue" 
        print ind8
        print ind9
##    else:
##        print filename
#    for a,b in zip(ind8,ind9):
#        if a>b:
#          print filename
#          break
       
#        for a,b in zip(ind8,ind9):
##            if a>b:
##              print a,b
##              print WPSP[a], WPSP[b]
##            else:
##              print  
#                     
#            if a > b or prevb > a:
#               print a, b
#               print WPSP[a], WPSP[b]
#            prevb = b
#                          
       
#    print filename
#    print ind8
#    print ind9

