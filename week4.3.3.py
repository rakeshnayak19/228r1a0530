def convert(s):

    ch=list(s)
    for i in range(len(s)):
        if i==0 and ch[i]!=' ':
            if ch[i] >='a' and ch[i]<='z':
                ch[i]=chr(ord(ch[i])-ord('a')+ord('A'))
        s="",ch[i]
    return s
print(convert("welcome sir"))