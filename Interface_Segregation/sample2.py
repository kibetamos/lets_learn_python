from unittest import result


class AdvancedArithmetic(object):

    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        result = 0
        for i in range(1,n+1):
            if(n % i == 0):
                result += i
        return result
