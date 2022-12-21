import re

input_filename = "/Users/aegar/Desktop/Programming/ADV_lessons/File processing/test_data.txt"
result_filename = "./results.txt"

myfile = open(input_filename,mode='r',encoding='Latin-1')
resultfile = open(result_filename, mode='w', encoding='Latin-1')
mytext = myfile.read()

lookfor = r"[\w.-]+@(?!icloud)[A-Za-z]+\.[\w.]+"  # lookfor = r"[\w.-]+@[A-Za-z]+\.[\w.]+"  # =  r'[\w]+@\w+.\w+'

results = re.findall(lookfor, mytext)

for x in results:
    print(x)
    resultfile.write(x + "\n")

print("Total: " + str(len(results)))