print("===============================" )   
print("   WELCOME TO SUDUKO CHECKER   ")
print("===============================")
def load_puzzle(files):
    global line                 # global line refferenced here so i can use 
                                # it in as input in the other functions.
                                
    line=files.read()
    line = list(line[0:len(line):2])     #this step removes "," from list.  
    print('sudoku_as_a_list=', line,"\n")



def print_puzzle(puzzle):
    global y
    print("Here is your solved sudoku file.\n")
    y = (' '.join(puzzle)) # this reverts the single list to a string
    print(y[0:6],"|",y[6:12],"|",y[12:18])
    print(y[18:24],"|",y[24:30],"|",y[30:36])
    print(y[36:42],"|",y[42:48],"|",y[48:54])
    print("------------------------")
    print(y[54:60],"|",y[60:66],"|",y[66:72])
    print(y[72:78],"|",y[78:84],"|",y[84:90])
    print(y[90:96],"|",y[96:102],"|",y[102:108])
    print("------------------------")
    print(y[108:114],"|",y[114:120],"|",y[120:126])
    print(y[126:132],"|",y[132:138],"|",y[138:144])
    print(y[144:150],"|",y[150:156],"|",y[156:162],"\n")    


# The function below takes input list, sorts it from smallest to 
# largest element, and then checks if the list is equal to 
# [1,2,3,4,5,6,7,8,9] which is what we want. If it isnt equal, you know
# there are duplicates, greater than or less than 9 elements, or integers
# outside of (0,9).

def check_numbers(x):
    y = ["1", "2", "3", "4" , "5", "6", "7", "8", "9"]
    x.sort()
    if x == y:
        return True
    else:
        return False



#Function to check rows.

def check_rows(row):
    row1 = line[0:9]
    row2 = line[9:18]
    row3 = line[18:27]
    row4 = line[27:36]
    row5 = line[36:45]
    row6 = line[45:54]
    row7 = line[54:63]
    row8 = line[63:72]
    row9 = line[72:81]
    if check_numbers(row1) != True:
        return "Row 1 is invalid,"
    elif check_numbers(row2) != True:
        return "Row 2 is invalid,"
    elif check_numbers(row3) != True:
        return "Row 3 is invalid,"
    elif check_numbers(row4) != True:
        return "Row 4 is invalid,"
    elif check_numbers(row5) != True:
        return "Row 5 is invalid,"
    elif check_numbers(row6) != True:
        return "Row 6 is invalid,"
    elif check_numbers(row7) != True:
        return "Row 7 is invalid,"
    elif check_numbers(row8) != True:
        return "Row 8 is invalid,"
    elif check_numbers(row9) != True:
        return "Row 9 is invalid,"
    else:
        return "-1"
    
    

    
#Function to check columns.

def check_columns(column):
    column1 = line[0:81:9]
    column2 = line[1:81:9]
    column3 = line[2:81:9]
    column4 = line[3:81:9]
    column5 = line[4:81:9]
    column6 = line[5:81:9]
    column7 = line[6:81:9]
    column8 = line[7:81:9]
    column9 = line[8:81:9]
    if check_rows(line)!="-1":
        return ""    
    elif check_numbers(column1) != True:
        return "Column 1 is invalid,"
    elif check_numbers(column2) != True:
        return "Column 2 is invalid,"
    elif check_numbers(column3) != True:
        return "Column 3 is invalid,"
    elif check_numbers(column4) != True:
        return "Column 4 is invalid,"
    elif check_numbers(column5) != True:
        return "Column 5 is invalid,"
    elif check_numbers(column6) != True:
        return "Column 6 is invalid,"
    elif check_numbers(column7) != True:
        return "Column 7 is invalid,"
    elif check_numbers(column8) != True:
        return "Column 8 is invalid,"
    elif check_numbers(column9) != True:
        return "Column 9 is invalid,"
    else:
        return "-1"
    
    
    
#function to check subgrids.

def check_subgrids(subgrid):
    subgrid1 = line[0:3]+ line[9:12]+line[18:21]
    subgrid2 = line[3:6]+ line[12:15]+line[21:24]
    subgrid3 = line[6:9]+ line[15:18] + line[24:27]
    subgrid4 = line[27:30]+ line[36:39]+line[45:48]
    subgrid5 = line[30:33]+ line[39:42]+line[48:51]
    subgrid6 = line[33:36]+ line[42:45] + line[51:54]
    subgrid7 = line[54:57]+ line[63:66]+line[72:75]
    subgrid8 = line[57:60]+ line[66:69]+line[75:78]
    subgrid9 = line[60:63]+ line[69:72]+line[78:81]
    if check_columns(line)!="-1":
        return ""    
    elif check_numbers(subgrid1) != True:
        return "Subgrid 1 is invalid,"
    elif check_numbers(subgrid2) != True:
        return "Subgrid 2 is invalid,"
    elif check_numbers(subgrid3) != True:
        return "Subgrid 3 is invalid,"
    elif check_numbers(subgrid4) != True:
        return "Subgrid 4 is invalid,"
    elif check_numbers(subgrid5) != True:
        return "Subgrid 5 is invalid,"
    elif check_numbers(subgrid6) != True:
        return "Subgrid 6 is invalid,"
    elif check_numbers(subgrid7) != True:
        return "Subgrid 7 is invalid,"
    elif check_numbers(subgrid8) != True:
        return "Subgrid 8 is invalid,"
    elif check_numbers(subgrid9) != True:
        return "Subgrid 9 is invalid,"  
    else:
        return "-1"
    

#This function is used to return one value, either an invalid row,column,subgrid 
# or a valid solution. 

def result():
    if check_rows(line)!="-1" :
        return check_rows(line)+" therefore the puzzle solution is invalid."
    elif check_columns(line) != "-1":
        return check_columns(line)+" therefore the puzzle solution is invalid."
    elif check_subgrids(line) != "-1":
        return check_subgrids(line)+" therefore the puzzle solution is invalid."
    else:
        return "Puzzle solution is valid."



x = input("Select a csv file containing a sloved suduko puzzle:")
file = open(x,'r') # User file input.
print()
load_puzzle(file)    # Converts input into list. 
print_puzzle(line)   # Uses list to print sodoku.




#This function takes the file you used for the puzzle, slices it to remove .csv
# then it concatenates the slice with -result.txt. Then the result of the test
# is written to the file the new txt file if it exists.

def write_file():
    x = input("Input the puzzle file you used to add output to new file:")
    x = x[0:len(x)-4]
    x = x+"-result.txt"
    file = open(x,'w')
    print("Output written  to: "+'"'+ str(x) + '"')
    file.write(result())
    





print(check_rows(line))
print(check_columns(line))
print(check_subgrids(line))
print(result())
write_file()
file.close()

print("Goodbye, thank you for using my program.")