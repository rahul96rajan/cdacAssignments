# Question 7 : Write a Python program to accept a filename from the user and print the extension of that.

fileName = input("Please enter the name of the file : ")
print("The extension of the file is =>", fileName.split(".")[-1])