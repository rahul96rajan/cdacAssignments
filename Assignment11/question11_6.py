'''Q.6. Q. 1. Given a dictionary of students and their favourite colours:
people={'Arham':'Blue','Lisa':'Yellow',''Vinod:'Purple','Jenny':'Pink'}
1. Find out how many students are in the list
2. Change Lisa’s favourite colour
3. Remove 'Jenny' and her favourite colour
4. Sort and print students and their favourite colours alphabetically by name
Write a function translate() that will translate a text into "rövarspråket"
(Swedish for "robber's language").
That is, double every consonant and place an occurrence of "o" in between.
For example, translate("this is fun") should return the string
"tothohisos isos fofunon".'''
import re
from sys import path


def people_colour():
    people = {'Arham': 'Blue', 'Lisa': 'Yellow',
              'Vinod': 'Purple', 'Jenny': 'Pink'}
    print("Number of students : ", len(people.values()))
    print("Dict before removal of 'Jenny' : ", people)
    del people['Jenny']
    print("Dict before removal of 'Jenny' : ", people)
    names = list(people.keys())
    names.sort()
    for name in names:
        print("{0}'s favorite color is {1}.".format(name, people[name]))


def srl_translator(string):
    con_reg = re.compile(r"([b-df-hj-np-tv-xz])")
    return re.sub(con_reg, r"\1o\1", string)


def main():
    path.insert(1, r"/home/rahulrajan/Documents/dev/scripts/"
                r"cdacAssignments/Assignment9")
    from question2 import input_positive_integer
    print("Select any one of the option: "
          "\n1. Run People Color"
          "\n2. Run Swedish Thief Translator")
    opt = input_positive_integer("Please Select from 1 or 2 : ")
    if opt == 1:
        people_colour()
    elif opt == 2:
        string = input("Please enter some string : ")
        print("Encoded text : ", srl_translator(string))
    else:
        print("Err! Invalid option selected")


if __name__ == "__main__":
    main()
