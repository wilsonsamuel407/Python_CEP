# A program that reads 9 rows of the Sudoku and checks if the puzzle is solved
# Input data was provided as a string in the following format.
# Assume only characters 1-9 were accepted on input
input_data = """
295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672
"""
#input_list = list(input_data.replace("\n","").strip(","))
input_list = input_data.replace("\n"," ").strip(",").split()
print(input_list)
# Check the rows
rows =list("".join(input_list))
# If duplicates the set will remove them and len < 9
for x in range(0,73,9):
    if(len(set(rows[x:x+9]))) != 9:
        print("Hard luck, there is an error in the Sodoku")
else:
    print("Well done, the rows are correct")

# Column check (order list by column and use same method)
col = []
a , b = 0,  73
while len(col) < 81:
    for x in range(a,b,9):
        col.append(rows[x])
    a += 1
    b += 1
# Then apply same method as the row check
for x in range(0,73,9):
    if(len(set(col[x:x+9]))) != 9:
        print("Hard luck, there is an error in the Sodoku")
else:
    print("Well done, the columns are correct")

# Square check (order list by column and use same method)
grid = []
a, b = 0, 3
while len(grid) < 27:
    for i in input_list:
        grid.append(i[a:b])
    a += 3
    b += 3
# Extra step needed to flatten the list out
subsquares = list("".join(grid))
# Then apply same method as the row check
for x in range(0,73,9):
    if(len(set(subsquares[x:x+9]))) != 9:
        print("Hard luck, there is an error in the Sodoku")
else:
    print("Well done, the sub squares are correct")



