import preprocessing as pre 
import read
import check_dup as dup
import allfunctions as func
import fill
# inputpath = "/home/pwm4/Desktop/cg342/sleepprogram_redo/20190419_ready/"

# def getInput():

#     pathname = raw_input("Enter a path: ")

#     if not pathname.endswith("/"):
#         pathname += "/"
#     return pathname
# func.getInput()

pathname = func.getInput()
# preprocessing data
try:
    pre.preprocess(pathname)
    print "Data preprocessing is successful"
except:
    print "Data preprocessing unsuccessful"
else:
    # run analysis
    print "Analyzing ...."
    outputpath = read.analyze(pathname)
    try:
        # check if there's duplicate line
        dup.check_dup(outputpath)
    except:
        print "exception"
    else:
        print "Success: No Duplicates"
        fill.fillgap(outputpath)

    

