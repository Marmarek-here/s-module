import sys
from .s import s

class CallableModule(sys.modules[__name__].__class__):
    def __call__(self, length=0):
        return s(length)

sys.modules[__name__].__class__ = CallableModule