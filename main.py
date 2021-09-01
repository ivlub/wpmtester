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
#start timer
start_time = time.time()
#userinput
user_input = input("")
#stop timer
end_time = time.time()
#calculate total time
total_time = end_time-start_time
#add user input to a list
user_list.append(user_input)


#time elapsed
print(">>> Time elapsed:", total_time, "seconds")
#calculate and print wpm
wpm = len(user_input)*60/(5*total_time)
print(">>> Typing speed:", wpm, "wpm")

#lists with no [] or ,
generated_words_no_space = ""
for word in generated_list:
    generated_words_no_space += word + " "


user_words_no_space =""
for y in user_list:
    user_words_no_space += y + " "

#calculate accuracy
acc = 0
for i, c in enumerate(generated_words_no_space):
    try:
        if user_words_no_space[i] == c:
            acc += 1
    except:
        pass

accuracy = acc*100/len(generated_words_no_space)


accuracy = acc*100/len(generated_words_no_space)
print(">>> Accuracy:", accuracy, "%")











  








            


