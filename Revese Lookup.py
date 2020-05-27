#performs the action of mapping to provided value
def reverseLookup(dictionary, value): 
    keys = []
    for key in dictionary:
        if dictionary[key] == value: 
            keys.append(key)
  
    #returns final list of values
    return keys 

#main function that uses reverseLookup
def main():
    #a dictionary mapping numbers to their most specific number type (integer, whole number, irrational number, etc)
    number_types = {"1" : "whole number", "-3" : "integer", "pi" : "irrational number", "2" : "whole number", "10" : "whole number", "square root of 2" : "irrational number"}
    
    #the print statements below demonstrate the three cases where the are 0, 1, or 2 returned values
   
    # 3 return values
    print("Examples of whole numbers: ", reverseLookup(number_types, "whole number"))
    #2 return values
    print("Examples of irrational numbers: ", reverseLookup(number_types, "irrational number"))
    #1 return value
    print("Example of integer is: ", reverseLookup(number_types, "integer"))
    #0 return values - print statement will not show an example because none exist in the dictionary
    print("An example of a complex number is: ", reverseLookup(number_types, "complex number"))

main()