#wpm tester
import time
import random
import sys
import keyboard
#

print("Start typing to start the timer.")


class wpmtester:
    #print out 10 random words from the words.txt file
    with open("words.txt") as words_file:
        words_list = [line.strip() for line in words_file]
    random.shuffle(words_list)
    hovno = words_list[:10]
    print(*hovno, sep= " ")
    output_length = len(hovno)
    print(output_length)



    #user input
    def test():
        while True:
            user_input = input("")

            if len(user_input) == 10:
                print("Well done")
                break
            


