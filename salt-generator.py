import pymongo, random, string

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient.passwords
hashed = db.hashed

for doc in hashed.find():
    salt = "".join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for i in range(6))
    db.hashed.update(doc, { "$set": { "salt": salt} } )