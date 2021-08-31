#wpm tester
#imports
from threading import Timer
import random
import sys
import keyboard
import time





#word amount
word_amount = int(input("How many words would you like to type?    "))

print("Okay, going to type", word_amount, "words.")
print(">>> Start typing to start the timer.")
#print out random words from the words.txt file
with open("words.txt") as words_file:
    words_list = [line.strip() for line in words_file]
random.shuffle(words_list)
hovno = words_list[:word_amount]
print(*hovno, sep= " ")
sracka = hovno[0][:1]
output_length = len(hovno)



#user input
keyboard.wait(sracka)
start_time = time.time()
user_input = input("")
end_time = time.time()
print("time elapsed =", end_time - start_time, "seconds")





  








            


