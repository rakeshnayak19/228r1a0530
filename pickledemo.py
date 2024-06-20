import pickle
fp=open("pickle1.txt" , "wb" )
cn=["dhoni","virat","dhawan"]
pickle.dump(cn,fp)
fp.close()