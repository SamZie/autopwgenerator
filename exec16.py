

import random
import sys

def the_first_three(pw_length, lowerlist, upperlist, numlist,pw):
    list_lists = [lowerlist, upperlist, numlist]
    counter = 0
    char_max = 3
    print(list_lists)
    while counter < char_max:
        pw.append(random.choice(list_lists[random.randrange(0,len(list_lists))]))
        pw_string = "".join(str(item) for item in pw)

        if any(char.isdigit() for char in pw_string) == True:
            try:
                list_lists.remove(numlist)
            except:
                print("numlist already gone")
        if any(char.isupper() for char in pw_string) == True:
            try:
                list_lists.remove(upperlist)
            except:
                print("upperlist already gone")
        if any(char.islower() for char in pw_string) == True:
            try:
                list_lists.remove(lowerlist)
            except:
                print("lowerlist already gone")

        counter += 1
        pw_length +=1
    return pw_length

def print_gen_pw(pwlist):
    pw_string = "".join(str(item) for item in pwlist)
    print("the generated pw is: {}".format(pw_string))


def randomPWgenerator(lowercasealph, uppercasealph, numberslist):
    length_pw = 0
    pw=[]
    pw_range = random.randrange(10,15)

    while length_pw <= pw_range:
        if length_pw == 0: #ensures that theres is atleast one lower one upper and one num char
            the_first_three(length_pw, lowercasealph, uppercasealph, numberslist, pw)
            length_pw = 2

        else:
            key_list=[lowercasealph, uppercasealph, numberslist]
            pw.append(random.choice(key_list[random.randrange(0,3)]))
        length_pw += 1

    print_gen_pw(pw)


def main():
    lc_alph = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    up_alph = []
    numbers = []

    #creates a UPPERcase version of alphabet
    for letter in lc_alph:
        up_alph.append(letter.upper())


    #create a list from 1 to 9
    i = 1
    while i <= 9:
        numbers.append(i)
        i += 1

    randomPWgenerator(lc_alph, up_alph, numbers)

if __name__ == "__main__":
    main()

    print(sys.version)
