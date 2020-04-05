text="Thou blind fool, Love, what dost thou to mine eyes \n" \
     "That they behold, and see not what they see \n"\
     "They know what beauty is, see where it lies \n" \
    "Yet what the best is take the worst to be"

f1=open("file1.txt,""w")
f1.write(text)
f1.close()

f1 = open("file1.txt,""r")
f2 =open("file2.txt,""a")
if text[len(text) - 1] == "a" or text[len(text) - 1] == "e" or \
        text[len(text) - 1] == "i" or text[len(text) - 1] == "o" or \
        text[len(text) - 1] == "u" or text[len(text) - 1] == "y":
    text = text + text[len(text) - 1] + "way"
    # S.endswith(str)
    pass #Оператор-заглушка, равноценный отсутствию операции.
else:
    text = text + text[len(text) - 1] + "ay"
 #f1 close

f = str(input("Какой файл?"))
  if f =="file 1"
f1= open("file1.txt")
print(f1.read())
    elif f=="file2"
f2= open("file2.txt")
print(f2.read())
      else:
print("Нет такого файла")