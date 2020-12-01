import pyperclip

text = str(input("Enter text: \n"))
pyperclip.copy(text)

print(pyperclip.paste())