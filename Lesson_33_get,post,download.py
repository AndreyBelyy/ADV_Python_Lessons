from urllib import request, parse
import sys

myUrl = "https://google.com/search?"
value = {'q': 'ANDESA Soft'}

myheader = {} # additional info for google, to get request
myheader['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'



try:
    mydata = parse.urlencode(value)
    print(mydata)
    myUrl = myUrl + mydata
    req = request.Request(myUrl, headers=myheader)
    otvet = request.urlopen(req)
    otvet = otvet.readlines()
    for line in otvet:
        print(line)
except Exception:
    print("Error occuried during web request!")
    print(sys.exc_info()[1])


#_______Download file________#

myUrl = "https://upload.wikimedia.org/wikipedia/commons/f/f1/Vie_de_J%C3%A9sus_%28Ernest_Renan%29.jpg"
myFile = "/Users/aegar/Desktop/Test.jpg"

try:
        print("Start downloading file from: " + myUrl)
        request.urlretrieve(myUrl, myFile)
except Exception:
    print("ACHTUNG!")
    print(sys.exc_info())
    exit()
print("File downloaded and saved at Desktop")
