# Sleep Analysis Tool

To analyze sleep stage data and beyond

1. findproblem.py
   - change folder path (1 line)
2. read.py
   - change folder path
3. check_dup.py
   - change folder path
   - uncomment next(f)
4. fill.py
   - change folder path
   - inputfile name and outputfile name
   - uncomment next(f)
   - (split inputfile in some occasions)
   - split output_unfilled.csv to 2-3 parts
   - keep updating inputfile name



__Three issues:__

- [ ] If there is a 0 (unscorable) between lights out or start time of sleep episode and a stage of sleep, then you cannot compute sleep latency

- [ ] If the 8 (lights out marker) is before the scheduled sleep onset (e.g., change in WP/SP from negative to positive #), then use the SCHEDULED time not the 8  time. If the 8 is after the scheduled time, then use the 8 time to calculate all metrics.

- [ ] If the 9 (lights on marker) is after the scheduled sleep offset (e.g., change in WP/SP from positive to negative #) then use the SCHEDUOED time not the 9 time. If the 9 is before the scheduled time, then use the 9 time to calculate all metrics.