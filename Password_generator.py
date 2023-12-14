from random import randint

char_nr = randint(8, 20)

def ran_gen():

    let = randint(0, 25)
    letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
              "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    num = randint(0, 9)
    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    char = randint(0, 5)
    character = ["!", "#", "€", "%", "&", "/"]

    random_char = randint(0, 10)

    for i in range(char_nr):
        if random_char < 3:
            return letter[let]
        elif random_char < 5:
            return letter[let].capitalize()
        elif random_char < 8:
            return number[num]
        else:
            return character[char]

def pw_gen():

    pw = []

    for i in range(char_nr):
        pw.append(ran_gen())

        if len(pw) < char_nr:
            continue
        elif len(pw) == char_nr:
            print("Your password:")
            print(*pw,sep='')

pw_gen()
