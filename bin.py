__doc__ = """

"""

def decToBin(value):
    return "000"

def binToDec(value):
    pass

def binToBin(value):
    pass

class BinWord(object):
    """
    
    """
    def __init__(self, value,  is_bin = False):
        if is_bin:
            self.dec = binToDec(value)
            self.bin = binToBin(value)
        else:
            self.dec = int(value)   
            self.bin = decToBin(value)

    def __getattr__(self):
        return self.bin

    def __abs__(self):
        """
        returns absolute value of variable:
        11101 -> 01101
        01101 -> 01101
        """
        pass

    def modificate(self, modifier = 2):
        """
        modificates code
        does not return
        11101 -> 111101
        01101 -> 001101
        """
        pass

    def __repr__(self):
        """
        "dec: "+str(self.dec)+", bin: "+self.bin
        """
        return "dec: "+str(self.dec)+", bin: "+self.bin

    def __str__(self):
        """
        called in print() and in str()
        """
        return self.bin

#as boolean type
    def __and__(self, value):
        """
        boolean:
            same as a & b = c
            01101
          & 01010
          = 01000
        """
        pass

    def __or__(self, value):
        """
        boolean:
            same as a | b = c
            01101
          | 01010
          = 01111
        """
        pass

    def __rand__(self, value):
        """
        boolean:
            same as __and__ method <=> a & b = c
        """
        pass

    def __ror__(self, value):
        """
        boolean:
            same as __or__ method <=> a | b = c
        """
        pass

    def __xor__(self, value):
        """
        boolean:
            same as __or__ method but with another syntax
            a ^ b = c
        """
        pass

    def __rxor__(self, value):
        """
        boolean:
            same as __rxor__ method
        """
        pass

#compare operators
    def __eq__(self, value):
        """
        boolean:
            same as self == value
        """
        pass

    def __ne__(self, value):
        """
        boolean:
            same as self != value
        """
        pass

    def __ge__(self, value):
        """
        boolean:
            same as self >= value
        """
        pass

    def __gt__(self, value):
        """
        boolean:
            same as self > value
        """
        pass

    def __le__(self, value):
        """
        boolean:
            same as self <= value
        """
        print("lolo")
        pass

    def __lt__(self, value):
        """
        boolean:
            same as self < value
        """
        pass

#shifts
    def __lshift__(self, value, put = '0'):
        pass

    def __rshift__(self, value, put = '0'):
        pass

