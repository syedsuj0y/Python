10# Function to print binary number fron decimal

def decimalToBinary(n):
   if n == 0:
       return '0'
   else:
       binary = ''
       while n >= 1:
           binary = str(n%2) + binary  # storing moduler 1 or 0 to binary
           n = n // 2
   return(binary)

decimal = input("Enter a decimal number :")
attempt = 0
while not decimal.isdigit() and attempt <= 3:            # input validation
    print("Please use whole number!")
    attempt += 1
    decimal = input("Enter a decimal number : ")
    if not decimal.isdigit():
        decimal = '0'
        print("Try again later!!")
decimal = int(decimal)
print('The Binary of ', decimal, '=', decimalToBinary(decimal))
