#function that will translate the word 
def pigLatin(word):
    vowels = "aeiou"
    #check to see if the word begins with a vowel
    if word[0] in vowels: 
        word += 'way'
        return word 
    else:
        #check to see where the first vowel is
        for i in range(len(word)): 
            if word[i] in vowels:
                word = word[i:] + word[:i] + "ay"
                return word 
#apply the input to the pigLatin function
def main():
    english = input("Enter the word you would like to translate into Pig Latin: ")
    print("Your input in Pig Latin is %s" % pigLatin(english))

main()



