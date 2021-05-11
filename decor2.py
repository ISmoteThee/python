class P:

    def __init__(self,x):
        self._x = x

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        if x < 0:
            self._x = 0
        elif x > 1000:
            self._x = 1000
        else:
            self._x = x

    @x.deleter
    def x(self):
        del self._x