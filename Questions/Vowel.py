# Write a Python program to test whether a passed letter is a vowel or not.
letter = input("Enter a letter");
if len(letter)>1:
    print("Enter a letter: ")
else:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' or letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
        print("It is a Vowel")
    else :
        print("It is not a vowel")