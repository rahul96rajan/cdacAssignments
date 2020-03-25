'''Exercise 1: Write a program to prompt for a file name, and then read through
 the file line-by-line. Note: the file name is Erle.txt and its content is,

Erle is the enabling technology for the
next generation of aerial and terrestrial
robots that will be used in cities solving
tasks such as surveillance, enviromental
monitoring or even providing aid at catastrophes.

Ensure you create the file.'''

import os
import sys


def create_txt_file(data_to_write, accessMode,
                    file_name=os.path.basename(sys.argv[0]).split(".")[0]):
    file_dir = os.path.join(os.getcwd(), r"Assignment10/textFiles",
                            file_name+r".txt")
    with open(file_dir, accessMode) as file:
        file.write(data_to_write)
        print("[SUCCESS] Written given data to file : ", file_name+".txt")


def read_file_from_top_down(file_name):
    file_dir = os.path.join(os.getcwd(), r"Assignment10/textFiles",
                            file_name+r".txt")
    if os.path.exists(file_dir):
        with open(file_dir, "r+") as file:
            return file.read()
    else:
        return "[WARNING] File '{}' doesn't exists!".format(file_dir)


def main():
    file_name = "erle"
    data = ("Erle is the enabling technology for the\n"
            "next generation of aerial and terrestrial\n"
            "robots that will be used in cities solving\n"
            "tasks such as surveillance, enviromental\n"
            "monitoring or even providing aid at catastrophes.")
    create_txt_file(data, "w+", file_name)
    print("\n::::::: Content(s) read from file '{}.txt'"
          " :::::::".format(file_name))
    print(read_file_from_top_down(file_name))


if __name__ == '__main__':
    main()
