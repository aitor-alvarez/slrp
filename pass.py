from passlib.hash import pbkdf2_sha256

hash = pbkdf2_sha256.encrypt("tgqawinx")
print(hash)