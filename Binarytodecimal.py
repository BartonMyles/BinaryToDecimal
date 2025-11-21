print("Choose an option:")
print("1. Binary to Decimal")
print("2. Decimal to Binary")

choice = input("Enter 1 or 2: ")

if choice == '1':
    binary = input("Enter a binary number: ")
    decimal = 0
    power = 0
    for digit in reversed(binary):
        if digit not in ('0', '1'):
            print("Invalid binary number!")
            exit()
        if digit == '1':
            decimal += 2 ** power
        power += 1
    print("Decimal value =", decimal)

elif choice == '2':
    decimal = int(input("Enter a decimal number: "))
    if decimal < 0:
        print("Please enter a non-negative number!")
        exit()
    binary = ''
    if decimal == 0:
        binary = '0'
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    print("Binary value =", binary)

else:
    print("Invalid choice!")
