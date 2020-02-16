#Project Euler Question 17

#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
#The use of "and" when writing out numbers is in compliance with British usage.

import inflect

p = inflect.engine()

def numword(x):
    wordlist = []
    for x in range(1,(x+1)):
        words = p.number_to_words(x)
        words = words.replace(" ", "")
        words = words.replace("-", "")
        wordlist.append(words)
    wordlist = "".join(wordlist)
    return len(wordlist)



print (numword(1000), "is the number of letters that would be used")