"""
CODING DORS
UNIT 2 - LOOPS - https://cs50.harvard.edu/python/2022/notes/2/
WEEK 6 - Strings 2 - https://www.codingdors.com/week/6
"""





# https://www.codingdors.com/problem/133
"""
count_char
Show Solution
Write a function that counts the occurrences of a specified character in a given string.
count_char('hello', 'l') -> 2
count_char('code', 'd') -> 1
count_char('banana', 'a') -> 3

Theory
count_char
1. Variables that are passed into a function when calling it. These parameters allow the function to accept different input values for processing. 
def example(parameter1, parameter2):
2. A way of accessing specific characters in a string. Each character in the string has an index position starting from 0 for the first character. For example, in the string "hello", the first (leftmost) letter 'h' has an index position of 0, the second letter 'e' has an index position of 1, and so on. 
string_var[index]
3. Statements that execute different code paths based on a condition being met. In Python, the if, elif, and else keywords are used to create conditional statements. For example: 
if condition1:
  # code block 1
elif condition2:
  # code block 2
else:
  # code block 3
4.  A way of iterating over a sequence of items, such as a string or a list. The 'for' keyword is used, along with a temporary variable to hold each item in the sequence as it's being processed. For example: 
for item in sequence:
  # do something with item
5. The process of combining two or more strings into a single string. In Python, the + operator is used for concatenation. For example: 
"hello" + "world"
 would result in the string "helloworld".

Hint
count_char
1. You will need to use a loop to iterate through each character in the string.
2. You will need to use an if statement to check if the current character is the specified character.
3. You will need to use a counter variable to keep track of how many times the specified character appears in the string.
4. At the end of the loop, you will need to return the counter variable.
"""
# My Code
  def count_char(s: str, char_to_count: str) -> int:
      contagem = 0
      for char in s:
          if char.lower() == char_to_count.lower():
              contagem += 1
          else:
              contagem += 0
      return contagem

# Solution
  def count_char(s: str, char_to_count: str) -> int:
  	count = 0
  	for i in s:
  	  if i.lower() == char_to_count.lower():
  	    count = count + 1
  	return count

# IA's Solutions
# 1. Using the `count()` method:
def count_char(s: str, char_to_count: str) -> int:
    return s.count(char_to_count)
# Explanation: The `count()` method in Python is a built-in method for strings that returns the number of occurrences of a specified substring or character in the given string. This solution simply leverages the `count()` method to directly calculate the count of the specified character in the string `s`.
# 2. Using list comprehension:
def count_char(s: str, char_to_count: str) -> int:
    return sum(1 for char in s if char == char_to_count)
# Explanation: This solution uses a list comprehension to create a list of `1` for each occurrence of the specified character in the string `s`. The `sum()` function then sums up all the `1` values, effectively counting the occurrences of the specified character.





# https://www.codingdors.com/problem/281
"""
count_lower_letters
Show Solution
Write a function that counts the number of lowercase letters present in a given string 's'.
count_lower_letters("Hello World") → 8
count_lower_letters("LOWERCASE") → 0
count_lower_letters("MixedCase123") → 5

Theory
count_lower_letters
Every character in a string corresponds to an index, starting with 0 for the first character. You can access any character in a string by referring to its index.
my_string = "Hello"
first_char = my_string[0]  # This will be 'H'
You can loop through the characters in a string using a for loop. This lets you examine or operate on each character individually.
for char in "Hello":
    print(char)
The islower() method returns True if the character is a lowercase letter, otherwise it returns False.
letter = "a"
result = letter.islower()  # This will be True
While iterating over a sequence, you can maintain a counter that you increment whenever a certain condition is met.
count = 0
for num in [1, 2, 3, 2, 4, 2]:
    if num == 2:
        count += 1
# count will be 3 after this loop

Hint
count_lower_letters
1. For each character, determine if it's lowercase. There's a built-in Python method for strings that helps with this.
2.Consider using a variable (e.g., count) to keep track of the number of lowercase letters you encounter as you iterate through the string.
3. Once you've finished iterating over the entire string, count should hold the total number of lowercase letters. This will be your final answer to return.
"""
# My Code
  def count_lower_letters(s: str) -> int:
      contador_islower = 0
      for char in s:
          if char.islower():
              contador_islower += 1
      return contador_islower

# Solution
  def count_lower_letters(s: str) -> int:
  	count = 0
  	for i in s:
  	  if i.islower() == True:
  	    count = count + 1
  	return count

# IA's Solutions
# Sure! Here's an alternative solution to count the number of lowercase letters in a string in Python:
def count_lower_letters(s: str) -> int:
    return sum(1 for char in s if char.islower())
# In this solution, a generator expression `1 for char in s if char.islower()` is used within the `sum()` function to count the number of occurrences where `char` is a lowercase letter in the string `s`. The `sum()` function then adds up the number of occurrences and returns the total count of lowercase letters in the string.
# This solution leverages the power of generator expressions and the `sum()` function to provide a concise and efficient way to count lowercase letters in a string.





# https://www.codingdors.com/problem/128
"""
count_vowels_str
Show Solution
Write a function that counts the number of vowels in a given string.
count_vowels_str('hello') -> 2
count_vowels_str('codingDORS') -> 3
count_vowels_str('APPLEbanana') -> 5

Theory
count_vowels_str
1. Strings: A sequence of characters 
string = 'hello'
2. Loops: Execute a block of code repeatedly 
for char in string:
3. Conditionals: Execute different code depending on a condition 
if char in vowels:
4. Counters: Keep track of a running total 
count += 1
5. Vowels: Letters A, E, I, O, U (including lowercase) 
vowels = 'aeiouAEIOU'

Hint
count_vowels_str
- The function should take a string as input.
- You will need to define a list of vowels.
- Loop over each character in the input string and check if it's a vowel.
- If the character is a vowel, add 1 to a counter variable.
- Return the counter variable at the end of the loop.
"""
# My Code
  def count_vowels_str(s: str) -> int:
      contador_vogais = 0
      lista_vogais = ['a', 'e', 'i', 'o', 'u']
      for char in s.lower():
          if char in lista_vogais:
              contador_vogais += 1
      return contador_vogais

# Solution
  def count_vowels_str(s: str) -> int:
  	vowels = ['a', 'e', 'i', 'o', 'u']
  	count = 0
  	for i in s:
  	  if i.lower() in vowels:
  	    count = count + 1
  	return count

# IA's Solutions
# 1. Using a dictionary to store the vowels:
def count_vowels_str(s: str) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return sum(1 for char in s.lower() if char in vowels)
# Explanation: In this solution, we use a set to store the vowels. We then use a generator expression inside the sum function to iterate through each character in the string, check if it is a vowel, and count the number of vowels found.
# 2. Using the count method:
def count_vowels_str(s: str) -> int:
    return sum(s.lower().count(v) for v in ['a', 'e', 'i', 'o', 'u'])
# Explanation: This solution takes advantage of the count method available for strings, which returns the number of occurrences of a specific substring in the given string. We use a list comprehension to iterate through each vowel in the list and count the number of occurrences of each vowel in the string 's'. Finally, we sum up the counts for each vowel to get the total number of vowels in the string.
def count_vowels_str(s: str) -> int:
    vowels = "aeiouAEIOU"
    contador_vogais = 0
    for char in s:
        if char in vowels:
            contador_vogais += 1
    return contador_vogais





# https://www.codingdors.com/problem/129
"""
count_consonants_str
Show Solution
Write a function that counts the number of consonants in a given string.
count_consonants_str('hello') -> 3
count_consonants_str('codingDORS') -> 7
count_consonants_str('APPLEbanana') -> 6

Theory
count_consonants_str
1. Strings in Python: A string is a sequence of characters enclosed in quotes. Strings are immutable, meaning that once a string is created, it cannot be modified. 
'hello'
2. For loop: A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string). 
for char in 'hello':
3. Conditional statements: Conditional statements allow you to execute different code depending on the state of your program at runtime. 
if char not in ['a', 'e', 'i', 'o', 'u']:
4. Counter: A counter is a variable used to keep track of something, typically the number of occurrences of a particular value. 
count = 0

Hint
count_consonants_str
1. Remember that vowels are a, e, i, o, and u. Any letter that is not a vowel is a consonant. 
2. You can use the lower() method to convert all letters in the string to lowercase for easier comparison. 
3. You can initiate a counter variable to keep track of the number of consonants found. 
4. Use a for loop to iterate through each letter in the string. 
5. Use an if statement to check if the letter is a consonant. If so, increment the counter variable.
"""
# My Code
  def count_consonants_str(s: str) -> int:
      nao_consoantes = ['a', 'e', 'i', 'o', 'u']
      contador_consoantes = 0
      for char in s.lower():
          if char not in nao_consoantes:
              contador_consoantes += 1
      return contador_consoantes

# Solution
  def count_consonants_str(s: str) -> int:
  	vowels = ['a', 'e', 'i', 'o', 'u']
  	count = 0
  	for i in s:
  	  if i.lower() not in vowels:
  	    count = count + 1
  	return count

# IA's Solutions
# 1. Using Regular Expressions:
import re
def count_consonants_str(s: str) -> int:
    consonants = re.findall(r'[bcdfghjklmnpqrstvwxyz]', s.lower())
    return len(consonants)
# This solution uses the `re.findall()` function from the `re` module to find all consonants in the string using a regular expression pattern. The pattern `[bcdfghjklmnpqrstvwxyz]` matches any lowercase consonant. Then it returns the count of consonants found.
# 2. Using Set Intersection:
def count_consonants_str(s: str) -> int:
    vowels = 'aeiou'
    consonants = set(s.lower()) - set(vowels)
    return len(consonants)
# In this solution, we first define a set of vowels and then create a set of all unique characters in the given string excluding vowels. Finally, it returns the count of consonants in the set.





# https://www.codingdors.com/problem/132
"""
find_char
Show Solution
Write a function that returns the index of the first occurrence of a specified character in a given string or -1 if the character is not present.
find_char('banana', 'b') -> 0
find_char('hello', 'l') -> 2
find_char('code', 'a') -> -1

Theory
find_char
1. Strings: Strings are a sequence of characters enclosed in single, double, or triple quotes. They are immutable and each character can be accessed by its index. 
'I am a string'
 is an example of a string.
2. Indexing: Indexing is the way we access individual elements in a sequence. It is done using a numeric index inside square brackets. The first element in a sequence has an index of 0. 
'hello'[1]
 will return 'e'.
3. for loop: A for loop is used to iterate over a sequence of elements. It is used to execute a block of code repeatedly. 
for item in sequence:
 is the syntax for a for loop.
4. if statement: An if statement is used to check a condition and execute a block of code if the condition is true. 
if condition:
 is the syntax. 
5. return statement: A return statement is used to exit a function and return a value to the caller. 'return value' is the syntax. Example:
# Example for indexing
word = 'hello'
print(word[1]) # output is 'e'
# Example for for loop
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit) # outputs the fruits in a new line each
# Example for if statement and return statement
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
print(is_even(4)) # output is True

Hint
find_char
1. The function should take two arguments: a string and a character to search for.
2. Use a loop to iterate through each character in the string.
3. Check if the current character matches the character being searched for.
4. If there is a match, return the index of that character in the string.
5. If the loop finishes without finding a match, return -1.
"""
# My Code


# Solution
  def find_char(s: str, char_to_find: str) -> int:
    for i in range(len(s)):
    	if char_to_find.lower() in s[i].lower():
    	   return i
    return -1

# IA's Solutions
# Certainly! Here is an alternative solution using the `index` method:
def find_char(s: str, char_to_find: str) -> int:
    try:
        index = s.lower().index(char_to_find.lower())
        return index
    except ValueError:
        return -1
# In this solution, we convert both the input string and the character to find to lowercase using the `lower()` method before searching for the character using the `index` method. If the character is found, the index of the first occurrence is returned. If the character is not found, a `ValueError` is raised, and we return -1.





# https://www.codingdors.com/problem/287
"""
contains_special_chars
Show Solution
Write a function that checks if the string contains either an exclamation mark (!) or a question mark (?). The function should return True if either (or both) of these characters are present, and False otherwise.
contains_special_chars("Hello! Welcome") → True
contains_special_chars("What is your name") → False
contains_special_chars("How are you?") → True

Theory
contains_special_chars
A for loop can be employed to traverse through each character in a string, facilitating individual examination or manipulation.
for char in "Hello":
    print(char)
For each char, check if it is equals to '!' or '?'.

Hint
contains_special_chars
1. Use Python string methods to check for the presence of characters in a string.
2. You have to check for two characters. Think about how you can efficiently check for both in one pass.
"""
# My Code
  def contains_special_chars(s: str) -> bool:
      especiais = ['!', '?']
      for char in s:
          if char in especiais:
              return True
      return False

# Solution
  def contains_special_chars(s: str) -> bool:
  	for i in s:
  	  if i == '!' or i == '?':
  	    return True
  	return False

# IA's Solutions
# 1. Using the any() function with a generator expression:
def contains_special_chars(s: str) -> bool:
    return any(char in ['!', '?'] for char in s)
# This solution utilizes the any() function along with a generator expression to iterate through the characters in the string and check if any of them are either '!' or '?'. It returns True if any special character is found, and False otherwise.
# 2. Using the set intersection method:
def contains_special_chars(s: str) -> bool:
    return bool(set(s) & set('!?'))
# This solution converts both the string and the special characters '!' and ? into sets and then calculates their intersection. If the intersection is not empty, it means that at least one special character is present in the string, so it returns True.
# 3. Using the any() function with a lambda function:
def contains_special_chars(s: str) -> bool:
    return any(map(lambda x: x in ['!', '?'], s))
# This solution combines the any() function with a lambda function to check if any character in the string is either '!' or '?'. It returns True if any special character is found, and False otherwise.





# https://www.codingdors.com/problem/283
"""
find_uppercase_position
Show Solution
Write a function that returns the position (index) of the first uppercase letter in a given string 's'. If there are no uppercase letters in the string, the function should return -1.
find_uppercase_position("hello World") → 6
find_uppercase_position("nouppercasehere") → -1
find_uppercase_position("CodingDors") → 0

Theory
find_uppercase_position
Every character in a string corresponds to an index, starting with 0 for the first character. You can access any character in a string by referring to its index.
my_string = "Hello"
first_char = my_string[0]  # This will be 'H'
You can loop through the characters in a string using a for loop. This lets you examine or operate on each character individually.
for char in "Hello":
    print(char)
The islower() method returns True if the character is a lowercase letter, otherwise it returns False.
letter = "a"
result = letter.islower()  # This will be True
While iterating over a sequence, you can maintain a counter that you increment whenever a certain condition is met.
count = 0
for num in [1, 2, 3, 2, 4, 2]:
    if num == 2:
        count += 1
# count will be 3 after this loop

Hint
find_uppercase_position
1. For each character in the string, use a Python string method to check if it is uppercase.
2. If you find an uppercase letter, immediately return its position (index).
3. If the loop completes without finding an uppercase letter, return -1.
"""
# My Code
  def find_uppercase_position(s: str) -> int:
      for i in range(len(s)):
          if s[i].isupper():
              return i
      return -1

  def find_uppercase_position(s: str) -> int:
      for i, char in enumerate(s):
          if char.isupper():
              return i
      return -1

# Solution
  def find_uppercase_position(s: str) -> int:
      for i in range(len(s)):
          if s[i].isupper():
              return 1
      else:
          return -1

# IA's Solutions
# Alternative Solution 0:
def find_uppercase_position(s: str) -> int:
    for i, char in enumerate(s):
        if char.isupper():
            return i
    return -1
# Alternative Solution 1:
def find_uppercase_position(s: str) -> int:
    return next((i for i, char in enumerate(s) if char.isupper()), -1)
# Explanation: This solution uses a generator expression inside the next function to iterate over the characters in the string and return the index of the first uppercase letter found. If no uppercase letter is found, it returns -1 using the default argument of next.
# Alternative Solution 2:
def find_uppercase_position(s: str) -> int:
    return s.index(next((char for char in s if char.isupper()), None))
# Explanation: This solution also uses a generator expression to find the first uppercase letter in the string, and then uses the index method to get the index of that letter in the original string. If no uppercase letter is found, it returns None which will raise a ValueError, hence it's important to handle this exception if using this approach.





# https://www.codingdors.com/problem/282
"""
extract_uppercase
Show Solution
Write a function that extracts all the uppercase letters from the given string 's' and return them as a new string in the order they appear.
extract_uppercase("Hello World") → "HW"
extract_uppercase("nouppercasehere") → ""
extract_uppercase("CODINGDORS") → "CODINGDORS"

Theory
extract_uppercase
A for loop can be employed to traverse through each character in a string, facilitating individual examination or manipulation.
for char in "Hello":
    print(char)
isupper() method returns True if a character is uppercase and False otherwise.
letter = "A"
result = letter.isupper()  # This will yield True
You can combine strings using the + operator. This action doesn't alter the original strings but yields a new string.
word1 = "Open"
word2 = "AI"
combined = word1 + word2  # "OpenAI"

Hint
extract_uppercase
1. For each character, check if it's an uppercase letter using a Python string method.
2. If the character is uppercase, append it to your initialized string or list.
3. After iterating over all characters, your string or list should contain all the uppercase letters from s.
4. Convert the list to a string if you used a list, and return the result. If you used a string, simply return it.
"""
# My Code
  def extract_uppercase(s: str) -> str:
      resultado = ""
      for char in s:
          if char.isupper() == True:
              resultado += char
      return resultado
          
# Solution
  def extract_uppercase(s: str) -> str:
      word = ''
      for i in s:
        if i.isupper():
          word = word + i
      return word

# IA's Solutions
# 1. Using list comprehension:
def extract_uppercase(s: str) -> str:
    return ''.join([char for char in s if char.isupper()])
# In this solution, a list comprehension is used to iterate over each character in the string 's' and only append the character to the list if it is uppercase. The list is then joined back together to form a new string containing only the uppercase letters.
# 2. Using filter and lambda function:
def extract_uppercase(s: str) -> str:
    return ''.join(filter(lambda char: char.isupper(), s))
# In this solution, the filter function is used along with a lambda function to filter out only the uppercase letters from the string 's'. The filtered characters are then joined back together to form a new string.





# https://www.codingdors.com/problem/284
"""
replace_a_with_four
Show Solution
Write a function that returns a new string where every instance of the letter 'a' (both uppercase and lowercase) in the given string 's' is replaced with the number '4'.
replace_a_with_four("Banana") → "B4n4n4"
replace_a_with_four("Apples are Amazing!") → "4pples 4re 4m4zing!"
replace_a_with_four("CodingDors") → "CodingDors"

Theory
replace_a_with_four
A for loop can be employed to traverse through each character in a string, facilitating individual examination or manipulation.
for char in "Hello":
    print(char)
isupper() method returns True if a character is uppercase and False otherwise.
letter = "A"
result = letter.isupper()  # This will yield True
You can combine strings using the + operator. This action doesn't alter the original strings but yields a new string.
word1 = "Open"
word2 = "AI"
combined = word1 + word2  # "OpenAI"

Hint
replace_a_with_four
1. Remember the problem requires you to replace both uppercase 'A' and lowercase 'a'. Consider converting the string to a uniform case before replacing, or use a method that can replace both cases simultaneously.
2. For each instance of 'a' or 'A' found, replace it with '4'.
3. After processing the entire string, return the modified string.
"""
# My Code
  def replace_a_with_four(s: str) -> str:
      p4l4vr4s = ""
      for char in s:
          if char == 'a' or char == 'A':
              char = '4'
              p4l4vr4s += char
          else:
              p4l4vr4s += char
      return p4l4vr4s
          
# Solution
  def replace_a_with_four(s: str) -> str:
  	word = ''
  	for i in s:
  	  if i.lower() == 'a':
  	    word = word + '4'
  	  else:
  	    word = word + i
  	return word

# IA's Solutions
# Sure! Here is an alternative solution using list comprehension:
def replace_a_with_four(s: str) -> str:
    return ''.join(['4' if char.lower() == 'a' else char for char in s])
# In this solution, we use list comprehension to iterate over each character in the input string `s`. We check if the lowercase version of the character is equal to 'a', and if it is, we replace it with '4'. Otherwise, we keep the character as is. Finally, we use `join()` to convert the list of characters back into a string.





# https://www.codingdors.com/problem/286
"""
replace_upper
Show Solution
Write a function that returns a new string where every uppercase letter from the given string 's' is replaced with an underscore (_).
replace_upper("helloWorld") → "hello_orld"
replace_upper("replaceUppeR") → "replace_ppe_"
replace_upper("cOdInG") → "c_d_n_"

Theory
replace_upper
A for loop can be employed to traverse through each character in a string, facilitating individual examination or manipulation.
for char in "Hello":
    print(char)
isupper() method returns True if a character is uppercase and False otherwise.
letter = "A"
result = letter.isupper()  # This will yield True
You can combine strings using the + operator. This action doesn't alter the original strings but yields a new string.
word1 = "Open"
word2 = "AI"
combined = word1 + word2  # "OpenAI"

Hint
replace_upper
1. Utilize Python string methods to identify uppercase letters.
2. For each uppercase letter found, replace it with an underscore.
3. Consider iterating over the string and building a new string based on the conditions mentioned.
"""
# My Code
  def replace_upper(s: str) -> str:
      replaced_uppers = ""
      for char in s:
          if char.isupper() == True:
              replaced_uppers += "_"
          else:
              replaced_uppers += char
      return replaced_uppers

# Solution
  def replace_upper(s: str) -> str:
  	word = ''
  	for i in s:
  	  if i.isupper():
  	    word = word + '_'
  	  else:
  	    word = word + i
  	return word

# IA's Solutions
# 1. Using list comprehension:
def replace_upper(s: str) -> str:
    return ''.join(['_' if char.isupper() else char for char in s])
# This solution uses list comprehension to iterate over each character in the input string 's'. If the character is uppercase, it replaces it with an underscore ('_'), otherwise, it keeps the character as it is. Finally, it joins all the characters back together to form the final replaced string.
# 2. Using a generator expression:
def replace_upper(s: str) -> str:
    return ''.join('_' if char.isupper() else char for char in s)
# This solution is similar to the previous one but uses a generator expression instead of a list comprehension. The main advantage of using a generator expression is that it is more memory efficient as it generates the values on-the-fly without creating a list in memory.
# 3. Using a regular expression:
import re
def replace_upper(s: str) -> str:
    return re.sub(r'[A-Z]', '_', s)
# This solution uses the `re.sub()` function from the `re` module to replace all uppercase letters (A-Z) in the input string 's' with an underscore ('_'). This is a more concise and efficient way to achieve the desired result using regular expressions.





# https://www.codingdors.com/problem/291
"""
triple_char
Show Solution
Given a string 's', return a new string where for every char in the original, there are three chars.
triple_char('The') → 'TTThhheee'
triple_char('Abc') → 'AAAbbbccc'
triple_char('code') → 'cccooodddeee'

Theory
triple_char
A for loop can be employed to traverse through each character in a string, facilitating individual examination or manipulation.
for char in "Hello":
    print(char)
You can combine strings using the + operator. This action doesn't alter the original strings but yields a new string.
word1 = "Open"
word2 = "AI"
combined = word1 + word2  # "OpenAI"

Hint
triple_char
1. Consider iterating over each character in the given string.
2. Think about how you can repeat each character in a string.
3. As you iterate, build a new string that incorporates the repeated characters.
"""
# My Code
  def triple_char(s: str) -> str:
      result_triple_char = ""
      for char in s:
          result_triple_char += char*3 
      return result_triple_char

# Solution
  def triple_char(s: str) -> str:
  	word = ''
  	for i in s:
  	  word = word + (i * 3)
  	return word

# IA's Solutions
# Certainly! Here is an alternative solution in Python using list comprehension:
def triple_char(s: str) -> str:
    return "".join([char*3 for char in s])
# In this alternative solution, a list comprehension is used to iterate over each character in the input string 's'. For each character, it multiplies the character by 3 and creates a list of tripled characters. Finally, the ''.join() method is used to concatenate the characters in the list into a single string, which is then returned.





# https://www.codingdors.com/problem/292
"""
hi_ho
Show Solution
Return True if the string "hi" and "ho" appear the same number of times in the given string.

hi_ho('hiho') → True
hi_ho('hihi') → False
hi_ho('1hi1hohello') → True

Theory
hi_ho
When dealing with strings (or other sequences), sometimes you don't just need the value of each item, but also its position (index) within the sequence. 
This is particularly useful when comparing two sequences, modifying a sequence based on its indices, or when you need direct access to adjacent elements.
The range() function generates a sequence of numbers, which when combined with len() (a function that returns the length of a sequence) produces a sequence of indices that represent the positions of items in a sequence.
s = "Hello"
for i in range(len(s)):
    print(i, s[i])  # Prints index and the character at that index
While iterating over a sequence, you can maintain a counter that you increment whenever a certain condition is met.
count = 0
s = "hello"
for i in range(len(s)):
    if s[i] == 'h':
        count += 1

Hint
hi_ho
1. Use string methods or manual iteration to count the occurrences of specific substrings in a string.
2. After counting occurrences of "hi" and "ho", compare the counts to determine the return value.
"""
# My Code
  def hi_ho(s: str) -> bool:
      conta_hi = 0
      conta_ho = 0
      tamanho = len(s)
      
      for i in range(tamanho-1): # range starts at 0
          if s[i:i+2] == 'hi':
              conta_hi += 1
          if s[i:i+2] == 'ho':
              conta_ho += 1
      
      return True if conta_hi == conta_ho else False
      
# Solution
  def hi_ho(s: str) -> bool:
  	count_hi = 0
  	count_ho = 0
  	# Count the 'hi's and 'ho's
  	for i in range(len(s)-1):
  	  if s[i:i+2] == 'hi':
  	    count_hi += 1
  	  elif s[i:i+2] == 'ho':
  	    count_ho += 1
  	# Check if they are the same
  	if count_hi == count_ho:
  	  return True
  	else:
  	  return False

# IA's Solutions
# Sure! Here is an alternative solution using a regular expression to count the number of occurrences of 'hi' and 'ho' in the given string:
import re
def hi_ho(s: str) -> bool:
    count_hi = len(re.findall(r'hi', s))
    count_ho = len(re.findall(r'ho', s))
    return count_hi == count_ho
# In this solution:
# - `re.findall(r'hi', s)` finds all non-overlapping occurrences of 'hi' in the input string `s` and returns them as a list. The length of this list gives the count of 'hi' occurrences in the string.
# - Similarly, `re.findall(r'ho', s)` gives the count of 'ho' occurrences.
# - Finally, it compares the counts of 'hi' and 'ho' and returns True if they are equal, otherwise False.





# https://www.codingdors.com/problem/293
"""
count_code_times
Show Solution
Return the number of times that the string "code" appears anywhere in the given string.
count_code_times('aaacodebbb') → 1
count_code_times('codexxcode') → 2
count_code_times('cozexxcope') → 0

Theory
count_code_times
When dealing with strings (or other sequences), sometimes you don't just need the value of each item, but also its position (index) within the sequence. 
This is particularly useful when comparing two sequences, modifying a sequence based on its indices, or when you need direct access to adjacent elements.
The range() function generates a sequence of numbers, which when combined with len() (a function that returns the length of a sequence) produces a sequence of indices that represent the positions of items in a sequence.
s = "Hello"
for i in range(len(s)):
    print(i, s[i])  # Prints index and the character at that index
While iterating over a sequence, you can maintain a counter that you increment whenever a certain condition is met.
count = 0
s = "hello"
for i in range(len(s)):
    if s[i] == 'h':
        count += 1

Hint
count_code_times
1. Think about how you can iterate over the string and identify occurrences of "code".
2. Consider using a sliding window approach where you inspect chunks of the string of size 4.
3. Maintain a count of the number of times "code" is identified in the string.
"""
# My Code
  def count_code_times(s: str) -> int:
      contador = 0
      tamanho = len(s)
      
      for i in range(tamanho-1):
          if s[i:i+4] == 'code':
              contador += 1
      return contador

# Solution
  def count_code_times(s: str) -> int:
  	count = 0
  	for i in range(len(s)-3):
  	  if s[i:i+4] == 'code':
  	    count += 1
  	return count

# IA's Solutions
# 1. Using regular expressions:
import re
def count_code_times(s: str) -> int:
    return len(re.findall('code', s))
# Explanation: This solution uses the `re.findall` function from the `re` module to find all non-overlapping occurrences of the string "code" in the input string `s`. The function returns a list of all matching substrings, and the length of this list corresponds to the number of occurrences found.
# 2. Using list comprehension:
def count_code_times(s: str) -> int:
    return sum(1 for i in range(len(s)-3) if s[i:i+4] == 'code')
# Explanation: This solution uses a list comprehension to iterate over all possible substrings of length 4 in the input string `s`, checking if each substring is equal to "code". For each matching substring found, it adds 1 to the sum. The final result is the total count of occurrences of "code" in the string.





# https://www.codingdors.com/problem/136
"""
swap_case
Show Solution
Write a function that returns a new string with the case of each character in the given string swapped.
swap_case('hello') -> 'HELLO'
swap_case('CODE') -> 'code'
swap_case('aPpLe') -> 'ApPlE'

Theory
swap_case
1. String - A sequence of characters 
string_example = "Hello, World!"
2. For Loop - A loop that iterates over a sequence and executes the block of code for each element in the sequence 
for element in sequence:
3. If statement - A conditional statement that executes a block of code if the condition is true 
if condition:
4. isupper() and islower() methods - String methods that return True if all characters of a string are in uppercase or lowercase, respectively 
"Hello".isupper()
 returns False, 
"hello".islower()
 returns True
5. upper() and lower() methods - String methods that return a string with all characters in uppercase or lowercase, respectively 
"Hello".upper()
 returns "HELLO", 
"hello".lower()
 returns "hello"

 Hint
swap_case
- You need to iterate through each character in the string and check whether it is upper or lowercase. 
- Then, you need to change the case of each character accordingly and add it to a new string.
"""
# My Code
  def swap_case(s: str) -> str:
      nova_string = ""
      for char in s:
          if char.isupper() == True:
              nova_string += char.lower()
          elif char.isupper() == False:
              nova_string += char.upper()
          elif char.islower() == True:
              nova_string += char.upper()
          elif char.islower() == False:
              nova_string += char.lower()
      return nova_string

# Solution
  def swap_case(s: str) -> str:
  	word = ''
  	for i in s:
  	  if i.isupper():
  	    word = word + i.lower()
  	  else:
  	    word = word + i.upper()
  	return word

# IA's Solutions
# Alternative Solution 1:
def swap_case(s: str) -> str:
    return s.swapcase()
# Explanation: This solution uses the `swapcase()` method provided by Python for strings. It directly swaps the case of each character in the string and returns the modified string.
# Alternative Solution 2:
def swap_case(s: str) -> str:
    return ''.join([char.lower() if char.isupper() else char.upper() for char in s])
# Explanation: This solution uses a list comprehension to iterate over each character in the string. It checks if the character is uppercase, then converts it to lowercase, and vice versa. Finally, it joins the modified characters back together to form the new string.
# Alternative Solution 3:
def swap_case(s: str) -> str:
    return ''.join(char.lower() if char.isupper() else char.upper() for char in s)
# Explanation: This solution is similar to the previous one but with a slight modification in the way the characters are joined back together. It directly uses the generator expression inside the `join()` function to achieve the same result.





# https://www.codingdors.com/problem/140
"""
reverse_string
Show Solution
Write a function that takes a string as input and returns the string reversed.
reverse_string('hello') -> 'olleh'
reverse_string('code') -> 'edoc'
reverse_string('banana') -> 'ananab'

Theory
reverse_string
When dealing with strings (or other sequences), sometimes you don't just need the value of each item, but also its position (index) within the sequence. 
This is particularly useful when comparing two sequences, modifying a sequence based on its indices, or when you need direct access to adjacent elements.
The range() function generates a sequence of numbers, which when combined with len() (a function that returns the length of a sequence) produces a sequence of indices that represent the positions of items in a sequence.
s = "Hello"
for i in range(len(s)):
    print(i, s[i])  # Prints index and the character at that index
The range() function can take up to three arguments: start, stop, and step. By default, range starts at 0 and increments by 1. However, if we set the start to the last index, and step to -1, we can effectively iterate backwards through the sequence.
s = "Hello"
for i in range(len(s)-1, -1, -1):  # starts from len(s)-1, ends at 0
    print(i, s[i])  # Prints index and the character at that index in reverse order

Hint
reverse_string
1. Think about how you can manipulate strings in Python. 
2. Consider using a loop to iterate through the string.
3. Think about how you can concatenate characters to create a new string that is the reverse of the original string.
"""
# My Code
  def reverse_string(s: str) -> str:
      nova_s = ''
      for char in s[::-1]:
          nova_s += char
      return nova_s

# Solution
  def reverse_string(s: str) -> str:
  	word = ''
  	for i in range(len(s)-1, -1, -1):
  	  word = word + s[i]
  	return word

# IA's Solutions
# 1. Using the `join` function:
def reverse_string(s: str) -> str:
    return ''.join(reversed(s))
# Explanation: The `reversed` function returns an iterator that iterates over the elements of the string in reverse order. By using `join`, we can concatenate these elements back into a string.
# 2. Using list comprehension:
def reverse_string(s: str) -> str:
    return ''.join([s[i] for i in range(len(s)-1, -1, -1)])
# Explanation: This solution uses a list comprehension to iterate over the characters of the string in reverse order and then join them back into a string.
# 3. Using slicing:
def reverse_string(s: str) -> str:
    return s[::-1]
# Explanation: This solution utilizes string slicing to reverse the order of the characters in the string. By using `[::-1]`, we can easily achieve the desired result without the need for a loop.





# https://www.codingdors.com/problem/285
"""
reverse_swap
Show Solution
Write a function that returns a new string that is the reverse of the given string 's', and where the case of each letter in the original string is swapped (i.e., lowercase letters become uppercase and uppercase letters become lowercase).
reverse_swap("Hello") → "OLLEh"
reverse_swap("wOrLd123!") → "!321DlRoW"
reverse_swap("sWAP mE") → "eM pawS"

Theory
reverse_swap
When dealing with strings (or other sequences), sometimes you don't just need the value of each item, but also its position (index) within the sequence. 
This is particularly useful when comparing two sequences, modifying a sequence based on its indices, or when you need direct access to adjacent elements.
The range() function generates a sequence of numbers, which when combined with len() (a function that returns the length of a sequence) produces a sequence of indices that represent the positions of items in a sequence.
s = "Hello"
for i in range(len(s)):
    print(i, s[i])  # Prints index and the character at that index
The range() function can take up to three arguments: start, stop, and step. By default, range starts at 0 and increments by 1. However, if we set the start to the last index, and step to -1, we can effectively iterate backwards through the sequence.
s = "Hello"
for i in range(len(s)-1, -1, -1):  # starts from len(s)-1, ends at 0
    print(i, s[i])  # Prints index and the character at that index in reverse order
Conditional statements, primarily if, enable execution of specific blocks of code based on whether certain conditions are met.
char = 'a'
if char.isupper():
    # Handle uppercase letter
elif char.islower():
    # Handle lowercase letter

Hint
reverse_swap
1. Think about how to reverse strings in Python.
2. Research Python string methods that allow you to change the case of letters.
3. Determine the order of the operations (reverse first, then swap case or vice versa) that is most efficient or easier to implement.    
"""
# My Code
  def reverse_swap(s: str) -> str:
  	word = ''
  	for i in range(len(s)-1, -1, -1):
  	  if s[i].isupper():
  	    word += s[i].lower()
  	  else:
  	    word += s[i].upper()
  	return word

# Solution
  def reverse_swap(s: str) -> str:
  	word = ''
  	for i in range(len(s)-1, -1, -1):
  	  if s[i].isupper():
  	    word += s[i].lower()
  	  else:
  	    word += s[i].upper()
  	return word

# IA's Solutions
# Certainly! Here's an alternative solution using list comprehension and the join method:
def reverse_swap(s: str) -> str:
    return ''.join([char.lower() if char.isupper() else char.upper() for char in s[::-1]])
# In this solution:
# 1. `s[::-1]` reverses the given string.
# 2. The list comprehension iterates over each character in the reversed string.
# 3. For each character, it checks if it is uppercase using `char.isupper()`. If it is uppercase, it converts it to lowercase using `char.lower()`. If it is not uppercase (meaning it is lowercase or not a letter), it converts it to uppercase using `char.upper()`.
# 4. The resulting list of characters is joined using `join` to form the final reversed and swapped string.





# https://www.codingdors.com/problem/288
"""
has_matching
Show Solution
Given two strings 's1' and 's2', write a function that determines if the two strings share at least one letter in the same position. The function should return True if they do and False otherwise.
Assume that both strings will have the same length.
has_matching("apple", "abcde") → True
has_matching("hello", "world") → True
has_matching("dance", "lover") → False

Theory
has_matching
When dealing with strings (or other sequences), sometimes you don't just need the value of each item, but also its position (index) within the sequence. 
This is particularly useful when comparing two sequences, modifying a sequence based on its indices, or when you need direct access to adjacent elements.
The range() function generates a sequence of numbers, which when combined with len() (a function that returns the length of a sequence) produces a sequence of indices that represent the positions of items in a sequence.
s = "Hello"
for i in range(len(s)):
    print(i, s[i])  # Prints index and the character at that index
Strings are indexed starting from 0 for the first character. This indexing allows for the retrieval or modification of individual characters in a string.
text = "Python"
first_char = text[0]  # 'P'

Hint
has_matching
1. Iterate over the length of the strings (since they are of the same length).
2. For each position, compare the characters of both strings.
3. Think about when you can terminate the check early, as soon as a match is found.
"""
# My Code
  def has_matching(s1: str, s2: str) -> bool:
      tamanho = len(s1)    
      for i in range(tamanho):
          if s1[i] == s2[i]:
              return True
      return False

# Solution
  def has_matching(s1: str, s2: str) -> bool:
  	for i in range(len(s1)):
  	  if s1[i] == s2[i]:
  	    return True
  	return False

# IA's Solutions
# 1. Using zip() function:
def has_matching(s1: str, s2: str) -> bool:
    return any(char1 == char2 for char1, char2 in zip(s1, s2))
# In this solution, the zip() function is used to iterate over both strings simultaneously. We check if there is at least one matching character at the same index in both strings using the any() function, which returns True if any element in the iterable is true.
# 2. Using list comprehension:
def has_matching(s1: str, s2: str) -> bool:
    return any(s1[i] == s2[i] for i in range(len(s1)))
# This solution is similar to the original solution but uses a list comprehension to generate a list of boolean values indicating if the characters at each index match. The any() function is then used to check if there is at least one True value in the list.
# 3. Using zip() and set intersection:
def has_matching(s1: str, s2: str) -> bool:
    return bool(set(s1) & set(s2))
# In this solution, we convert both strings into sets and then calculate the intersection of the sets using the '&' operator. If there is at least one common character between the two strings, the intersection set will not be empty, and the bool() function will return True.





# https://www.codingdors.com/problem/289
"""
check_first_number
Show Solution
Given a string 's', determine if the first number appearing in the string is 0. The function should return False if the first number in the string is 0. If the string does not contain any numbers or if the first number appearing isn't 0, it should return True.
check_first_number("Hello") → True
check_first_number("Hell0") → False
check_first_number("H3ll0") → True

Theory
check_first_number
Looping through each character in a string is a fundamental concept. In Python, you can achieve this using a for loop.
for char in s:
    # process char
To identify whether a character is a number, we can use the isdigit() method which is built into Python's string handling.
if char.isdigit():
    # char is a number
When iterating through a list or string, if a certain condition is met, it might not be necessary to process the rest of the elements or characters. In such cases, the loop can be exited immediately using the break statement or by returning a value directly from inside the loop.
for i in s:
    if i == 0:
        return False
    else:
        return True

Hint
check_first_number
1. Loop through the string to identify the first occurrence of a digit.
2. Once a number is found, immediately check if it's 0.
3. Consider what to return if no numbers are found in the entire string.
"""
# My Code
  def check_first_number(s: str) -> bool:
      for char in s:
          if char.isdigit():
              if char == "0": # As soon as it occurs 
                  return False # Should return False if the first number in the string is 0.
              else:
                  return True # or if the first number appearing isn't 0, it should return True.                
      return True # If the string does not contain any numbers 

# Solution
  def check_first_number(s: str) -> bool:
  	for i in s:
  	  if i.isdigit():
  	    if i == '0':
  	      return False
  	    else:
  	      return True
  	# If we don't have any number, we need the next line
  	return True

# IA's Solutions
# Certainly! Here is an alternative solution for the given problem:
def check_first_number(s: str) -> bool:
    if s == "":
        return True  # If the string is empty, return True
    for char in s:
        if char.isdigit():
            if char == "0" and s.index(char) == 0:
                return False  # Return False if the first number in the string is 0
            else:
                return True  # Return True if the first number appearing isn't 0
    return True  # If the string does not contain any numbers, return True
# This solution follows a similar approach to the previous one but uses the `s.index(char) == 0` condition to check if the current number is the first character in the string. It returns False if the condition is met, indicating that the first number in the string is 0. Otherwise, it continues to check the remaining characters in the string. This solution also returns True if the string does not contain any numbers.





# https://www.codingdors.com/problem/290
"""
valid_vanity_plate
Show Solution
Given a string 's', determine if, after the first appearance of a number in the string, there are any letters. For a string to be considered valid, once numbers start appearing, they should not be followed by any letters.
valid_vanity_plate("ABC123") → True
valid_vanity_plate("AB12CD") → False
valid_vanity_plate("A1B2") → False

Theory
valid_vanity_plate
When dealing with strings (or other sequences), sometimes you don't just need the value of each item, but also its position (index) within the sequence. 
This is particularly useful when comparing two sequences, modifying a sequence based on its indices, or when you need direct access to adjacent elements.
The range() function generates a sequence of numbers, which when combined with len() (a function that returns the length of a sequence) produces a sequence of indices that represent the positions of items in a sequence.
s = "Hello"
for i in range(len(s)):
    print(i, s[i])  # Prints index and the character at that index
To identify the type of a character (whether it's a letter or a number), Python provides two helpful string methods: isdigit() and isalpha().
if char.isdigit():
    # char is a number
if char.isalpha():
    # char is a letter

Hint
valid_vanity_plate
1. Begin by initializing a flag or a variable (e.g., found_number) to False. This will be used to track when you've first encountered a number in the string.
2. Start by iterating over each character of the string s.
3. While iterating, check if the current character is a digit.
4. If it is a digit and found_number is False, set found_number to True. This indicates you've found your first number.
5. If found_number is True (meaning you've previously encountered a number), check if the current character is a letter. If it is a letter, immediately return False as this means a letter has appeared after a number.
6. If you complete the loop without returning False, it means one of the following:
- No numbers were found in the string.
- Numbers were found, but no letters followed them.
In both cases, you should return True.
7. Once found_number is set to True, you can skip checking if the other characters are digits since you're only concerned about letters appearing afterward.
"""
# My Code
  def valid_vanity_plate(s: str) -> bool:
      for i in range(len(s)):
          
          if s[i].isdigit():
              if s[i:].isdigit():
                  return True
              else:
                  return False
      
      return True

# Solution
  def valid_vanity_plate(s: str) -> bool:
  	for i in range(len(s)):
  	  if s[i].isdigit():
  	    if s[i:].isdigit():
  	      return True
  	    else:
  	      return False
  	# If we don't have any number, we should return True
  	return True

# IA's Solutions
# Certainly! Here is an alternative solution using a flag variable to keep track of whether letters have appeared after the first number:
def valid_vanity_plate(s: str) -> bool:
    number_found = False
    for char in s:
        if char.isdigit():
            number_found = True
        elif number_found and char.isalpha():
            return False
    return True
# Explanation:
# 1. We initialize a flag variable `number_found` to keep track of whether a number has been found in the string.
# 2. We iterate through each character in the string.
# 3. If the character is a number, we set `number_found` to True.
# 4. If `number_found` is True and the character is a letter, we immediately return False as the condition is violated.
# 5. If no violation is found after iterating through the string, we return True at the end.





# https://www.codingdors.com/problem/138
"""
split_string
Show Solution
Write a function that splits a given string into a list of words using a specified delimiter.
split_string('apple,banana,orange', ',') -> ['apple', 'banana', 'orange']
split_string('red.green.blue', '.') -> ['red', 'green', 'blue']
split_string('python/java/html', '/') -> ['python', 'java', 'html']

Theory
split_string
1. The process of splitting a string into a list using a specified delimiter. Example: 
string = 'apple,banana,orange'
delimiter = ','
result = string.split(delimiter) # ['apple', 'banana', 'orange']
2. The process of converting a list of strings into a single string by joining them with a specified delimiter. Example:
list_of_strings = ['apple', 'banana', 'orange']
delimiter = ','
result = delimiter.join(list_of_strings) # 'apple,banana,orange'
3. Providing default values for function arguments that can be overwritten if desired. Example:
def some_function(argument_1, argument_2='default_value'):
    # function code
    return result
In this example, if argument_2 is not provided when the function is called, it will use the default value of 'default_value'.
4. The process of creating a new string using variables and formatting techniques such as f-strings or the str.format() method. Example:
name = "Alice"
age = 30
result = f"My name is {name} and I am {age} years old." # "My name is Alice and I am 30 years old."

Hint
split_string
1. Start the function definition with the name and parameters.
2. Create an empty list to hold the words.
3. Use the "split" method on the string parameter to split it into words.
4. Use the delimiter parameter as the argument for the "split" method.
5. Use a loop to iterate through the words and append them to the empty list.
6. Return the list.
"""
# My Code
def split_string(s: str, delimiter: str) -> list:
    nova_lista = []
    nova_lista = s.split(delimiter)
    return nova_lista

# Solution
def split_string(s: str, delimiter: str) -> list:
	return s.split(delimiter)

# IA's Solutions
# 1. Using list comprehension:
def split_string(s: str, delimiter: str) -> list:
    return [word for word in s.split(delimiter)]
# Explanation:
# - In this solution, list comprehension is used to directly create a new list of words by splitting the input string 's' using the specified delimiter.
# - The split() method is used to split the string based on the delimiter and then each word is added to the new list using list comprehension.
# - Finally, the new list of words is returned.
# 2. Using map function:
def split_string(s: str, delimiter: str) -> list:
    return list(map(str.strip, s.split(delimiter)))
# Explanation:
# - In this solution, the map() function is used to apply the strip() method to each word in the list obtained after splitting the string.
# - The strip() method is used to remove any leading or trailing whitespaces from each word.
# - The map() function returns an iterator, so we convert it back to a list using the list() function before returning the final list of words.




