# Sleep Analysis Tool

To analyze sleep stage data and beyond
0. sleep_analysis.py
1. preprocessing.py
2. read.py
3. check_dup.py
4. fill.py

__Running on Windows__

open command line:  Start menu -> Run  and type cmd
```
$ C:\python27\python.exe 
$ Z:\code\hw01\script.py
Or if your system is configured correctly, you can drag and drop your script from Explorer onto the Command Line window and press enter.
```



__Three issues (Resolved):__

- [x] If there is a 0 (unscorable) between lights out or start time of sleep episode and a stage of sleep, then you cannot compute sleep latency

- [x] If the 8 (lights out marker) is before the scheduled sleep onset (e.g., change in WP/SP from negative to positive #), then use the SCHEDULED time not the 8  time. If the 8 is after the scheduled time, then use the 8 time to calculate all metrics.

- [x] If the 9 (lights on marker) is after the scheduled sleep offset (e.g., change in WP/SP from positive to negative #) then use the SCHEDUOED time not the 9 time. If the 9 is before the scheduled time, then use the 9 time to calculate all metrics.