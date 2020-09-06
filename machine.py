class Pin:
    IN = 0
    OUT = 1
    val=0
    PULL_DOWN=0

    def __init__(self, id, mode=-1, pull=- 1):
        a = 4

    def value(self,x=None):

        if (x==None):
            return self.val
        else:
            self.val=x
