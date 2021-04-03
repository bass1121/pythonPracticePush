def validate_pin(pin):
    if len(str(pin)) == 4 or len(str(pin)) == 6 and type(pin) == int and pin >= 0:
        return True
    else:
        return False

 
print(validate_pin(1234))
print(validate_pin(5.667)) 


"""

"""
def validate_pin(pin):
    if int(pin) >= 0:
        if len(str(pin)) == 4 or len(str(pin)) == 6:
            if type(pin) is int or type(pin) is str:
                return True
            return False
    return False

