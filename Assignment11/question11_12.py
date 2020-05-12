'''Q. 11.In English, present participle is formed by adding suffix -ing to
infinite form: go -> going. A simple
set of heuristic rules can be given as follows:
If the verb ends in e, drop the e and add ing
(if not exception: be, see, flee, knee, etc.)
If the verb ends in ie, change ie to y and add ing
For words consisting of consonant-vowel-consonant, double the final letter
before adding ing
By default just add ing
Your task in this exercise is to define a function make_ing_form() which given
a verb in infinitive form
returns its present participle form. Test your function with words such as lie,
see, move and hug.
However, you must not expect such simple rules to work for all cases.'''
import re


def make_ing_form(string):
    temp_string = string
    temp_string = string.lower()
    cvc_reg = re.compile("[b-df-hj-np-tv-xz][aeiouy][b-df-hj-np-tv-xz]")
    if re.match(cvc_reg, temp_string[-3:]):
        return string+string[-1]+"ing"
    elif temp_string.endswith("ie"):
        return string[0:-2]+"ying"
    elif temp_string.endswith("e"):
        if temp_string.endswith("ie"):
            return string[0:-2]+"ing"
        return string if ['be', 'bee', 'see', 'flee', 'knee']\
            .count(temp_string) > 0 else string[0:-1]+"ing"
    else:
        return string+"ing"


def main():
    word = input("Please enter a word : ").strip()
    print("Present participle form  of '{0}' is '{1}'".
          format(word, make_ing_form(word)))


if __name__ == "__main__":
    main()
