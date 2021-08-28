#wpm tester
#imports
from threading import Timer
import random
import sys
import keyboard
#




class wpmtester:
    #word amount
    word_amount = int(input("How many words would you like to type?    "))

    print(">>> Start typing to start the timer.")

    #print out random words from the words.txt file
    with open("words.txt") as words_file:
        words_list = [line.strip() for line in words_file]
    random.shuffle(words_list)
    hovno = words_list[:word_amount]
    print(*hovno, sep= " ")
    output_length = len(hovno)
    print(output_length)

    user_input = input("")

  








            


