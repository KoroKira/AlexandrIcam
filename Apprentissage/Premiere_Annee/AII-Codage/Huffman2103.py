# ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ #
#                                                                             #
#  ▧     ▧  ▧     ▧   ▧▧▧▧▧▧   ▧▧▧▧▧▧  ▧▧   ▧▧   ▧▧▧▧▧   ▧▧    ▧              # 
#  ▧     ▧  ▧     ▧  ▧        ▧        ▧ ▧ ▧ ▧  ▧     ▧  ▧ ▧   ▧              #
#  ▧▧▧▧▧▧▧  ▧     ▧  ▧▧▧▧▧▧▧  ▧▧▧▧▧▧▧  ▧  ▧  ▧  ▧▧▧▧▧▧▧  ▧  ▧  ▧              #
#  ▧     ▧  ▧     ▧  ▧        ▧        ▧     ▧  ▧     ▧  ▧   ▧ ▧              #  
#  ▧     ▧   ▧▧▧▧▧   ▧        ▧        ▧     ▧  ▧     ▧  ▧    ▧▧              #
#                                                                             #
#   ▧▧▧▧▧▧   ▧▧▧▧▧   ▧▧▧▧▧▧   ▧▧▧▧▧▧▧  ▧▧    ▧   ▧▧▧▧▧▧                       # 
#  ▧        ▧     ▧  ▧     ▧     ▧     ▧ ▧   ▧  ▧                             #
#  ▧        ▧     ▧  ▧     ▧     ▧     ▧  ▧  ▧  ▧   ▧▧▧                       #
#  ▧        ▧     ▧  ▧     ▧     ▧     ▧   ▧ ▧  ▧     ▧                       # 
#   ▧▧▧▧▧▧   ▧▧▧▧▧   ▧▧▧▧▧▧   ▧▧▧▧▧▧▧  ▧    ▧▧   ▧▧▧▧▧▧                       #
#                                                                             #
# ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ #
#
import numpy as np
#
# ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ #
#
"""
▌ Function: fcn_find_index
    To find an element within a list and return its row-index.
▼ Inputs:
    column: int - column of some_list to look through.
    some_list: nx2 numpy.ndarray of strings - holds strings and weights.
    some_str: string to look up in some_list.
▼ Outputs:
    index: the row-index of some_str in some_list.
▲ n = number of different string elements in the list.
"""
#
def fcn_find_index( column_to_search, some_list, str_to_find ):
    #
    # Initialize:
    index = -1 # variable to return: -1 -> str_to_find is not found
    flag = 0 # indicates if str_to_find is found: 0 / 1 -> not found / found
    #
    list_length = len(some_list) # number of rows of some_list
    #
    # Loop until str_to_find is found: flag = 1
    while flag == 0 :
        index = index + 1 # increment index
        if index == list_length: # end of some_list is reached
            flag = 1 # set to 1 to exit while loop
            index = -1 # set to -1 to indicate str_to_find is not found
        else: # end of some_list is not reached
            # need to differenciate between column 0 and column 1
            # column 1: contains strings
            # column 2: contains strings that need to be converted to int
            if column_to_search == 0:
                v = some_list[index,column_to_search]
            elif column_to_search == 1:
                v = int(some_list[index,column_to_search])
            if v == str_to_find:
                flag = 1 # str_to_find is found!
    #
    return index
#
# ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ #
#
"""
▌ Function: fcn_update_list_and_key
    To combine the first two elements in some_list and insert the new combined
    string at the correct row. 
    To update old_key.
▼ Inputs:
    some_list: nx2 numpy.ndarray of strings - holds strings and weights.
    old_key: nx2 numpy.ndarray of strings - holds characters and keys.
▼ Outputs:
    new_list: nx2 numpy.ndarray of strings - the updated version of some_list.
    new_key: nx2 numpy.ndarray of strings - the updated version of some_key.
▲ n = number of different string elements in the list.
"""
#
def fcn_update_list_and_key( some_list, old_key ):
    #
    # Initialize: start with new key equal to old key
    new_key = old_key
    #
    # The first two elements in the first column (0) of some_list
    element_0 = some_list[0,0]
    element_1 = some_list[1,0]
    #
    # For each element of element_0 find its index then append a '0' in new_key
    for j in range(len(element_0)):
        # Find index of element
        index_old_key = fcn_find_index( 0, old_key, element_0[j] )
        # Append with a '0'
        new_key[index_old_key,1] = new_key[index_old_key,1] + '0'
    #
    # For each element of element_1 find its index then append a '1' in new_key
    for j in range(len(element_1)):
        # Find index of element
        index_old_key = fcn_find_index( 0, old_key, element_1[j] )
        # Append with a '1'
        new_key[index_old_key,1] = new_key[index_old_key,1] + '1'
    #
    # Combine element_0 and element_1 into one string
    str_combine = element_0 + element_1;
    # Add up their weights
    weight_combine =  int(some_list[0,1]) + int(some_list[1,1])
    # Create a new element, to be placed in new_list
    element = (str_combine, str(weight_combine))
    #
    # Delete element_0 and element_1 from some_list
    new_list = np.delete(some_list,[0,1],0)
    #
    # Find where to place the new string (in new_list) based on its weight
    index = fcn_find_index( 1, new_list, weight_combine )
    if index == -1: # if the weight is the larger than the rest
        index = len(new_list)
    #
    # Place the element in new_list at the correct row
    new_list = np.insert(new_list, index, element, axis=0)
    #
    return new_list, new_key
#
# ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ ▧ #
#
"""
▌ Function: fcn_compress
    To compress a string using its corresponding Huffman key.
▼ Inputs:
    text: string - holds the chain of characters to compress.
    key: nx2 numpy.ndarray of strings - holds characters and keys.
▼ Outputs:
    text_compressed: nx2 numpy.n
▲ n = number of different characters the string has.
"""
#
def fcn_compress( text, key ):
    # 
    # Initialize: start with an empty string
    text_compressed = ''
    # Loop over the charcters in the text
    for i in range(len(text)):
        #
        # Find the index (row) of the ith character in key
        p = fcn_find_index( 0, key, text[i] )
        # Append the compressed text
        text_compressed = text_compressed + key[p,1]
    #
    return text_compressed

# =========================================================================== #

# Read the text to compress from a file
text_path = "huffman_text.txt"
with open(text_path) as f:
    text_list = f.readlines()
text = ''
for i in range(len(text_list)):
    text = text + text_list[i];

# Read the alphabet from a file
alphabet_path = "huffman_alphabet.txt"
with open(alphabet_path) as g:
    alphabet_list = g.readlines()
alphabet = alphabet_list[0];

# Length of text:
text_length = len(alphabet)

# List to store the characters available in text and their count:
list_charc_count = [] # empty

# Loop over the length of text:
for i in range(text_length):
    #
    charac = alphabet[i] # ith character in text
    count = text.count(alphabet[i]) # occurence of ith character
    #
    if count > 0: # if this character occurs in text
        list_charc_count.append( (charac, count) ) # append the list

# Sort the list of available characters in ascending order of occurence:       
sorted_list = sorted(list_charc_count, key=lambda student: student[1])

# Convert list to numpy array (of characters):
sorted_list = np.array(sorted_list)

#print( sorted_list )

key = []
for i in range(len(sorted_list)):
    key.append([sorted_list[i,0],sorted_list[i,1]])
key = np.array(key)
key[:,1] = ''
key = key.astype('<U11')

for i in range(len(sorted_list)-1):
    sorted_list, key = fcn_update_list_and_key( sorted_list, key )

for i in range(len(key)):
    key[i,1] = key[i,1][::-1]
    
text_compressed = fcn_compress( text, key )

#open text file
text_file = open("Huffman_compressed.txt", "w")
#write string to file
text_file.write(text_compressed)
#close file
text_file.close()

"""
print('.')
print(text)
print('.')
print(key)
print('.')
print(text_compressed)
print('.')
"""