import re
def validate_email(email):
    Pattern=r"^[a-zA-Z0-9+._-]+@[a-zA-z0-9+_-]+\.[a-zA-z0-9-]+$"
    f=re.match(Pattern,email)
    return f
#email=input()
