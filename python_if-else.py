print("TASK - Given an integer, , perform the following conditional actions:\n"
      "\tIf n is odd, print Weird"
      "\tIf n is even and in the inclusive range of 2 to 5, print Not Weird\n"
      "\tIf n is even and in the inclusive range of 6 to 20, print Weird\n"
      "\tIf n is even and greater than 20, print Not Weird\n")
print("INPUT FORMAT - A single line containing a positive integer n.")
print("CONSTRAINTS - 1 <= N <= 100")
print("OUTPUT FORMAT - Print Weird if the number is weird. Otherwise, print Not Weird.")



n = int(input())
if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")
