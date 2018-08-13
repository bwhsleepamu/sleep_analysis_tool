# this compares two csv files line by line
# and returns the rows that has difference


folderpath = "/home/pwm4/Desktop/cg342/sleepprogram_redo/Ready_to_send/"
f1 = folderpath+"20180803_output_2.csv"
f2 = folderpath+"20180813_output_2.csv"

with open(f1, 'r') as t1, open(f2, 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()


with open(folderpath+'diff2.csv', 'w') as out1:
    for line in filetwo:
        if line not in fileone:
            out1.write(line)

with open(folderpath+'diff1.csv', 'w') as out2:
    for line in fileone:
        if line not in filetwo:
            out2.write(line)
