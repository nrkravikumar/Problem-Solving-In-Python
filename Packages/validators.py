
import re

def phonenumberValidator(number):
    pattern = "^[6-9][0-9]{9}$|^[0][6-9][0-9]{9}$|^[+](91)[6-9][0-9]{9}"
    if re.match(pattern,str(number)):
        return True
    return False


def emailValidator(email):
    pattern = "^[a-z0-9][a-z0-9._]{4,13}[0-9a-z][@][a-z0-9]{3,18}[.][a-z]{2,4}"
    if re.match(pattern,email):
        return True
    return False

