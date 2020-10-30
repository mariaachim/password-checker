import hashlib, pymongo, getpass

myclient = pymongo.MongoClient("mongodb://localhost:27017/") # database stuff
passwords = myclient.passwords # database
hashed = passwords.hashed # collection

def hash_password(plaintextPassword, salt): # hashes the user input and checks with contents of mongodb collection
    hashedPassword = hashlib.sha256()
    hashedPassword.update(bytes(plaintextPassword + salt, "utf-8"))
    return hashedPassword.hexdigest()

attempts = 0
loggedIn = False

while attempts < 3 and loggedIn == False:
    passwd = getpass.getpass("Please enter your password: ") # deobfuscation in terminal
    if len(passwd) < 8:
        print("Password is too short :(")
        exit()
    for doc in hashed.find():
        if hash_password(passwd, doc["salt"]) == doc["hashed"]:
            loggedIn = True
            break
        else:
            attempts += 1
            
    if loggedIn == True:
        print("Success! You have logged in :) ")
    else:
        print("Incorrect password")

if loggedIn == False:
    print("You have been locked out!")

exit()