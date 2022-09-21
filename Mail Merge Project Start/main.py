#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

people_f = open("./Input/Names/invited_names.txt")
p = people_f.readlines()
person = []
for people in p:
    person.append(people.split('\n')[0])
people_f.close()

letter = open("./Input/Letters/starting_letter.txt")
line = letter.readlines()

for name in person:
    new_letter = open(f"./Output/ReadyToSend/{name}.txt", 'w')
    for l in line:
        new_letter.write(l.replace("[name]",name))
    new_letter.close()

print(person)