#: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

def main():
    with open('./Input/Names/invited_names.txt') as names:
        all_names = names.readlines()
        all_names = [name.rstrip() for name in all_names]
    with open('./Input/Letters/starting_letter.txt') as letter:
        full_letter = letter.readlines()
        first_line = full_letter[0]
    for name in all_names:
        with open(f'./Output/ReadyToSend/{name}.txt', 'w') as file:
            file.write(first_line.replace('[name]', name ))
            for line in full_letter[1:]:
                file.write(line)
if __name__ == '__main__':
    main()