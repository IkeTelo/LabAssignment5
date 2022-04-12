

'''LAYMAN'S TERMS'''
"""
The program is trying to translate a sentence captured as user input.
We first read in the text file textese.txt.
Then from text file, we create a list from each line.
Then we create a dictionary for the list.
Once the text file has been read into memory, we close the file.

We then define a function for translating which envolves the user input (sentence) into an
array of strings ("enjot the excellent band tonight") ["enjoy", "the", "excellent", "band", "tonight"]

one we have the array of strongs representing the user's input sentence, we
loop though each word, find the keys matching the word, and return the back the value tied to that word
in our dictionary

After each word is translated, we then
Print out the translated sentence to the user.
"""
'''PSEUDO-CODE'''
"""
main:
   set sentence = input()
   set dictionary = translate()
   translate(sentence, dictionary)

translate(sentence, dictionary):
   words = for each of the word in the sentence
   for each word, translate
   print translated sentence to user

create_dictionary():
   read in textese.txt
   create list = each line from file
   close the file
   create a dict off the list
   return the dict

main()
"""
