#Encrupt plain text into chiper text using caesar chiper
def encrypt(text,k):
result = ""
   # transverse the plain text
   for i in range(len(text)):
      char = text[i]
      # Encrypt uppercase characters in plain text
      
      if (char.isupper()):
         result += chr((ord(char) + s-65) % 26 + 65)
      # Encrypt lowercase characters in plain text
      else:
         result += chr((ord(char) + s - 97) % 26 + 97)
      return result
#check the above function
text = input("enter the text:")
k = int(input("enter the shift pattern:"))
print("Plain Text : " + text)
print("Shift pattern : " + str(k))
print("Cipher: " + encrypt(text,k))
