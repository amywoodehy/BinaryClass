__doc__ = 
"""

"""

def decToBin(value):
    #without sign works!
    #return bin(value)[2:]
    if(value < 0):
        result = "1"
    else:
        result = "0"

    result = result + bin(abs(value))[2:]
    return result

def binToDec(value):
    иштфкн = value[1:]

    pass

def binToBin(value):
    
    pass

def eqlen(value1, value2):
    if len(value1) != len(value2):
        if len(value1) > len(value2):
            value2.fill(len(value1))
        else:
            value1.fill(len(value2))

class BinWord(object):
    """
    
    """
    def __init__(self, value,  is_bin = False):
        if is_bin:
            self.bin = binToBin(value)
            self.dec = binToDec(self.bin)
        else:
            self.dec = int(value)   
            self.bin = decToBin(self.dec)
        #self.mod = False

    def __getattr__(self):
        return self.bin

    def __abs__(self):
        """
        returns absolute value of variable:
        11101 -> 01101
        01101 -> 01101
        """
        # result = BinWord(mod(self.dec))
        # or
        # result.bin = "0"+self.bin[1:] #doesn't care about sign bit
        return BinWord(abs(self.dec))

    def modificate(self, modifier = 2):
        """
        don't use it

        modificates code
        does not return
        11101 -> 111101
        01101 -> 001101
        """
        self.bin = self.bin[0]*modifier + self.bin[1:]
        self.modifier = True

    def __len__(self):
        return len(self.bin)

    def fill(self, lenght):
        """
        fills binary representation to given lenght

        """
        if lenght <= len(self):
            raise
        else:
            self.bin = "0"*(lenght-len(self))+self.bin

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

    def __setitem__(self, where, what):
        if what in (0, 1):
            self.bin = self.bin[:where]+str(what)+self.bin[where+1:]
        self.dec = binToDec(self.bin)

#as boolean type
    def __and__(self, value):
        """
        boolean:
            same as a & b = c
            01101
          & 01010
          = 01000
        """
        if len(self) != len(value):
            if len(self) > len(value):
                value.fill(len(self))
            else:
                self.fill(len(value))


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

