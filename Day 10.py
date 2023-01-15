print("Enter a Number: ", end="")
n = int(input())
rv = 0
t = n
while t>0:
    rm = t % 10
    rv = rm + (rv * 10)
    t = int(t / 10)
if rv==n:
    print("\n" + str(n) + " is a Palindrome Number")
else:
    print("\n" + str(n) + " is not a Palindrome Number")