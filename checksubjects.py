# get a list of subjects

import glob
import os
import csv

# read the files with all subjects that are needed
# input: N/A
# output: a list of all subject_codes
def read_desired_subjects(filename):
#    all_subjects = "subjects.txt"

    sub = []
    with open(filename, 'r') as f1:
        for line in f1:
          a = line.rstrip()
          if line not in sub:
            sub.append(a)
    return sub


def read_desired_subjects_csv(filename):
#    all_subjects = "subjects.txt"

    sub = []
    with open(filename, 'r') as f1:
        for line in f1:
          linelist = line.rstrip().split(",")
          s = linelist[0]
          if s not in sub:
            sub.append(s)
    return sub

   

filetocheck = "SleepAnalysis_OUTPUT_20180627.csv"
subjectfile = "subjects.txt"
      
# list of subjects we want
allsub = read_desired_subjects(subjectfile)
sub = read_desired_subjects_csv(filetocheck)

print len(allsub)
print len(sub)

for s in allsub:
  if s not in sub:
    print s
