# Q18. Write a Python program to extract year, month and date from an url.
import re


def extract_date(url):
    date_reg = re.compile(r"\d{1,2}\/\d{1,2}\/\d{4}")
    date = re.search(date_reg, url)
    if date is not None:
        return "Date in URL : " + str(date.group())
    else:
        return "No date of format DD/MM/YYYY was found in url."


def main():
    url = input("Please input a url : ")
    print(extract_date(url))


main()
