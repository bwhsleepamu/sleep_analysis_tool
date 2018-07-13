import os
import glob

paths = "/home/pwm4/Desktop/cg342/sleepprogram_redo/20180627/data_all/"

files = glob.glob(paths+"*.csv")

for f in files:
 f_full = os.path.basename(f)
 index = f_full.find("Slp")
 filename = f_full[0:index]
 print filename


