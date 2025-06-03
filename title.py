#Ask name of user
name=input("What's your name? ")
#Remove all the whitespaces before the first letter and after the last letter of the string
name=name.strip()
#Capitalize the first letter and the first letter after each whitespace of the string
name=name.title()
#Say Hello to user
print(f"Hello, {name}")