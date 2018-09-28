# this code reads from a list of subjects
# find the corresponding file
# and move the file to a designated location
import os.path
import shutil
import os


# read the file with a list of subjects
# input: N/A
# output: a list of all subjects
def read_desired_subjects():
    all_subjects = "subjects.txt"

    sub = []
    with open(all_subjects, 'r') as f1:
        for line in f1:
          a = line.rstrip()
          if line not in sub:
            sub.append(a)
    return sub

# # from a list of subjects, get all the path of the file
# # in such format: /I/AMU Cleaned Data Sets/2046S/Sleep/2046SSlp.01.csv
# def getfilepath(L):
#     for sub in L:
#         path = "/I/AMU Cleaned Data Sets/" + sub + "/Sleep/" + sub + "Slp.01.csv"
#         path2 = "/I/AMU Cleaned Data Sets/" + sub + "/Sleep/" + sub.lower() + ".slp.01.csv"
#         # then check if this path exists
#         if os.path.isfile(path):
#             pass
#         elif os.path.isfile(path2):
#             print path2
#         else:
#             print sub
#             print path2
#         # if not exist
#         # grep keyword "Slp.01"
#         # then check existance
#         # then move to new folder:
        
# from a list of subjects, get all the path of the file
# in such format: /I/AMU Cleaned Data Sets/2046S/Sleep/2046SSlp.01.csv
def getandcopy(L):
    
    for sub in L:
        path = "/I/AMU Cleaned Data Sets/" + sub + "/Sleep/" 
        hasit = 0
        if os.path.exists(path):
            for fname in os.listdir(path):

                if fname.endswith('.01.csv'):
                    hasit = 1
                    print path+fname
                    copyfile(path+fname)
            if hasit == 0:
                print sub
        else:
            print "no such dir: " + sub

def copyfile(path):
    filename = os.path.basename(os.path.splitext(path)[0])
    print filename
    dst_path = "/home/pwm4/Desktop/cg342/sleepprogram_redo/20180925_allsubjects/" 
    shutil.copy2(path, dst_path)


l = read_desired_subjects()
getandcopy(l)