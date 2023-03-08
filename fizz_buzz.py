class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        myresult = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                myresult.append("FizzBuzz")
            elif i % 3 == 0:
                myresult.append("Fizz")
            elif i % 5 == 0:
                myresult.append("Buzz")
            else:
                myresult.append(str(i))
        return myresult