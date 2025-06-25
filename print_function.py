print("TASK - The included code stub will read an integer, , from STDIN.\n"
      "\tWithout using any string methods, try to print the following:\n"
      "\tNote that "" represents the consecutive values in between.")
print("EXAMPLE - n = 5 prints the string '12345'")
print("INPUT FORMAT - first line contains the integer n")
print("CONSTRAINTS - 1 <= n <= 150")
print("OUTPUT FORMAT - print the list of integers from 1 to n as a string without spaces")

while True:
    n = int(input())
    if 1 <= n <= 150:
        break
    else:
        print("Invalid input. Please enter a number between 1 to 150")
inc = n-1
for i in range(n):
    print(n-inc,end="")
    inc -= 1

