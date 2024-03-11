print("Type in a positive number")
num = int(input("Number is "))
if num < 0:
    print("Try a positive number")
else:
    def armstrong_num(num):
        num_string = str(num)
        num_length = len(num_string)
        digits_summation = sum(int(digit) ** num_length for digit in num_string)
        return num == digits_summation


    if armstrong_num(num):
        print(num, "number is an Armstrong number.")
    else:
        print(num, "number is not an Armstrong number.")
