#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Day24-Directories/Mail_Merge_Project_Start/Input/Letters/starting_letter.txt", "r") as file:
    letter_str = file.read()

name_list = []
with open("Day24-Directories/Mail_Merge_Project_Start/Input/Names/invited_names.txt", "r") as file:
    for name in file:
    #    if name[-1] == '\n':
    #        name = name[:-1]
        name = name.strip('\n')
        name_list.append(name)
        
for name in name_list:
    with open(f"Day24-Directories/Mail_Merge_Project_Start/Output/ReadyToSend/{name}_invite.txt", "w") as file:
        text_str = letter_str.replace('[name]', name)
        file.write(text_str)