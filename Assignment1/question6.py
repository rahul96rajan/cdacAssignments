# Question 6 : If a five-digit number is input through the keyboard, write a program to calculate the sum of its digits. (Hint: Use the modulus operator ‘%’)

number = input("Please enter a number : ").strip()
numSum = 0
for i in range(0, len(number)):
    numSum += int(number[i])

print("Sum of digits of number ", numSum)