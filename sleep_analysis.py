import preprocessing as pre 
import read
import check_dup as dup
import allfunctions as func
import fill

# /home/pwm4/Desktop/cg342/sleepprogram_redo/20190419/test2
# /home/pwm4/Desktop/cg342/sleepprogram_redo/20190530
pathname = func.getInput()
# preprocessing data
try:
    pre.preprocess(pathname)
    print "\n"
    print "Data preprocessing is successful\n"
except:
    print "\nData preprocessing error!\n"
else:
    # run analysis
    print "Analyzing ..."
    
    try:
        outputpath = read.analyze(pathname)
        
    except:
        print "Analysis Error!"
    else:
        try:
            # check if there's duplicate line
            dup.check_dup(outputpath)
        except:
            print "Error: Duplicates found!"
        else:
            print "Success: No Duplicates"
            
            try:
                fill.fillgap(outputpath)
            except: #FunctionTimedOut:
                # print "Function exceed 3 seconds and was terminated"
                print "Fill.py error"
            else:   
                print "Output created successfully!"

            

    

