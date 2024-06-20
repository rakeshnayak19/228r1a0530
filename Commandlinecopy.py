from sys import argv

if 3 == len(argv):
    try:
        fp1 = open(argv[1], "r")
        fp2 = open(argv[2], "w+")
        for i in fp1:
            fp2.write(i)
        print("copied successfully")
        fp2.seek(0, 0)
        c = fp2.read()
        print(c)
        fp1.close()
        fp2.close()
    except Exception:
        print("error")