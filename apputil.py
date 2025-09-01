#Author: Bella Roberson
#Date: 2025-09-01
#INFO-H501 Week 1 Exercise 1
def palindrome(word): #creates function to check if statement is a palindrome or contains palindromic words
    lower_statement = word.lower() #converts statement to lowercase
    cleaned = ''.join(char for char in lower_statement if char.isalnum()) #removeds spaces and punctuation
    if cleaned == cleaned[::-1]: #checks if cleaned statement is a palindrome (reads the same forwards and backwards)
        return True #returns this if it is a palindrome
    else: #if it is not a palindrome, checks for palindromic words
        palindromes = [] #creates list to store palindromic words
        for string in lower_statement.split(): #splits statement into words and checks each word through iteration
            cleaned_word = ''.join(char for char in string if char.isalnum()) #removes spaces and punctuation from each individual word
            if cleaned_word == cleaned_word[::-1] and len(cleaned_word) > 1: #checks if cleaned word reads the same forwards and backwards and has more than 1 character
                palindromes.append(cleaned_word) #adds palindromic word to list if above is true
        if len(palindromes) == 0: #checks if there are no palindromic words in the list to return appropriate message
            return False
            # return "Your statement isn't a palindrome, and there are no palindromic words in the statement."
        else: #if there are palindromic words in the list, returns them with proper message
            return False
            #return "Your statement isn't a palindrome, but the following words in the statement are!: " + str(palindromes)

#Author: Bella Roberson
#Date: 2025-09-01
#INFO-H501 Week 1 Exercise 2
def parentheses(sequence): #creates function to check if parentheses are balanced
    count = 0 #creates counter variable to keep track of parentheses
    for char in sequence: #iterates through each character in the inputted sequence
        if char == '(': #if character is an opening parenthesis, adds 1 to counter
            count += 1
        elif char == ')': #if character is a closing parenthesis, subtracts 1 from counter
            count -= 1
    return count == 0 #if counter is 0 (not greater than or less than 0), parentheses are balanced and returns True. If counter is not 0, parentheses are not balanced and returns False.
    