import hashlib, pymongo, random, string, getpass

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
passwords = myclient.passwords
hashed = passwords.hashed

passwd = getpass.getpass("Please enter your password: ")

if len(passwd) >= 8:
    salt = "".join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for i in range(6))
    hashedPassword = hashlib.sha256()
    hashedPassword.update(bytes(passwd + salt, "utf-8"))
    hashed.insert_one( {"hashed": hashedPassword.hexdigest(), "salt": salt} )
else:
    print("Password is less than 8 characters")

# HASHED COLLECTION CONTENTS
# abcd1234
# supersecurepassword
# password1234