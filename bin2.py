#----- GLOBAL -----
SIZE = 16

#----- Functions ----
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
    binary = value[1:]
    binary = binary[::-1]
    decimal = 0
    p = 0
    for x in binary:
        if x == "1":
            decimal = decimal + 2**p
        p = p + 1
    if value[0] == "1":
        decimal = -decimal
    return decimal

def binToBin(value):
    if type(value) is not str:
        raise ValueError
    binary = ""
    base = 0
    ls = []
    if "0" in value and "1" in value:
        return value
    for x in value:
        if x not in ls:
            base = base + 1
            ls.append(x)
    if base != 2:
        print("\t###\n value", value)
        raise ValueError
    else:
        for x in value:
            if x == ls[0]:
                binary = binary + "1"
            else:
                binary = binary + "0"
    return binary

def eqlen(value1, value2):
    """
    make equal len to the shortest
        value1 = 010
        value2 = 01101

      ->value1 = 00010
      ->value2 = 01101
    """
    if type(value1) is Word and type(value2) is Word:
        if len(value1) != len(value2):
            if len(value1) > len(value2):
                value2.fill(len(value1))
            else:
                value1.fill(len(value2))
    else:
        print("eqlen: Value Error")

def eqlento(val, to):
    if type(val) is Word and type(to) is Word:
        if len(val) > len(to):
            pass
        elif len(val) == len(to):
            pass
        else:
            val.fill(len(to))
    else:
        print("eqlento: ValueError")

def set_size(string, size):
    if len(string) > size:
        #print("set_size(): error")
        raise ValueError
       # result = string[0]+string[-1:size-1]
    elif len(string) == size:
        return string
    else:
       # print("(size - len(string)):", (size - len(string)))
        result = string[0]+(size - len(string))*"0"+string[1:]
       # print("len() : ", len(result))
    return result

def autoWord(value, size):
    if type(value) is not Word:
        if type(value) is str:
            value = Word(value, size)
        elif type(value) is int:
            value = Word(value, size)
        else:
            raise ValueError
    else: pass


class Word(object):

    def __init__(self, value, size = SIZE):
        if int(size) > 3 and type(size) is int:
            self.size = abs(int(size))
        if type(value) is str:
            self.bin = binToBin(value)
            self.dec = binToDec(self.bin)
        elif type(value) is int:
            self.dec = int(value)
            self.bin = decToBin(self.dec)
        elif type(value) is Word:
            self.bin = value.bin
            self.dec = value.dec
            self.size = value.size
        else:
            print(type(value))
            print("error")

        self.bin = set_size(self.bin, size)

    def update(self):
        if self.bin != decToBin(self.dec) and len(decToBin(self.dec)) != self.size:
            self.dec = binToDec(self.bin)
    def details(self):
        return "dec: "+str(self.dec)+", \nbin: "+self.bin+", size "+str(self.size)

    def __getattr__(self):
        return self.bin

    def __repr__(self):
        return self.bin

    def __str__(self):
        astr = self.bin[0]+"."+self.bin[1:]
        bstr = str(self.dec)
        cstr = str(self.size)
        outp = "{Word}\nbinary: "+astr+"\ndecimal: "+bstr+"\nsize: "+cstr+"\n"
        return outp
       # return self.bin

    def __getitem__(self, key):
        if key <= len(self):
            return self.bin[key]
        else:
            raise IndexError

    def __len__(self):
       # print("__len__:", len(self.bin))
        return len(self.bin)

    def fill(self, lenght):
        """
        fills binary representation to given lenght

        """
       # print("\t\t\t fill(): lenght =",lenght)
        if lenght <= len(self):
            raise
        else:
            self.bin = "0"*(lenght-len(self))+self.bin
            self.size = lenght

# ---------- UNARY OPERATORS ---------------
    def __abs__(self):
        return Word(abs(self.dec))

    def __neg__(self):
        """
        unary. same as a = -a
        bin:  01001
            ->11001
        dec:
              9
            =-9

        """
        if self.bin[0] == "0":
            self.bin = "1" + self.bin[1:]
        else:
            self.bin = "0" + self.bin[1:]
        return Word(self.bin, self.size)

    def __invert__(self):
        """
        same as ~a
        return new Word invert of image
        bin:
              01001
            ->10110
        dec:  calculated
        """
        result = ""
        for x in self.bin:
            if x == "1":
                result = result + "0"
            else:
                result = result + "1"
        return Word(result, len(result))

# ---------- MATH ------------------
    def __add__(self, value):
        try:
            return Word(self.dec+value.dec, self.size)
        except ValueError:
            print("nay")
            return Word(self.dec+value.dec, value.size)
        except TypeError:
            print("nya")
        except AttributeError:
            value = Word(value)
            return Word(self.dec+value.dec, self.size)


# ---------- COMPARE ---------------
    def __eq__(self, value):
        """
        boolean:
            same as self == value
        """
        if type(value) is Word:
            if self.bin == value.bin and self.dec == value.dec:
                return True
        else:
            raise ValueError
        return False

    def __ne__(self, value):
        """
        boolean:
            same as self != value
        """
        return not self.__eq__(value)

    def __ge__(self, value):
        """
        boolean:
            same as self >= value
        """
        if type(value) is Word:
            for k in range(len(self)):
                if self[k] != value[k]:
                    if self[k] == "1" and value[k] == "0":
                        return True
                    else:
                        return False
        else:
            raise ValueError
        return True

    def __lt__(self, value):
        """
        boolean:
            same as self < value
        """
        # if self.__ge__(value):
        #     return False
        # else:
        #     return True

        return not self.__ge__(value)
        
    def __gt__(self, value):
        """
        boolean:
            same as self > value
        """
        if type(value) is Word:
            for k in range(len(self)):
                if self[k] != value[k]:
                    if self[k] == "1" and value[k] == "0":
                        return True
                    else:
                        return False
        else:
            raise ValueError
        return False

    def __le__(self, value):
        """
        boolean:
            same as self <= value
        """
        return not self.__gt__(value)
        # if self.__gt__(value):
        #     return False
        # else:
        #     return True


#----------- SHIFTS -------------
    def __lshift__(self, value):
        print("value : ", value)
        return Word(self.bin[int(value):] + "0" * int(value), self.size+int(value))

    def __rshift__(self, value):
        return Word("0" * int(value) + self.bin[:-int(value)], self.size)

    def lshift(self, value, put = 0):
        return Word(self.bin + str(put) * int(value), self.size+int(value))

    def rshift(self, value, put = 0):
        return Word(str(put) * int(value) + self.bin, self.size)

#----------- BOOLEAN -----------
    def __and__(self, value):
        """
        boolean:
            same as a & b = c
            01101
          & 01010
          = 01000
        """
        autoWord(value, self.size)

        if value.size != self.size:
            eqlento(value, self)
        result = ""
        for k in range(len(self)):
            if self.bin[k] == "1" and value.bin[k] == "1":
                result = result + "1" 
            elif self.bin[k] == "0" or value.bin[k] == "0":
                result = result + "0"
            else:
                print("\n###wtf:###\n self", self, "\nvalue", value, "\n###/wtf###\n")
        return Word(result)

    def __or__(self, value):
        """
        boolean:
            same as a | b = c
            01101
          | 01010
          = 01111
        """
        autoWord(value, self.size)

        if value.size != self.size:
            eqlento(value, self)
        result = ""
        for k in range(len(self)):
            if self[k] == "0" and value[k] == "0":
                result = result + "0"
            elif self[k] == "1" or value[k] == "1":
                result = result + "1"
            else:
                print("\n###wtf:###\n self", self, "\nvalue", value, "\n###/wtf###\n")
        return Word(result)



    def __xor__(self, value):
        """
        boolean:
            same as not-or method but with another syntax
            a ^ b = c
        """
        autoWord(value, self.size)

        if value.size != self.size:
            eqlento(value, self)
        result = ""
        for k in range(len(self)):
            if self[k] == "1" or value[k] == "1":
                result = result + "0"
            elif self[k] == "0" and value[k] == "0":
                result = result + "1"
            else:
                print("\n###wtf:###\n self", self, "\nvalue", value, "\n###/wtf###\n")
        return Word(result)



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

    def __rxor__(self, value):
        """
        boolean:
            same as __xor__ method
        """
        pass

#--------- CODE ----------
def code(value):
    if type(value) is Word:
        result = "1"+"0"*(value.dec-1)
    elif type(value) is int:
        result = "1" + "0"*(value)
    else:
        raise

def decode(value):
    return len(value)
    #return value.index("1")