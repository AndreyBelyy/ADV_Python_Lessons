#!/bin/python3

import shutil       # For CopyFile
import os           # For GetFileSize and check if file exists
import sys          # For CLI Arguments

# lesson_script_cleaning_logs.py mylog.txt 10 5 #

if(len(sys.argv)) < 4:
    print("Missing arguments! Usage is script.py 10 5")
    exit(1)
file_name  = sys.argv[1]
limitsize  = int(sys.argv[2])
logsnumber = int(sys.argv[3])

if(os.path.isfile((file_name)) == True):            # Check if MAIN logfile file exist
    logfile_size = os.stat(file_name).st_size       # Get filesize in BYTES
    logfile_size = logfile_size / 1024              # Convert from BYTES to KILOBYTES

    if(logfile_size >= limitsize):
        if(logsnumber > 0):
            for currentFileNum in range(logsnumber, 1, -1):   # Current file name
                src = file_name + "_" + str(currentFileNum-1) # Previous file name
                dst = file_name + "_" + str(currentFileNum)   # Next file name
                if os.path.isfile(src) == True:               # If previous file exists
                    shutil.copyfile(src, dst)                 # Copy to next file (new file)
                    print("Copied: " + src + " to " + dst)
            shutil.copyfile(file_name, file_name + "_1")      # New file name
            print("Copied :" + file_name + "  to " + file_name + "_1")
        myfile = open(file_name, 'w')                         # Erase sorce file
        myfile.close()
