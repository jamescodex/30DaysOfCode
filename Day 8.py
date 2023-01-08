print(end="Enter a Number: ")
n = int(input())

rev = 0
o = n
while n>0:
    rem = n % 10
    rev = rem + (rev*10)
    n = int(n / 10)

if o==rev:
    print("\n" +str(o)+ " (Original) = " +str(rev)+ " (Reverse)")
else:
    print("\n" +str(o)+ " (Original) != " +str(rev)+ " (Reverse)")