# TEE RATKAISUSI TÄHÄN:

import math
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02d} eur"
    
    def __eq__(self, another:"Money"):
        if  self.__euros == another.__euros:
            if self.__cents == another.__cents:
                return True
        return False
    
    def __lt__(self,another:"Money"):
        if  ( self.__euros + self.__cents ) < (another.__euros + another.__cents):
            return True
        else:
            return False
    
    def __gt__(self,another:"Money"):
        if  ( self.__euros + self.__cents ) > (another.__euros + another.__cents):
            return True
        else:
            return False
        
    def __ne__(self, another:"Money"):
        if  ( self.__euros + self.__cents ) != (another.__euros + another.__cents):
            return True
        else:
            return False
    
    def __add__(self,another:"Money"):
        our_total = float(f"{self.__euros}.{self.__cents:02d}")
        another_total = float(f"{another.__euros}.{another.__cents:02d}")

        addition = str(our_total + another_total)
        euros = int(addition.split(".")[0])
        cents = int(addition.split(".")[1].ljust(2,"0"))
      
        return Money(euros,cents)

    def __sub__(self,another:"Money"):
        our_total = float(f"{self.__euros}.{self.__cents:02d}")
        another_total = float(f"{another.__euros}.{another.__cents:02d}")

        subtraction = str(round(float(our_total - another_total),2))
        
        if float(subtraction) < 0:
            raise ValueError("a negative result is not allowed")
        
        euros = int(subtraction.split(".")[0])
        cents = int(subtraction.split(".")[1].ljust(2,"0"))
        return Money(euros,cents)

if __name__ == "__main__":
    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    #print(e3)
    print(e4)

    #e5 = e2-e1
    #print(e5)