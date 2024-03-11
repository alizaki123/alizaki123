#Authors:1-Ali Mahmoud Mohamed Zaki / Problems 2,5
        #2-Ammar Sayed Mansour Mohamed / Problem 3,4
        #3-Rajeh Ahmed Saleh Saad /Problems 1,6

#Version: 1.0

#Date: 28/2/2024


def menu():
    print("1: is used to take the mark and prints the grade")
    print("2: is used to take a number and checks if it is an armstrong number or not")
    print("3: is used to take an approximate value of the pie (π)")
    print("4: is used to make an encryption for data entered")
    print("5: is used to check if two lists have the same elements or not")
    print("6: is used to find all factors of any positive number")
    print("Choose a number of the task you want to use, 1 for ")
    menu()


while True:
    choice = int(input("Choose your choice from 1 to 6: "))
    if choice < 1 and choice > 6:
        print("Choose a number from 1 to 6")
        break
    else:
        if choice == 1:
            mark = float(input("Enter the mark \n"))
            if mark >= 90:
                print("your average is: A+")
            elif mark >= 85:
                print("your average is: A")
            elif mark >= 80:
                print("your average is: A-")
            elif mark >= 75:
                print('your average is: B+')
            elif mark >= 70:
                print("your average is: B")
            elif mark >= 65:
                print("your average is: B-")
            elif mark >= 60:
                print("your average is: C+")
            elif mark >= 55:
                print("your average is: C")
            elif mark >= 50:
                print("your average is: C-")
            elif mark >= 45:
                print("your average is: D+")
            elif mark >= 40:
                print("your average is: D")
            else:
                print("your average is: F")

        elif choice == 2:
            print("Type in a positive number")
            num = int(input("Number is "))
            if num < 0:
                print("Try a positive number")
            else:
                def armstrong_num(num):
                    num_str = str(num)
                    num_length = len(num_str)
                    digits_sum = sum(int(digit) ** num_length for digit in num_str)
                    return num == digits_sum


                if armstrong_num(num):
                    print(num, "number is an Armstrong number.")
                else:
                    print(num, "number is not an Armstrong number.")

        elif choice == 3:
            print("Welcome")
            while True:
                n = int(input("Enter number of terms: "))
                if n <= 0:
                    raise ValueError
                break
            try:
                pi = 0
                sign = 1
                for i in range(1, n * 2, 2):
                    pi += sign * (1 / i)

                    sign *= -1
                pi *= 4
                result = pi

                print(f"the estimated value of Pi using {n} terms is: {result}")
            except ValueError:
                print("enter a positive integer number")


        elif choice == 4:
            print("Welcome")
            while True:
                message = str(input("enter a message : "))
                result = ""
                alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                         "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                         "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
                count = 0
                for char in message:
                    if char == "z":
                        next_char = "a"
                    elif char == "Z":
                        next_char = "A"
                    else:
                        if char in alpha:
                            next_char = alpha[alpha.index(char) + 1]
                        else:
                            next_char = char
                    result += next_char
                count += 1
                if count == 1:
                    print(result)
                    break

        elif choice == 5:
            list_1 = []
            list_2 = []
            count = 0
            print("Type in list 1, when you finish your list type 'z' ")
            while True:
                digits_1 = str(input("Number is "))
                if digits_1 != 'z':
                    list_1.append(digits_1)
                    print(list_1, "Do you want to add more to list 1")
                else:
                    break
            print("Type in list 2, when you finish your list type 'z' ")
            while True:
                digits_2 = str(input("Number is "))
                if digits_2 != 'z':
                    list_2.append(digits_2)
                    print(list_2, "Do you want to add more to list 2")
                else:
                    break
            print(list_1)
            print(list_2)
            for i in list_1:
                if i not in list_2:
                    count += 1
                    break
            for i in list_2:
                if i not in list_1:
                    count += 1
                    break
            if count == 0:
                print("Elements are the same")
            else:
                print("Elements are different")

        elif choice == 6:
            import math


            def find_factors(num):
                factors = []
                i = 1

                while i <= math.sqrt(num):
                    if num % i == 0:
                        factors.append(i)
                        if i != math.sqrt(num):
                            factors.append(num // i)
                    i += 1

                factors.sort()
                return factors


            # Test the program
            num = int(input("Enter a positive integer:\n "))

            factors = find_factors(num)
            print("Factors of", num, "are:", factors)








