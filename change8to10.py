# to find the problem with files 
# check if they have the right lights out/on sequences

import csv
from collections import defaultdict
from collections import OrderedDict
import glob
import codecs
import os

try:
    # Python 3
    from itertools import zip_longest
except ImportError:
    # Python 2
    from itertools import izip_longest as zip_longest


# # write line to file       
# def writeline(line,fname):
#     filepath = '/home/pwm4/Desktop/cg342/sleepprogram_redo/20180925_allsubjects _ready/'+ fname
#     with open(filepath, 'a') as out:
#         out.write(line+"\n")
        

inputpath = "/home/pwm4/Desktop/cg342/sleepprogram_redo/20180925_allsubjects_tobeready/"
csv_files = glob.glob(inputpath+"*.csv")


for filename in csv_files:
    # read from files
    # print filename
    with open(filename, 'r') as f:
        d = dict()

        for line in f:
            singleline = line.rstrip()
            listofline = singleline.split(',')
            # print listofline
            # if "8" in listofline[-1]:
            if listofline[-1] == " 8" or listofline[-1]== "8":
                spn = abs(int(listofline[1]))
                if d.has_key(spn):
                    d[spn] += 1
                else:
                    d[spn] = 1
        for key, value in d.iteritems():
            if value>2:
                print filename, key