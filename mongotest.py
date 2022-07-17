import pymongo

client = pymongo.MongoClient("mongodb+srv://karanman7:MGLZ5R2umX3NksS@cluster0.ztdaffn.mongodb.net/?retryWrites=true"
                             "&w=majority")
db = client.test
print(db)

# """Connecting with Sudhanshu's MongoDB's server"""
# client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
# db = client.test
# print(db)

dict_var = {
    "name": "karan",
    "email": "karanmanchanda90@gmail.com",
    "surname": "manchanda"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(dict_var)
