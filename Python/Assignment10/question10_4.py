'''Exercise 4: Define a class called Songs, it will show the lyrics of a song.
Its __init__() method should have two arguments:self and lyrics.
lyricsis a list.Inside your class create a method called sing_me_a_song that
prints each element of lyrics on his own line. Define a varible:
happy_bday = Song(["May god bless you, ",
                   "Have a sunshine on you,",
                   "Happy Birthday to you !"])
Call the sing_me_song method on this variable.
'''
from question10_1 import read_file_from_top_down


class Songs:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_song(self):
        return '\n'.join(self.lyrics)


def file_to_list(file_path=r"/home/rahulrajan/Documents/dev/scripts/"
                 "cdacAssignments/Assignment10/textFiles/song"):
    return read_file_from_top_down(file_path).split("\n")


def main():
    song_as_list = file_to_list()
    print("-"*50, "\n::: Here you see the song as a list :::\n", song_as_list)
    my_song = Songs(file_to_list())
    print("-"*50, "\n::: And here is the song unified :::\n")
    print(my_song.sing_me_song())


if __name__ == "__main__":
    main()
