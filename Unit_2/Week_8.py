"""
CODING DORS
UNIT 2 - LOOPS - https://cs50.harvard.edu/python/2022/notes/2/
WEEK 8 - Dictionaries - https://www.codingdors.com/week/8
"""





# https://www.codingdors.com/problem/312
"""
create_dictionary
Show Solution
Given a string 'name' and an integer 'age', return a dictionary with the pair of key 'name' and value 'age' added. 
Hint: Dictionaries are used to store data values in key:value pairs.
create_dictionary(gi', 25) -> {'gi': 25}
create_dictionary('leo', 41) -> {'leo': 41}
create_dictionary('rod', 12) -> {'rod': 12}
"""
# My Code
        def create_dictionary(name, age):
            dicionario = {name: age}
            return dicionario
        
# Solution
        def create_dictionary(name, age):
          new_dict = {name: age}
          return new_dict

# IA's Solutions
# Certainly! Here's an alternative solution using dictionary comprehension:
def create_dictionary(name, age):
    return {name: age}
# This solution is more concise and uses dictionary comprehension to directly create and return the dictionary with the key-value pair of 'name' and 'age'. It achieves the same result as the original solution but in a more compact form.






# https://www.codingdors.com/problem/315
"""
add_element_dictionary
Show Solution
Given a dictionary called 'students', a string 'name' and an integer 'age', return the dictionary 'student' with the pair of key 'name' and value 'age' added. 
Hint: Dictionaries are used to store data values in key:value pairs.
add_element_dictionary({'leo': 12}, 'gi', 25) -> {'leo':12, 'gi': 25}
add_element_dictionary({'fe': 27}, 'leo', 41) -> {'fe': 27,'leo': 41}
add_element_dictionary({}, 'rod', 12) -> {'rod': 12}
"""
# My Code

        
# Solution
def add_element_dictionary(students, name, age):
	students[name] = age
	return students

# IA's Solutions
# Sure! Your solution is already quite efficient and straightforward. Another way to achieve the same result is by using the `update` method of the dictionary class. Here's an alternative solution using the `update` method:
def add_element_dictionary(students, name, age):
    students.update({name: age})
    return students
# In this solution, `update` method takes a dictionary with one key-value pair as an argument and updates the original `students` dictionary with the new key-value pair. Finally, it returns the updated dictionary.





# https://www.codingdors.com/problem/316
"""
return_value
Show Solution
We have a dictionary 'd' that contains as key the fruit and the value its price. Given a string 'fruit', return the price of this fruit in the dictionary.

return_value({'apple': 0.5, 'banana': 0.25, 'cherry': 0.75}, 'apple') -> 0.5
return_value({'apple': 0.5, 'banana': 0.25, 'cherry': 0.75}, 'cherry') -> 0.75
"""
# My Code
        def return_value(d, fruit):
            return d[fruit]
# ou então
        def return_value(d, fruit):
            try:
                price = d[fruit]
                return price
            except:
                return "Fruit not found."
        
# Solution
        def return_value(d, fruit):
        	price = d[fruit]
        	return price

# IA's Solutions
# Certainly! Your solution is concise and correct. Here is an alternative solution using the get() method which allows us to provide a default value in case the fruit is not found in the dictionary:
def return_value(d, fruit):
    return d.get(fruit, "Fruit not found")
# In this solution, if the fruit is not found in the dictionary, it will return the string " Fruit not found " instead of raising a KeyError.
# Another alternative solution would be to use a try-except block to handle the case when the fruit is not found in the dictionary:
def return_value(d, fruit):
    try:
        return d[fruit]
    except KeyError:
        return "Fruit not found"
# This solution is similar to using the get() method but uses a try-except block instead.





# https://www.codingdors.com/problem/30
"""
find_person
Show Solution
Given a dictionary 'd' and a string 'name', return True if the given name exist in our dictionary. Otherwise, False. 
find_person({'Gi': 123, 'Leo': 456}, 'Gi') -> True 
find_person({'Gi': 123, 'Leo': 456}, 'Ana') -> False

Theory
find_person
1. Dictionaries: A dictionary is a collection of key-value pairs. Each key is separated from its value by a colon (:), and the pairs are separated by commas. All keys in a dictionary must be unique. 
{'key1': 'value1', 'key2': 'value2'}
2. Membership operators: 'in' and 'not in' are membership operators in Python. They are used to test whether a value or variable is found in a sequence (string, list, tuple, set, or dictionary). 
'hello' in 'hello world'
 returns True.
3. Boolean values: bool is a built-in data type in Python used to represent the truth values True and False. 
x = True
Therefore, in order to solve the problem, we can check whether the given name is a key in our dictionary using the 'in' membership operator. If it is, return True, otherwise, return False.

Hint
find_person
1. You need to check if the given name is a key in the dictionary. 
2. Use the 'in' keyword to check if the name exists in the dictionary. 
3. 'in' keyword returns True if the name exists in the dictionary and False otherwise.
"""
# My Code
	def find_person(d: dict,name: str) -> bool:
	    if name in d: # == True - In Python, the `in` operator already returns a boolean value (True or False) based on whether the specified key exists in the dictionary. So there is no need to compare it explicitly with `True`.
	        return True
	    else:
	        return False
        
# Solution
	def find_person(d: dict,name: str) -> bool:
		if name in d:
		  return True
		else:
		  return False

# IA's Solutions
# 1. Using the `get` method:
def find_person(d: dict, name: str) -> bool:
    return d.get(name) is not None
# Explanation: The `get` method retrieves the value associated with the specified key in a dictionary. If the key is not found, it returns `None`. By checking if the return value is not `None`, we can determine if the key exists in the dictionary.
# 2. Using the `in` keyword with a ternary operator:
def find_person(d: dict, name: str) -> bool:
    return True if name in d else False
# Explanation: This solution uses a ternary operator to achieve the same result as your original solution in a single line. If the name exists in the dictionary, it returns `True`, otherwise it returns `False`.
# 3. Using the `keys` method:
def find_person(d: dict, name: str) -> bool:
    return name in d.keys()
# Explanation: The `keys` method returns a view object that displays a list of all the keys in the dictionary. By checking if the name is in this list of keys, we can determine if the name exists in the dictionary. 





# https://www.codingdors.com/problem/233
"""
dictionary_size
Show Solution
Given a dictionary, return the number of key-value pairs it contains.

dictionary_size({}) -> 0
dictionary_size({'name': 'Gi'}) -> 1
dictionary_size({'a':1, 'b':4, 'c': 7}) -> 3

Theory
dictionary_size
1. Dictionary: A collection of key-value pairs that are unordered, changeable, and indexed.
example_dict = {'a': 1, 'b': 2, 'c': 3}
2. Key: The identifier used to access a value in a dictionary.
example_key = 'a'
3. Value: The data associated with a key in a dictionary.
example_value = 1
4. Length: The number of elements in a collection.
example_len = len(example_dict)

Hint
dictionary_size
Think about how you would count the number of items in a list. 
Can the same approach be applied to a dictionary?
"""
# My Code
	def dictionary_size(d):
	    tamanho_dicionario = len(d)
	    return tamanho_dicionario
        
# Solution
	def dictionary_size(d):
		return len(d)

# IA's Solutions
# 1. Using the `len()` function directly on the dictionary's items:
def dictionary_size(d):
    return len(d.items())
# Explanation: This solution uses the `items()` method of dictionaries to get a view of all key-value pairs and then uses the `len()` function to determine the number of key-value pairs.
# 2. Using a list comprehension:
def dictionary_size(d):
    return len([(k, v) for k, v in d.items()])
# Explanation: This solution uses a list comprehension to generate a list of key-value pairs from the dictionary and then calculates the length of that list to determine the number of key-value pairs.






# https://www.codingdors.com/problem/236
"""
update_value
Show Solution
Given a dictionary, a key, and a value, update the value associated with the key in the dictionary. If the key does not exist, add the key-value pair to the dictionary.

update_value({}, 'name', 'Gi') -> {'name': 'Gi'}
update_value({'name': 'Gi'}, 'name', 'Leo') -> {'name': 'Leo'}
update_value({'name': 'Gi'}, 'age', 25) -> {'name': 'Gi', 'age': 25}

Theory
update_value
1. Dictionary: A dictionary is a collection of key-value pairs enclosed in curly braces 
{}
. Each key is unique and is associated with a value. 
{"name": "John", "age": 25, "city": "New York"}
2. Key: A key is a unique identifier in a dictionary used to access its associated value. Keys must be immutable, meaning they cannot be changed once created. 
"name"
3. Value: A value is a data that is associated with a particular key in a dictionary. Values can be of any data type including strings, numbers, lists, or even another dictionary. 
"John"
4. Update: To update a value in a dictionary, simply access the key and assign it a new value. If the key does not exist, it will add the key-value pair to the dictionary. 
my_dict["name"] = "Jane"
5. Add: To add a new key-value pair to a dictionary, simply assign a value to a new key. 
my_dict["city"] = "Los Angeles"

Hint
update_value
1. You will need to use the dictionary's built-in methods for updating or adding new key-value pairs.
2. Pay attention to the data types of the key and value you are working with.
3. Consider using conditional statements to check if the key already exists in the dictionary.
4. Remember to assign the updated dictionary back to the original variable.
"""
# My Code
	def update_value(d, key, value):
		if key in value:
		  d[key] = value
		  return d
		else:
		  d[key] = value
		  return d
		  
		# Since we'll change the value either way, 
		# you can do only as follow:
		d[key] = value
		return d
        
# Solution
	def update_value(d, key, value):
		if key in value:
		  d[key] = value
		  return d
		else:
		  d[key] = value
		  return d
		  
		# Since we'll change the value either way, 
		# you can do only as follow:
		d[key] = value
		return d

# IA's Solutions
# Solution 1: Using dictionary methods
def update_value(d, key, value):
    d[key] = value
    return d
# Explanation: This solution directly assigns the key-value pair to the dictionary. If the key already exists, it will update the value; otherwise, it will add a new key-value pair to the dictionary.
# Solution 2: Using the setdefault() method
def update_value(d, key, value):
    d.setdefault(key, value)
    return d
# Explanation: The setdefault() method checks if a key exists in the dictionary. If the key is present, it returns the corresponding value. If the key is not found, it adds the key with the specified value to the dictionary and returns the value.
# Solution 3: Using the update() method
def update_value(d, key, value):
    d.update({key: value})
    return d
# Explanation: The update() method adds the key-value pair to the dictionary. If the key already exists, it will update the value; otherwise, it will add a new key-value pair to the dictionary.





# https://www.codingdors.com/problem/
"""

"""
# My Code

        
# Solution


# IA's Solutions






# https://www.codingdors.com/problem/
"""

"""
# My Code

        
# Solution


# IA's Solutions






# https://www.codingdors.com/problem/
"""

"""
# My Code

        
# Solution


# IA's Solutions






# https://www.codingdors.com/problem/
"""

"""
# My Code

        
# Solution


# IA's Solutions






# https://www.codingdors.com/problem/
"""

"""
# My Code

        
# Solution


# IA's Solutions






# https://www.codingdors.com/problem/
"""

"""
# My Code

        
# Solution


# IA's Solutions






# https://www.codingdors.com/problem/
"""

"""
# My Code

        
# Solution


# IA's Solutions






# https://www.codingdors.com/problem/
"""

"""
# My Code

        
# Solution


# IA's Solutions






# https://www.codingdors.com/problem/
"""

"""
# My Code

        
# Solution


# IA's Solutions



# https://www.codingdors.com/problem/
"""

"""
# My Code

        
# Solution


# IA's Solutions






# https://www.codingdors.com/problem/
"""

"""
# My Code

        
# Solution


# IA's Solutions






# https://www.codingdors.com/problem/
"""

"""
# My Code

        
# Solution


# IA's Solutions






# https://www.codingdors.com/problem/
"""

"""
# My Code

        
# Solution


# IA's Solutions









# https://www.codingdors.com/problem/
"""

"""
# My Code

        
# Solution


# IA's Solutions






