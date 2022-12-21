import sys

filename = "/Users/aegar/Desktop/Programming/ADV_lessons/File processing/tr.txt"
while True:
    try:
        print("Inside TRY")
        myfile = open(filename, mode='r', encoding ='Latin-1')
    except Exception:
        print("Insdie exception")
        print("Error found")
        print(sys.exc_info()[1])
        filename = input("Enter filepath, please: ")
    else:
        print("Inside else")
        print(myfile.read())
        sys.exit()
    finally:
        print("Insdie finally")