#
import os
import time

DAYS = 1            # maximal age of file, older will be deleted
FOLDERS = [
            "/Users/aegar/Downloads"
]

TOTAL_DELETED_SIZE = 0
TOTAL_DELETED_FILE = 0
TOTAL_DELETED_DIRS = 0

nowTime = time.time()             # Get current time in seconds
ageTime = nowTime - 60*60*24*DAYS # Back days in seconds
def delete_old_files(folder):
    """Delete files older than asked DAYS"""
    global TOTAL_DELETED_FILE
    global TOTAL_DELETED_SIZE
    for path, dirs, files in os.walk(folder):
        for file in files:
            fileName = os.path.join(path, file)     # get full path to file
            fileTime = os.path.getmtime(fileName)
            if fileTime < ageTime:
                sizeFile = os.path.getsize(fileName)
                TOTAL_DELETED_SIZE += sizeFile      # count sum of all deleted files (freespaced)
                TOTAL_DELETED_FILE += 1             # count number of deleted files
                print("Deleting file: " + str(fileName))
                os.remove(fileName)                 # Delete file

def delete_empty_dir(folder):
    global TOTAL_DELETED_DIRS
    empty_folders_in_this_run = 0
    for path, dirs, files in os.walk(folder):
        if (not dirs) and (not files):
            TOTAL_DELETED_DIRS += 1
            empty_folders_in_this_run += 1
            print("Deleting emptydir: " + str(path))
            os.rmdir(path)
    if empty_folders_in_this_run > 0:
        delete_empty_dir(folder)

#________________________________________________________________

starttime = time.asctime()

for folder in FOLDERS:
    delete_old_files(folder)    # Delete old filed
    delete_empty_dir(folder)    # Delete empty folders

finishtime = time.asctime()

print("-------------------")
print("START TIME: "                    + str(starttime))
print("Total Detected Size: "           + str(int(TOTAL_DELETED_SIZE/1024/1024)) + "MB")
print("Total Deleted Files: "           + str(TOTAL_DELETED_FILE))
print("Total Deleted Empty Folders: "   + str(TOTAL_DELETED_DIRS))
print("START TIME: " + str(finishtime))
print("____EOF_____")