letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "User"
print(letter.format(country, name)) # at 0th index is country & 1th index is name


print(f"Hey my name is {name} and I am from {country}")
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}") # see this output


price = 49.09999
txt = f"For only {price:.2f} dollars!" # .2f takes 2 decimal places , output will be 49.09
print(txt)


print(f"{2 * 30}")
print(type(f"{2 * 30}"))