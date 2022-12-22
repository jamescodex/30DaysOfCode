class CodesCracker:
    def checkPrime(self, x):
        for i in range(2, x):
            if n%i==0:
                return 1

print("Enter a Number: ", end="")
n = int(input())

obj = CodesCracker()
p = obj.checkPrime(n)
if p==1:
    print("\nNot Prime Number")
else:
    print("\nPrime Number")