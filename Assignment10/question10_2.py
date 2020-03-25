'''Exercise 2:Create a file called new_world.txt.First add a new line to the
 file:Welcome to robotics time..
 And then print the content of new_world.txt.'''

from question1 import create_txt_file, read_file_from_top_down


def main():
    data = "Welcome to robotics time..(´･_･`)"
    file_name = "new_world"
    create_txt_file(data, "w+", file_name)
    print("\n::::::: Content(s) read from file '{}.txt'"
          " :::::::".format(file_name))
    print(read_file_from_top_down(file_name))


if __name__ == "__main__":
    main()
