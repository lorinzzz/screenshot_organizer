import os
from pathlib import Path

file_list = []
for i in os.listdir():
    # keep only files in list that are image files 
    file_extension = os.path.splitext(i)
    # common image file formats 
    if file_extension[1] == ".jpg" or file_extension[1] == ".jpeg" or file_extension[1] == ".gif" or file_extension[1] == ".png" or file_extension[1] == ".bmp":
        file_list.append(i)

# no need to build a list of longest common substrings bedcause listdir() will read in all files alphabetically, each game will produce a screenshot with the same prefix in the file name

tok_str = ""
sub_str = ""
folder_count = 0
for x in file_list:

    # check to see if file name prefix matches the sub_str
    if sub_str == x[0:len(sub_str)] and len(sub_str) > 0:
        Path(x).rename(sub_str + "/" + x)

    # if it does not, it means we are the beginning of the list, or the file names belong to another game
    # create a new sub_str
    else:
        # read until first whitespace or '_', and get that sub_str before
        for y in x:
            if y == ' ' or y == '_':
                tok_str = x.split(y)
                sub_str = tok_str[0]
                folder_count += 1
                #print("New sub_str: ", sub_str)
                break
         # create folder and move file to it
        os.mkdir(sub_str)
        Path(x).rename(sub_str + "/" + x)
    

print("Organized", len(file_list), "into", folder_count, "folders!")
