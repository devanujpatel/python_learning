class Reverse:

    def reverse_word(self,word):
        my_reverse_word = ""
        reversed=word[::-1]

        for letters in reversed:
            my_reverse_word  += letters
        print(my_reverse_word)

attribute=input("enter a word: ")
obj=Reverse()

obj.reverse_word(attribute)