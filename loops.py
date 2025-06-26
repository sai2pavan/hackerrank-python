print("TASK - The provided code stub reads an integer n from STDIN. For all non-negative integers i < n print i^2")
print("EXAMPLE - For n = 3, The list of non-negative integers that are less than n=3 is [0,1,2] Print the squares of each number on a seperate line")
print("INPUT FORMAT - The first and the only line contains integer n")
print("OUTPUT FORMAT - Print n lines correcponding to each i")
print("CONSTRAINTS - 1 <= n <= 20")

while True:
    n = int(input())
    if 1 <= n <= 20:
        break
    else:
        print("Invalid input, Please enter a number between 1 and 20")  
for i in range(n):
    print(i**2)
