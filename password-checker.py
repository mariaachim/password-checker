import hashlib, pymongo, getpass

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient.passwords
hashed = db.hashed

def hash_password(plaintextPassword, salt):
    hashedPassword = hashlib.sha256()
    hashedPassword.update(bytes(plaintextPassword + salt, "utf-8"))
    return hashedPassword.hexdigest()

attempts = 0
loggedIn = False

while attempts < 3 and loggedIn == False:
    passwd = getpass.getpass("Please enter your password: ")
    if len(passwd) < 8:
        print("Password is too short :(")
        exit()
    for doc in hashed.find():
        if hash_password(passwd, doc["salt"]) == doc["hashed"]:
            print("Success! You have logged in :) ")
            loggedIn = True
            break
        print("Incorrect password")
        attempts += 1
        break

if loggedIn == False:
    print("You have been locked out!")

exit()