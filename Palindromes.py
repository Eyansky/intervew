"""A palindrome is a word or phrase that is spelt the same way forward and backward
 (disregarding whitespace, punctuation and capitalization). Examples include madam, level, nurses run"""

entry = []
def palindromes(x):
        #remove whitespace 
        word = x.replace(" ", "")
        #reverse the words 
        rewind = reversed(word)
            
        #check if it is a Palindrome
        if list(word) == list(rewind):
            return "It is a Palindrome!!"
        else:
            return "It is not a Palindrome!!"

while True:
    #giving exit instructions
    print("To exit type 'quit'")
    #Get user input
    phrase = input("Enter name to be tested: ")
    #add the input into the entry list
    entry.append(phrase)
    print(palindromes(phrase))

    if phrase == "quit":
        break
    else:
        for x in entry:
            print("Entries made: " + x)
