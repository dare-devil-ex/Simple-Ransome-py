import os
from cryptography.fernet import Fernet

locker = []
root_dir = "C:\\Users/acer/Music/trail"
key = open("Thekey.key", "r+").read()
print(key)
wkaie = Fernet(key)

for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        full_path = os.path.join(dirpath, filename)
        
        with open(full_path, "rb") as f:
            unpackedFile = f.read()
            decData = wkaie.decrypt(unpackedFile)
            
        with open(full_path, "wb") as f:
            f.write(decData)
            
print("Your files decrypted successfully :]")