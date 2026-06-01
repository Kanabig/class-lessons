_signInedMemberId = ""


def setSignInedMemberId(id=""):
    global _signInedMemberId
    _signInedMemberId = id


def getSignInedMemberId():
    return _signInedMemberId
