from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import ssl
from model_mongodb import Diary

app = Flask(__name__)
CORS(app)


@app.route('/diaries', methods=['GET', 'POST'])
def get_diaries():
    if request.method == "GET":
        diaries = Diary().find_all()
        return {"diaries": diaries}, 200
    if request.method == 'POST':
        diaryToAdd = request.get_json()
        newDiary = Diary(diaryToAdd)
        newDiary.save()
        resp = jsonify(newDiary), 200
        return resp


# this needs to be done properly; still just copy pasted
@app.route('/diaries/<id>/entries', methods=['GET', 'POST'])
def get_entries(id):
    diary = Diary({"_id": id})
    if request.method == "GET":
        entries = Diary().find_all_entries()
        return {"entries": entries}, 200
    if request.method == 'POST':
        entryToAdd = request.get_json()
        newEntry = Entry(entryToAdd)  # don't have an Entry class...
        newEntry.save()
        resp = jsonify(newEntry), 200
        return resp