import math
class no_rat:
    def __init__(self, a, b):
        if b==0:
            print("Denominator cannot be zero")
            self.a=None
            self.b=None
        else:
            self.a=a
            self.b=b
    def __str__(self):
        if self.a is None or self.b is None:
            return "Undefined"
        else:
            return f"{self.a}/{self.b}"
    def subtract(self,other):
        if self.a is None or self.b is None or other.a is None or other.b is None:
            return None
        lcm=self.b*other.b//math.gcd(self.b,other.b)
        self_num=self.a*(lcm//self.b)
        other_num=other.a*(lcm//other.b)
        if self_num==other_num:
            return 0
        elif self_num<other_num:
            return -1
        else:
            return 1
    def divide(self,other):
        if self.a is None or self.b is None or other.a is None or other.b is None:
            return None
        if other.a==0:
            print("Zero divisor is not allowed")
            return None
        result_a=self.a*other.b
        result_b=self.b*other.a
        gcd=math.gcd(result_a,result_b)
        return no_rat(result_a//gcd,result_b//gcd)
    def power(self,n):
        if self.a is None or self.b is None:
            print("Undefined")
            return None
        if n==0:
            print("Error: Zero to the power of zero is undefined")
            return None
        result_a=self.a**abs(n)
        result_b=self.b**abs(n)
        if n<0:
            result_a,result_b=result_b,result_a
        gcd=math.gcd(result_a,result_b)
        return no_rat(result_a//gcd,result_b//gcd)