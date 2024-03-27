# A simple program to count each character in a text file.
from os import strerror

# Store the number of each characters in  dictionary with a starting value of 0
try:
    source_file = input("Enter a file name to analyse:")
    src = open(source_file, "rt")
    results_file = open(f"{source_file}.hist", "w")   
# Set up a dictionary to count and report each character
    alphabet = [chr(i) for i in range(97, 123)]
    occurances = dict.fromkeys(alphabet,0)
    content = src.read().lower().strip()
    for c in content:
        occurances[c] += 1
    for key in dict(sorted(occurances.items(), key=lambda item: item[1], reverse = True)):
        if occurances[key] > 0:
           x = f"{key} -> {occurances[key]}\n"
           results_file.write(x)
                
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

finally:
    src.close()
    results_file.close()

