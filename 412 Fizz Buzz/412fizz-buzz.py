class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        list = []
        for i in range(1,n+1):
            divbythree = (i % 3 is 0)
            divbyfive = (i % 5 is 0)
            string = ""
            if(divbythree and divbyfive):
                string += "FizzBuzz"
            elif(divbythree):
                string += "Fizz"
            elif(divbyfive):
                string += "Buzz"
            else:
                string += str(i)
            list.append(string)
        return list
        