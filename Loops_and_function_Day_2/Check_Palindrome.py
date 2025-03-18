def reverse_String(s):
    r_string=''            # define empty string
    for char in s:           #through loop we get single char from string
        r_string=char+r_string #add char to empty string one by one
    return r_string         # return Reverse String

str=input("Enter A String: ") # taken user input as String
reverse_str=reverse_String(str)

if str==reverse_str:   #check both string are Same 
    print("String is Palindrome") # if it is True String is Palindrome
else:
    print("String is Not Palindrome") #else String is Not Palindrome