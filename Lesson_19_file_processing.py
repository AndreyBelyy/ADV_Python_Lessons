
input_file = "/Users/aegar/Desktop/Programming/ADV_lessons/File processing/names.txt"
input_file2 = "/Users/aegar/Desktop/Programming/ADV_lessons/File processing/pass.txt"
outputfile = "/Users/aegar/Desktop/Programming/ADV_lessons/File processing/out_pass.txt"

password_to_find = "kol"

myfile = open(input_file2, mode='r', encoding='latin_1')
myfile2 = open(outputfile, mode='a', encoding='latin_1')

#list = []
for num, line in enumerate(myfile, 1):
    if password_to_find in line:
        # list.append(line)
        print("Line #: " + str(num) + ": " + line.strip())
        myfile2.write("Found password: " + line)
        # print(list)

myfile.close()
myfile2.close()

