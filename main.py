#wpm tester
#imports
import random
import keyboard
import time




print("Welcome to wpm-tester! Test your typing speed and accuracy!")
#word amount
word_amount = int(input("How many words would you like to type?    "))

print("Okay, going to type", word_amount, "words.")
print(">>> Start typing to start the timer. Hit enter at the end to stop the timer.")
#print out random words from the words.txt file
with open("words.txt") as words_file:
    words_list = [line.strip() for line in words_file]
random.shuffle(words_list)
generated_list = words_list[:word_amount]
print(*generated_list, sep= " ")
first_character = generated_list[0][:1]
output_length = len(generated_list)



#user input
user_list = []
keyboard.wait(first_character)
start_time = time.time()
user_input = input("")
end_time = time.time()
total_time = end_time-start_time
user_list.append(user_input)

#calculation
print(">>> Time elapsed:", total_time, "seconds")
wpm = len(user_input)*60/(5*total_time)
print(">>> Yout typing speed:", wpm, "wpm")









  








            


