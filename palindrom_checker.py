# A program to check if a piece of text is a palindrome

usr_chosen_word = str(input("Enter a word and I will reveal if it's a palindrom: "))
usr_chosen_word_formatted = usr_chosen_word.lower().replace(" ","")
usr_chosen_word_backward = usr_chosen_word_formatted[::-1]
print(usr_chosen_word_backward)
if usr_chosen_word_backward == usr_chosen_word_formatted:
    print("Yes, that is a palindrome")
else:
    print("Hard luck, not a palindrome")

