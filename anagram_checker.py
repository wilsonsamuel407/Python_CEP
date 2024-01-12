# A simple program to check if two words are anagrams
print("Welcome to anagram checker, you will be asked to enter two words to check")
while True:
    word_1 = str(input("Enter first word: ")).lower().replace(" ","")
    if len(word_1) == 0:
        print("Enter a word with more than zero letters")
    else:
        break

while True:
    word_2 = str(input("Enter second word: ")).lower().replace(" ","")
    if len(word_2) == 0:
        print("Enter a word with more than zero letters")
    else:
        break

if len(word_1) != len(word_2):
    print("Sorry, It's not an anagram")

else:
    for n in word_1:
        if n not in word_2:
            print("Sorry, It's not an anagram")
            break
        else:
            continue
    else:
        print("Congrats! That is an anagram")
