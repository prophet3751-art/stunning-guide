from cryptography.fernet import Fernet as fr

key = fr.generate_key()
with open("key.key", "wb") as f:
    f.write(key)