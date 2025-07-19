rows = int(input("Enter the size of the pattern: "))

for i in range(1, rows + 1):
    for i in range(1, i + 1):
        print("*", end="")
        