#Ask name of user
name=input("What's your name? ")
#Remove all whitespaces before the first letter and after the last letter of the string
name=name.strip()
#Capitalize the first letter of the string
name=name.capitalize()
#Say Hello to user
print(f"Hello, {name}")