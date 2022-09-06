#Function removes all exclamation marks from a given string

#Function removes exclimation mark
def remove_exclamation_marks(s):
    s2 = s.replace("!","")
    return s2
    
new_string = remove_exclamation_marks("Hello!")

print(new_string)
 