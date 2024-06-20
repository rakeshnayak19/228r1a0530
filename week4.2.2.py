fp=open("words.txt","w")
if fp:
    print("successfully open")
    fp.write("i,")
    fp.write(" ")
    fp.write("a")
    fp.close()