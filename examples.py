   #function to repplace characters in astring
def replace_in(phrase) :
    word=" "
    for letter in phrase :
        if letter.lower () in "aeiou" :
            word = word+"G"
        else:
         word = word + letter
    return word           
print(replace_in(input("Enter a phrase : ")))   