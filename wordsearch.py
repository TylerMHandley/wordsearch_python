#!/usr/bin/python3
import random
import csv
import categories as cat


def insert_first_word(word):
    direction = random.randint(1,8)
    max = (size - len(word))
    #direction = 8
    offset = random.randint(0, max)
    offset2 = random.randint(0, max)
    start_location = random.randint(0, 9)
    locations = []
    if direction == 1:
        for i in range(0, len(word)):
            word_search[offset+i][start_location] = word[-i-1]
            locations.append((offset+i, start_location, 1, word[-i-1]))
    elif direction == 2:
        for i in range(0,len(word)):
            #print(size-i-1, start_location+i, i)
            word_search[(size-1-i)-offset][offset2+i] = word[i]
            locations.append(((size-1-i)-offset, offset2+i, 2, word[i]))
    elif direction == 3:
       for i in range(0,len(word)):
           word_search[start_location][offset+i] = word[i]
           locations.append((start_location,offset+i, 3, word[i]))
    elif direction == 4:
        for i in range(0,len(word)):
            word_search[offset+i][offset2+i] = word[i]
            locations.append((offset+i, offset2+i, 4, word[i]))
    elif direction == 5:
        for i in range(0, len(word)):
            #print (offset + i,start_location)
            word_search[offset + i][start_location] = word[i]
            locations.append((offset + i,start_location, 5,  word[i]))
    elif direction == 6:
        for i in range(0,len(word)):
            word_search[offset+i][size - 1 - offset2-i] = word[i]
            locations.append((offset+i,size - 1 - offset2-i, 6, word[i]))
    elif direction == 7:
        for i in range(0, len(word)):
            word_search[start_location][offset + i] = word[-i-1]
            locations.append((start_location,offset + i, 7, word[-i-1]))
    else:
        for i in range(0,len(word)):
            word_search[offset+i][offset2+i] = word[-i-1]
            locations.append((offset+i, offset2+i, 8, word[-i-1]))
    for i in range(0,size):
        #print(word_search[i])
        return locations
		
		
def insert_new_word(word, location):
    global words_added
    #Location is a list of tuples with the format (x,y,direction, letter)
    not_inserted = True
    for i in range(1, len(location)):
        if location[i][-1] in word:
            index = word.index(location[i][-1])
            #print("Word: {}, Index: {}".format(word, index))
            xIsPositive = True
            if location[i][0] < 0:
                xIsPositive = False
            yIsPositive = True
            if location[i][0] < 0:
                yIsPositive = False
            num_letter_after = len(word) - (index+1)+1
            direction = location[-2]
            while direction == location[-2]:
                direction = random.randint(1,8)
            count = 0
            while not_inserted and count < 8:
                toReplace = []
                canReplace = True
                try:
                    if direction == 1:
                        for ii in range(1,index+1):
                            if (location[i][0] + ii >= 0) != xIsPositive:
                                canReplace = False
                                break
                            if word_search[location[i][0]+ii][location[i][1]] == "*" \
                                    or word_search[location[i][0]+ii][location[i][1]] == word[index-ii]:
                                toReplace.append((location[i][0]+ii, location[i][1], 1,  word[index-ii]))
                            else:
                                canReplace = False
                        for ii in range(1,num_letter_after):
                            if (location[i][0] - ii >= 0) != xIsPositive:
                                canReplace = False
                                break
                            if word_search[location[i][0] - ii][location[i][1]] == "*" \
                                    or word_search[location[i][0] - ii][location[i][1]] == word[index + ii]:
                                toReplace.append((location[i][0] - ii, location[i][1], 1, word[index + ii]))
                            else:
                                canReplace = False
                    elif direction == 2:
                        for ii in range(1, index+1):
                            if (location[i][0]+ii >= 0) != xIsPositive or (location[i][1] - ii >= 0) != yIsPositive:
                                canReplace = False
                                break
                            if word_search[location[i][0]+ii][location[i][1] - ii] == "*" \
                                    or word_search[location[i][0]+ii][location[i][1] - ii] == word[index-ii]:
                                toReplace.append((location[i][0]+ii, location[i][1] - ii, 2, word[index-ii]))
                            else:
                                canReplace = False
                        for ii in range(1,num_letter_after):
                            if (location[i][0] - ii >= 0) != xIsPositive or (location[i][1] + ii >= 0) != yIsPositive:
                                canReplace = False
                                break
                            if word_search[location[i][0] - ii][location[i][1]+ii] == "*" \
                                    or word_search[location[i][0] - ii][location[i][1]+ii] == word[index + ii]:
                                toReplace.append((location[i][0] - ii, location[i][1]+ii, 2, word[index + ii]))
                            else:
                                canReplace = False
                    elif direction == 3:
                        for ii in range(1,index+1):
                            if (location[i][1] - ii >= 0) != yIsPositive:
                                canReplace = False
                                break
                            if word_search[location[i][0]][location[i][1]-ii] == "*" \
                                    or word_search[location[i][0]][location[i][1]-ii] == word[index-ii]:
                                toReplace.append((location[i][0], location[i][1]-ii, 3, word[index-ii]))
                            else:
                                canReplace = False
                        for ii in range(1,num_letter_after):
                            if (location[i][1] + ii >= 0) != yIsPositive:
                                canReplace = False
                                break
                            if word_search[location[i][0]][location[i][1] + ii] == "*" \
                                    or word_search[location[i][0]][location[i][1]+ ii] == word[index + ii]:
                                toReplace.append((location[i][0], location[i][1]+ ii, 3, word[index + ii]))
                            else:
                                canReplace = False
                    elif direction == 4:
                        for ii in range(1,index+1):
                            if (location[i][0] - ii >= 0) != xIsPositive or (location[i][1] - ii >= 0) != yIsPositive:
                                canReplace = False
                                break
                            if word_search[location[i][0]-ii][location[i][1]-ii] == "*" \
                                    or word_search[location[i][0]-ii][location[i][1]-ii] == word[index-ii]:
                                toReplace.append((location[i][0]-ii, location[i][1]-ii, 4, word[index-ii]) )
                            else:
                                canReplace = False
                        for ii in range(1,num_letter_after):
                            if (location[i][0]+ii >= 0) != xIsPositive or (location[i][1] + ii >= 0) != yIsPositive:
                                canReplace = False
                                break
                            if word_search[location[i][0] + ii][location[i][1]+ii] == "*" \
                                    or word_search[location[i][0] + ii][location[i][1]+ ii] == word[index + ii]:
                                toReplace.append((location[i][0] + ii, location[i][1]+ ii, 4, word[index + ii]))
                            else:
                                canReplace = False
                    elif direction == 5:
                        for ii in range(1,index+1):
                            if (location[i][0] - ii >= 0) != xIsPositive:
                                canReplace = False
                                break
                            if word_search[location[i][0]-ii][location[i][1]] == "*" \
                                    or word_search[location[i][0]-ii][location[i][1]] == word[index-ii]:
                                toReplace.append((location[i][0]-ii, location[i][1], 5, word[index-ii]) )
                            else:
                                canReplace = False
                        for ii in range(1,num_letter_after):
                            if (location[i][0]+ii >= 0) != xIsPositive:
                                canReplace = False
                                break
                            if word_search[location[i][0] + ii][location[i][1]] == "*" \
                                    or word_search[location[i][0] + ii][location[i][1]] == word[index + ii]:
                                toReplace.append((location[i][0] + ii, location[i][1], 5, word[index + ii]))
                            else:
                                canReplace = False
                    elif direction == 6:
                        for ii in range(1,index+1):
                            if (location[i][0] - ii >= 0) != xIsPositive or (location[i][1] + ii >= 0) != yIsPositive:
                                canReplace = False
                                break
                            if word_search[location[i][0]-ii][location[i][1] + ii] == "*" \
                                    or word_search[location[i][0]-ii][location[i][1] + ii] == word[index-ii]:
                                toReplace.append((location[i][0]-ii, location[i][1]+ii, 6, word[index-ii]) )
                            else:
                                canReplace = False
                        for ii in range(1,num_letter_after):
                            if (location[i][0]+ii >= 0) != xIsPositive or (location[i][1] - ii >= 0) != yIsPositive:
                                canReplace = False
                                break
                            if word_search[location[i][0] + ii][location[i][1] - ii] == "*" \
                                    or word_search[location[i][0] + ii][location[i][1] - ii] == word[index + ii]:
                                toReplace.append((location[i][0] + ii, location[i][1]-ii, 6, word[index + ii]))
                            else:
                                canReplace = False
                    elif direction == 7:
                        for ii in range(1,index+1):
                            if (location[i][1] + ii >= 0) != yIsPositive:
                                canReplace = False
                                break
                            if word_search[location[i][0]][location[i][1]+ii] == "*" \
                                    or word_search[location[i][0]][location[i][1]+ii] == word[index-ii]:
                                toReplace.append((location[i][0], location[i][1]+ii, 7, word[index-ii]))
                            else:
                                canReplace = False
                        for ii in range(1,num_letter_after):
                            if (location[i][1] - ii >= 0) != yIsPositive:
                                canReplace = False
                                break
                            if word_search[location[i][0]][location[i][1] - ii] == "*" \
                                    or word_search[location[i][0]][location[i][1]- ii] == word[index + ii]:
                                toReplace.append((location[i][0], location[i][1]- ii, 7, word[index + ii]))
                            else:
                                canReplace = False
                    else:
                        for ii in range(1,index+1):
                            if (location[i][0]+ii >= 0) != xIsPositive or (location[i][1] +ii >= 0) != yIsPositive:
                                canReplace = False
                                break
                            if word_search[location[i][0]+ii][location[i][1]+ii] == "*" \
                                    or word_search[location[i][0]+ii][location[i][1]+ii] == word[index-ii]:
                                toReplace.append((location[i][0]+ii, location[i][1]+ii, 8, word[index-ii]) )
                            else:
                                canReplace = False
                        for ii in range(1,num_letter_after):
                            if (location[i][0]-ii >= 0) != xIsPositive or (location[i][1] - ii >= 0) != yIsPositive:
                                canReplace = False
                                break
                            if word_search[location[i][0] - ii][location[i][1]-ii] == "*" \
                                    or word_search[location[i][0] - ii][location[i][1]- ii] == word[index + ii]:
                                toReplace.append((location[i][0] - ii, location[i][1]- ii, 8, word[index + ii]))
                            else:
                                canReplace = False
                    if canReplace:
                        words_added.append(word)
                        #print(toReplace)
                        for p in range(0,len(toReplace)):
                            word_search[toReplace[p][0]][toReplace[p][1]]= toReplace[p][3]
                            location.append(toReplace[p])
                            not_inserted = False
                    else:
                        count+=1
                        direction += 1
                        if direction >8:
                            direction = 1
                except IndexError:
                    count += 1
                    direction += 1
                    if direction > 8:
                        direction = 1
            if not_inserted == False:
                return location
    #Here is where a word will go to be added if it could not fit at any location
    for row in range(1,size):
        for col in range(1, size):
            count = 0
            direction = random.randint(1,8)
            while not_inserted and count < 8:
                toReplace = []
                canReplace = True
                if direction == 1:
                    for ii in range(0, len(word)):
                        if 0 <= row - ii < size:
                            if word_search[row - ii][col] == "*" \
                                    or word_search[row - ii][col] == word[ii]:
                                toReplace.append((row - ii, col, 1, word[ii]))
                        else:
                            canReplace = False
                            break
                elif direction == 2:
                    for ii in range(0, len(word)):
                        if 0 <= row - ii < size and 0<= col + ii < size:
                            if word_search[row - ii][col + ii] == "*" \
                                    or word_search[row - ii][col + ii] == word[ii]:
                                toReplace.append((row - ii, col + ii, 2, word[ii]))
                        else:
                            canReplace = False
                            break
                elif direction == 3:
                    for ii in range(0, len(word)):
                        if 0 <= col + ii < size:
                            if word_search[row][col + ii] == "*" \
                                    or word_search[row][col + ii] == word[ii]:
                                toReplace.append((row, col + ii, 3, word[ii]))
                        else:
                            canReplace = False
                            break
                elif direction == 4:
                    for ii in range(0, len(word)):
                        if 0 <= row + ii < size and 0 <= col + ii < size:
                            if word_search[row + ii][col + ii] == "*" \
                                    or word_search[row + ii][col + ii] == word[ii]:
                                toReplace.append((row + ii, col + ii, 4, word[ii]))
                        else:
                            canReplace = False
                            break
                elif direction == 5:
                    for ii in range(0, len(word)):
                        if 0 <= row + ii < size :
                            if word_search[row + ii][col] == "*" \
                                    or word_search[row + ii][col] == word[ii]:
                                toReplace.append((row + ii, col, 5, word[ii]))
                        else:
                            canReplace = False
                            break
                elif direction == 6:
                    for ii in range(0, len(word)):
                        if 0 <= row + ii < size and 0 <= col - ii < size:
                            if word_search[row + ii][col - ii] == "*" \
                                    or word_search[row + ii][col - ii] == word[ii]:
                                toReplace.append((row - ii, col - ii, 6, word[ii]))
                        else:
                            canReplace = False
                            break
                elif direction == 7:
                    for ii in range(0, len(word)):
                        if 0 <= row - ii < size and 0 <= col + ii < size:
                            if word_search[row][col - ii] == "*" \
                                    or word_search[row][col - ii] == word[ii]:
                                toReplace.append((row, col - ii, 7, word[ii]))
                        else:
                            canReplace = False
                            break
                else:
                    for ii in range(0, len(word)):
                        if 0 <= row - ii < size and 0 <= col + ii < size:
                            if word_search[row - ii][col - ii] == "*" \
                                    or word_search[row - ii][col - ii] == word[ii]:
                                toReplace.append((row - ii, col - ii, 8, word[ii]))
                        else:
                            canReplace = False
                            break
                if canReplace:
                    words_added.append(word)
                    for p in range(0, len(toReplace)):
                        word_search[toReplace[p][0]][toReplace[p][1]] = toReplace[p][3]
                        location.append(toReplace[p])
                        not_inserted = False
                else:
                    count += 1
                    direction += 1
                    if direction > 8:
                        direction = 1
            if not_inserted == False:
                return location
    return location
	
def prepare_added_list(added_list):
    chunked_list = [added_list[i::3] for i in range(0,3)]
    return zip(chunked_list[0], chunked_list[1], chunked_list[2])


def write_wordsearch(file_name, word_list, isAnswers=False):
    if isAnswers:
        file_name = file_name + '_Answers.txt'
    else:
        file_name = file_name + '.txt'
    with open(file_name, 'w+') as file: 
        for row in word_search:
            file.writelines("\t")
            for letter in row:
                file.writelines("{} ".format(letter))
            file.writelines("\n")
        file.writelines("\n")
        if not isAnswers:
            col_writer = csv.writer(file, delimiter='\t')
            col_writer.writerows(word_list)	


category = ""
# Getting the list of categories from the other file
keys = list(cat.categories.keys())
# Forcing the user to select an input from the list
while category not in keys:
    category = input("{}\nChoose a category from above: ".format(keys)).lower()
# Collecting the list of words from the file
word_list = cat.categories[category]
# Getting the 'hyper parameters'
size = ''
while not size.isdigit():
    size = input("Input a size for your Word Search: ")
size = int(size)
file_name = 'wordsearches/' + input("Enter a name for your Word Search: ")
# Generating the initial wordsearch filled with *
word_search = [["*" for val in range(0,size)] for val1 in range(0, size)]

# Sorting the wordlist in reverse order
word_list.sort(key=lambda x: len(x), reverse=True)
words_added = [word_list[0]]
location = insert_first_word(word_list[0])

print("first word is {}".format(word_list[0]))

# Going to try to add every word
for x in range(1,len(word_list)):
    word = random.choice(word_list)
    location = insert_new_word(word, location)
    word_list.remove(word)
# Preparing the list of words at the bottom
words_added.sort(key=lambda x: len(x))
bottom_list = prepare_added_list(words_added)
# Writing the answer sheet
write_wordsearch(file_name, bottom_list, True)
#Replacing all the * characters with random letters
for y in range(0,size):
    for x in range(0,size):
       if word_search[y][x] == '*':
           word_search[y][x] = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
# Finally writing the actual word search
write_wordsearch(file_name, bottom_list)


#file.close()