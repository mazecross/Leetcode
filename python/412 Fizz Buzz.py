'''
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
'''
#xxy 2016.12.4 UoM
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        
        """
        a=[];
        if n==0:
            return a
        for i in range(1,n+1):
            if i%15==0:
                #print "FizzBuzz"
                a.append('FizzBuzz')
            elif i%5==0:
                #print "Buzz"
                a.append("Buzz")
            elif i%3==0:
                #print "Fizz"
                a.append("Fizz")
            else:
                
                a.append(str(i))
                
        return a 
