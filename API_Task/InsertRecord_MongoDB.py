"""Program to insert a record in MongoDB via API"""
from flask import Flask, request, jsonify
import pymongo

client = pymongo.MongoClient("mongodb+srv://karanman7:MGLZ5R2umX3NksS@cluster0.ztdaffn.mongodb.net/?retryWrites=true"
                             "&w=majority")
db = client.test
print(db)
app = Flask(__name__)


@app.route('/insrecmdb', methods=['GET', 'POST'])
def insert_record():
    if request.method == 'POST':
        emp_name = request.json['name']
        emp_mail_id = request.json['mail']
        emp_mob = request.json['mob']

        dict_var = {
            "name": f'"{emp_name}"',
            "email": f'"{emp_mail_id}"',
            "mob": f'{emp_mob}'
        }

        db1 = client['mongotest']
        coll = db1['test']
        coll.insert_one(dict_var)
        return "inserted"


if __name__ == '__main__':
    app.run()
