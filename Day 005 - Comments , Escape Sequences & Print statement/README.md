# Day 5

## Python Comments

A comment is a part of the coding file that the programmer does not want to execute, rather the programmer uses it to either explain a block of code or to avoid the execution of a specific part of code while testing.

### Single Line comment

To write a comment just add a ‘#’ at the start of the line.

```Python
# This is a single line comment
print("hello")
```

### Multi Line comment

To write multi-line comments you can use ‘#’ at each line or you can use the multiline string.

```Python
# 1st line
# 2nd line
print("hello")
```

or

```Python
'''1st line
2nd line'''
print("hello")
```

## [Escape Sequence Character](https://www.w3schools.com/python/gloss_python_escape_characters.asp)

- To insert characters that cannot be directly used in a string, we use an escape sequence character.
- An escape sequence character is a backslash `\` followed by the character you want to insert.

An example of a character that cannot be directly used in a string is a double quote inside a string that is surrounded by double quotes:

```Python
print("This doesnt "execute")
print("This will \" execute")
```

## Print Statement

The syntax of a print statement looks something like this:

```python
print(object(s), sep=separator, end=end, file=file, flush=flush)
```

### Other Parameters of Print Statement

1. object(s): Any object, and as many as you like. Will be converted to string before printed.
2. sep='separator': Specify how to separate the objects, if there is more than one. Default is ' '
3. end='end': Specify what to print at the end. Default is '\n' (line feed)
4. file: An object with a write method. Default is sys.stdout

Parameters 2 to 4 are optional.
