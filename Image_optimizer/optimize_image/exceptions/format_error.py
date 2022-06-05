

class FormatError(Exception):

    def __init__(self, errcode, errmsg):
        self.errcode = errcode
        self.errmsg = errmsg
        
    def __str__(self):
        return (
            "FormatError %s: %s" %
            (self.errcode, self.errmsg)
            )
