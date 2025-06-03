#Ask name of user while removing all the whitespaces before the first letter and after the last letter of the string; and capitalize the first letter and the first letter after each whitespace of the string
name=input("What's your name? ").strip().title()
#Say Hello to user
print(f"Hello, {name}")