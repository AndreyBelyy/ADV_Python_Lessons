
import re

mytext = "Vasya aaaaaaaa 1972,  Kolya - 19727777: Olesya 1981, aaaaaa@intel.com," \
         "bbbbbbbbbb@intel.com, Petya ggggggggg, 1992,cccccccccc@yahoo.com,  " \
         "ddddddddddd@intel.com, vasya@yandex.net, hello hello, Misha #43 1984, " \
         "Vladimir 1977, Irina , 2001,  annnnnnn@intel.com, eeeeeeee@yandex.com," \
         "ooooooooooo@hotmai.gov, gggggggggggg@gov.gov, tututut@giv.hot"

"""
\d = any digit
\D = Any non DIGIT
\w = Any alphabet symbol [A-Z a-z]
\W = Any non-alphabet symbol
\s = backspace
\S = non breakspace

[0-9]{3}
[A-Z][a-z]+
\w

"""

# text_for_look = r"[0-9]{3}" # = r"\d\d\d\"
#text_for_look = r"@\w+\.\w+" # any symbols before point and after the point
#text_for_look = r""


allresults = re.findall(text_for_look, mytext)
print(allresults)