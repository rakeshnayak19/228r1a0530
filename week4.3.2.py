def remove_word(str, w):
    return str.replace(w, '')


str1= "hello cmrec hello"
print("--Before removing--")
print(str1)
print("--After removing--")
print(remove_word(str1, "hello"))