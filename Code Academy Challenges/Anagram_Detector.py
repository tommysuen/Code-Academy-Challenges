# Write a function in your favorite programming language that will accept any
# two strings36 as parameters and return "1" if they are
# anagrams233 and "0" if they are not.

def anagram(string1, string2):
    #checks if the two strings are equal length, if not, then it is not an anagram
    if len(string1) != len(string2):
        print("Not an anagram")
        return

    elif len(string1) == len(string2):
        for x in range(len(string1)):
            if string1[x] in string2:
                #Checks each letter and replace comparison string's char with blank
                string2 = string2.replace(str(string1[x]), "")

        print("Anagram")
                

