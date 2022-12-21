import sys
import os

x =len(sys.argv)
if x > 1:
    if sys.argv[1] == "1":
        print("help requested")
    print("Arguments: " + str(sys.argv[1:]))
else:
    print("Arguments not provided")

os.system("ls -la > t.txt")
#os.mkdir("test dir")
sys.exit(2)