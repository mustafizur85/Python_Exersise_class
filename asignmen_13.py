
# Example_ 1
lst = []
user_input = True
while user_input:
    num = int(input("Enter Number ="))
    if num%10 ==0:
        lst.append(num)
        print("print divisible list =",lst)
    elif num>120:
        break

print("..............")
# Example-2
user_input = True


while user_input:
    num = int(input("Enter Number = "))
    if num % 10 ==0:
        print(num," is divisible Number")
    elif num > 120:
            break