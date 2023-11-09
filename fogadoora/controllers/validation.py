from .. import models as m 

def isValidPass(pwd): 
    pwd = list(pwd)

    def passHasInt(pwd):

         for i in pwd:
             if i.isDigit():
                 return True

    def passHasChar(pwd):
        
        chars = ["#", "!", "@", "(", ")", "*", "%"]
        for i in pwd:
            if i in chars:
                return True

    def passHasLover(pwd):

        for i in pwd:
            if i.islover():
                return True
    
    def passHasUpper(pwd):

        for i in pwd:
            if i.isupper():
                return True

    def passIsLong(pwd):
        
        if len(pwd) <= 7:
            return False

    if passHasUpper() and passHasLover() and passHasChar() and passHasInt() and passIsLong():
        return True
    else:
        return False

def isValidUname(uname):

    def unIsLong(uname):
        if (m.doesUserExist()):
            if len(uname) > 0 and len(uname) < 40:
                return True
            else:
                return False
    
    return unIsLong()
   
        