# String Slicing & Operations on String

## Length of a String

We can find the length of a string using len() function.

### Example:

```Python
fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word.")
```

### Output

```Python
Mango is a 5 letter word
```

## String as an array

A string is essentially a sequence of characters also called an array. Thus we can access the elements of this array.

## Example:

```Python
pie = "ApplePie"
print(pie[:5])
print(pie[6])   #returns character at specified index
```

### Output

```Python
Apple
i
```

> Note: This method of specifying the start and end index to specify a part of a string is called slicing.

## Slicing Example:

```Python
pie = "ApplePie"
print(pie[:5])      #Slicing from Start
print(pie[5:])      #Slicing till End
print(pie[2:6])     #Slicing in between
print(pie[-8:])     #Slicing using negative index
```

### Output

```Python
Apple
Pie
pleP
ApplePie
```

## Loop through a String:

Strings are arrays and arrays are iterable. Thus we can loop through strings.

### Example:

```Python
alphabets = "ABCDE"
for i in alphabets:
    print(i)
```

### Output

```Python
A
B
C
D
E
```
