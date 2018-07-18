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
inputpath = "/home/pwm4/Desktop/cg342/sleepprogram_redo/20180627/data_all/"
csv_files = glob.glob(inputpath+"*.csv")

### testing file: 
#inputpath = "/home/pwm4/Desktop/cg342/sleepprogram/24B7GXT3Slp.01.csv"

# generate output folder
timestr = time.strftime("%Y%m%d-%H%M%S")
outputpath =  inputpath + "output_" + timestr + "/"
if not os.path.exists(outputpath):
    os.makedirs(outputpath)


class Data(object):
    value=0
    pointer=-1

    def __init__(self, value, pointer):
        self.value = value
        self.pointer = pointer   


# dictionary for the final output
adict = OrderedDict()

output_header = ["Subject","SPn","latS1","latS2","latREM","latSWS","latPersistSLeep","S1",
"S2","S3","S4","Wake","REM","Other","WAPSO","FinalWake","NWake_1","NWake_2","NWake_5",
"Lout2Lon","LastSlp","LastSlp_before_finalwake"]

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
    
    for a,b in zip(ind8,ind9):
        for i in range(a,b+1):
          slp_unit.append(Data(sleepstate[i], i))
        slp_list.append(slp_unit)
        slp_unit=[]


    # index of each first occured sleep state
    # then calculate latency (/2.0)
    for unit in slp_list:
        # making the Data.value into a new list
        newU = func.getDataValue(unit)

        adict["Subject"].append(columns['subject'][unit[1].pointer])
#        adict["SPn"].append(abs(int(columns['WPSP'][unit[0].pointer])))
#        if int(columns['WPSP'][unit[1].pointer]) <0:
#          print columns['subject'][unit[1].pointer], int(columns['WPSP'][unit[1].pointer])
        adict["SPn"].append(abs(int(columns['WPSP'][unit[2].pointer])))
        adict["latS1"].append(func.getLat(unit, 1))
        adict["latS2"].append(func.getLat(unit, 2))
        adict["latREM"].append(func.getLat(unit, 6))
        # checking if 3 appears before 4        
        if func.getLat(unit, 3)<=func.getLat(unit, 4):
          adict["latSWS"].append(func.getLat(unit, 3))
        else:
          adict["latSWS"].append(func.getLat(unit, 4)) 

        p = func.getPS(newU) # index of onset of PS
        if not p:
          index="."
          adict["latPersistSLeep"].append(index)
        else:
          index = p[1]
          adict["latPersistSLeep"].append(index/2.0)

        adict["S1"].append(func.getCount(newU)[0])
        adict["S2"].append(func.getCount(newU)[1])
        adict["S3"].append(func.getCount(newU)[2])
        adict["S4"].append(func.getCount(newU)[3])
        adict["Wake"].append(func.getCount(newU)[4])
        adict["REM"].append(func.getCount(newU)[5])
        adict["Other"].append(func.getCount(newU)[6])
        adict["WAPSO"].append(func.countWake(newU, index))

        adict["FinalWake"].append(func.getFinalWake(newU))
        # get NWake: second parameter is wake time of 1, 2, or 5 minuites
        adict["NWake_1"].append(func.getNWake(newU,1))
        adict["NWake_2"].append(func.getNWake(newU,2))
        adict["NWake_5"].append(func.getNWake(newU,5))
        adict["Lout2Lon"].append(func.getLout2Lon(newU))
        
        # adding 2 more columns:
        lastslp = func.SleepStageB49(newU)
        if lastslp == None:
          adict["LastSlp"].append(".")
        else:
          adict["LastSlp"].append(lastslp)
        
        lastslpfw = func.SleepStageB4FinalWake(newU)
        if lastslpfw == None:
          adict["LastSlp_before_finalwake"].append(".")           
        else:
          adict["LastSlp_before_finalwake"].append(lastslpfw)

## write to output
with open(outputpath + "output_unfilled.csv", "wb") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(adict.keys())
    export_data = zip_longest(*adict.values(), fillvalue = "")
    writer.writerows(export_data)




