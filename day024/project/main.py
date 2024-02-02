#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

def get_template():
    """
    Returns the invitation template as a string
    """
    with open("Input/Letters/starting_letter.txt") as starting_letter:
        return starting_letter.read()


def get_names():
    """
    Returns a list of names as a list of strings
    """
    with open("Input/Names/invited_names.txt") as invited_names:
        return invited_names.readlines()


# Start
template = get_template()
names = get_names()

for name in names:
    stripped_name = name.strip()
    invitation = template.replace("[name]", stripped_name)
    with open(f"Output/ReadyToSend/{stripped_name}.txt", mode="w") as output_file:
        output_file.write(invitation)
