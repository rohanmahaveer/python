def encrypt(string,shift):

  cipher=' '
  for char in string:
      if char ==' ' :
          cipher=cipher+char
      elif char.isupper():
          cipher=cipher+chr((ord(char)+shift-65)%26+65)
      else:
          cipher=cipher+chr((ord(char)+shift-97)%26+97)
  return cipher
print("enter string")
text=input()
print("enter shift")
s=int(input())
print("original string:",text)
print("encrypted string:",encrypt(text,s))
