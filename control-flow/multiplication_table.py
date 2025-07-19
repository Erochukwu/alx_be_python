number = int(input("Enter a number to see its multiplication table: "))
for X in number:
    for Y in range (1, 11):
        product = X * Y
        print(f"{X} * {Y} = {product}", end = "\t")
    print()
    