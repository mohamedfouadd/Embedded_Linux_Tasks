import string


vowels=['a','e','o','u','i']
user_input = input ("please enter a letter:")
letter = user_input[0]
if user_input in vowels:
    print("the user input is a vowel")
else:
    print("the user input is not a vowel")

