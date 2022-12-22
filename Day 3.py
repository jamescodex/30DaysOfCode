class CodesCracker:
    def checkLeapOrNot(self, x):
        if y % 4 == 0 and y % 100 != 0:
            return 1
        elif y % 400 == 0:
            return 1

print("Enter the Year: ", end="")
y = int(input())

ob = CodesCracker()
chk = ob.checkLeapOrNot(y)
if chk==1:
    print("\nLeap Year")
else:
    print("\nNot a Leap Year")