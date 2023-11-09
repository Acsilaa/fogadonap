

def isValidPass(pass): 
        pass = list(pass)

    def hasInt(pass):

        for i in pass:
            if i.isDigit():
                return True

    def hasChar(pass):
        
        chars = ["#", "!", "@", "(", ")", "*", "%"]
        for i in pass:
            if i in chars
            return True

    def hasLoverCase(pass):

        for i in pass:
            if i.islover():
                return True
    
    def hasUpper(pass):

        for i in pass:
            if i.isupper():
                return True

    if hasUpper() and hasLover() and hasChar() and hasInt():
        return True
    else:
        return False