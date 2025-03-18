def Count(str):
    count_vowel=count_constant=0 #declare count of vowels and constant as 0

    vowel="AEIOUaeiou" #define All vowel in string

    for char in str:   #get one char from input  String

        if char in vowel:  #Check if char match with vowels

            count_vowel=count_vowel+1 #if True Count Vowel count increased by 1
        else:
            count_constant=count_constant+1 #if false Count Constant increased by 1

    return count_vowel,count_constant # return count of vowels and constant 

str=input("Enter String : ") #user input String

print(Count(str))
