# String methods

Python provides a set of built-in methods that we can use to alter and modify the strings.
The mathods covered are upper, lower, strip, rstrip, replace, split, capitalize, center, count, endswith, find, index, isalnum, isalpha, islower, isprintable, isspace, istitle, isupper, startswith, swapcase, title.

## upper():

The upper() method converts a string to upper case.

### Example:

```Python
str1 = "AbcDEfghIJ"
print(str1.upper())
```

### Output:

```Python
ABCDEFGHIJ
```

## lower():

The lower() method converts a string to lower case.

### Example:

```Python
str1 = "AbcDEfghIJ"
print(str1.lower())
```

### Output:

```Python
abcdefghij
```

## strip():

The strip() method removes any white spaces before and after the string.

### Example:

```Python
str2 = " Silver Spoon "
print(str2.strip)
```

### Output:

```Python
Silver Spoon
```

## rstrip():

the rstrip() removes any trailing characters.

### Example:

```Python
str3 = "Hello !!!"
print(str3.rstrip("!"))
```

### Output:

```Python
Hello
```

## replace():

The replace() method replaces all occurences of a string with another string. 

### Example:

```Python
str2 = "Silver Spoon"
print(str2.replace("Sp", "M"))
```

### Output:

```Python
Silver Moon
```

## split():

The split() method splits the given string at the specified instance and returns the separated strings as list items.

### Example:

```Python
str2 = "Silver Spoon"
print(str2.split(" "))      #Splits the string at the whitespace " ".
```

### Output:

```Python
['Silver', 'Spoon']
```

## capitalize():

The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.

### Example:

```Python
str1 = "hello"
capStr1 = str1.capitalize()
print(capStr1)
str2 = "hello WorlD"
capStr2 = str2.capitalize()
print(capStr2)
```

### Output:

```Python
Hello
Hello world
```

## center():

The center() method aligns the string to the center as per the parameters given by the user.

### Example:

```Python
str1 = "Welcome to the Console!!!"
print(str1.center(50))
```

### Output:

```Python
            Welcome to the Console!!!
```

We can also provide padding character. It will fill the rest of the fill characters provided by the user.

## count():

The count() method returns the number of times the given value has occurred within the given string.

### Example:

```Python
str2 = "Abracadabra"
countStr = str2.count("a")
print(countStr)
```

### Output:

```Python
4
```

## endswith():

The endswith() method checks if the string ends with a given value. If yes then return True, else return False.

### Example:

```Python
str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))
```

### Output:

```Python
True
```

We can even also check for a value in-between the string by providing start and end index positions.

### Example:

```Python
str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))
```

### Output:

```Python
True
```

## find():

The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.

### Example:

```Python
str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))
```

### Output:

```Python
10
```

As we can see, this method is somewhat similar to the index() method. The major difference being that index() raises an exception if value is absent whereas find() does not.

### Example:

```Python
str1 = "He's name is Dan. He is an honest man."
print(str1.find("Daniel"))
```

### Output:

```Python
-1
```

## index():

The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.

### Example:

```Python
str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Dan"))
```

### Output:

```Python
13
```

As we can see, this method is somewhat similar to the find() method. The major difference being that index() raises an exception if value is absent whereas find() does not.

### Example:

```Python
str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Daniel"))
```

### Output:

```Python
ValueError: substring not found
```

## isalnum():

The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.

### Example:

```Python
str1 = "WelcomeToTheConsole"
print(str1.isalnum())
```

### Output:

```Python
True
```

## isalpha():

The isalpha() method returns True if all the characters are alphabet letters (A-Z)(a-z).

### Example:

```Python
str1 = "Welcome"
print(str1.isalpha())
```

### Output:

```Python
True
```

## islower():

The islower() method returns True if all the characters in the string are lower case, else it returns False.

### Example:

```Python
str1 = "hello world"
print(str1.islower())
```

### Output:

```Python
True
```

## isprintable():

The isprintable() method returns True if all the values within the given string are printable, if not, then return False.

### Example:

```Python
str1 = "We wish you a Merry Christmas"
print(str1.isprintable())
```

### Output:

```Python
True
```

## isspace():

The isspace() method returns True only and only if the string contains white spaces, else returns False.

### Example:

```Python
str1 = "        "       #using Spacebar
print(str1.isspace())
str2 = "        "       #using Tab
print(str2.isspace())
```

### Output:

```Python
True
True
```

## istitle():

The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.

### Example:

```Python
str1 = "World Health Organization" 
print(str1.istitle())
```

### Output:

```Python
True
```

### Example:

```Python
str2 = "To kill a Mocking bird"
print(str2.istitle())
```

### Output:

```Python
False
```

## isupper():

The isupper() method returns True if all the characters in the string are upper case, else it returns False.

### Example:

```Python
str1 = "WORLD HEALTH ORGANIZATION" 
print(str1.isupper())
```

### Output:

```Python
True
```

## startswith():

The endswith() method checks if the string starts with a given value. If yes then return True, else return False.

### Example:

```Python
str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))
```

### Output:

```Python
True
```

## swapcase():

The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.

### Example:

```Python
str1 = "Python is a Interpreted Language" 
print(str1.swapcase())
```

### Output:

```Python
pYTHON IS A iNTERPRETED lANGUAGE
```

## title():

The title() method capitalizes each letter of the word within the string.

### Example:

```Python
str1 = "He's name is Dan. Dan is an honest man."
print(str1.title())
```

### Output:

```Python
He'S Name Is Dan. Dan Is An Honest Man.
```
