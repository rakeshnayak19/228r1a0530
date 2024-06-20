import re
s="ab ab cd ef 1, 2 ,3 "
#k=re.findall("[^cmr]",s)#not abc
#b=re.sub("\d","#",s)
a=re.findall(".a",s)
print(a)