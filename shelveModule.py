import shelve
#fp=shelve.open("shelve")
with shelve.open("shelve")as sh:
    sh['one']=1
    #sh[one]=2 error
    #this or this
'''fp=shelve.open("shelve")
fp['one']=1
fp['two']=2
fp['three']=3
fp.close()'''