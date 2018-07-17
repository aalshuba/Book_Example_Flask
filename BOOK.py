from flask import Flask
from flask import jsonify
from flask import request
import json
from flask.json import JSONEncoder



app = Flask(__name__)
bookDB=[
      {
       'id':'101',
       'name':'Harry Potter',
       'author':'JK Rowling'
       },
       { 'id':'201',
         'name':'The Davinci Code',
         'author':'Dan Brown'
       }
     ]

#get all books 
@app.route('/bookdb/book',methods=['GET'])
def getAllBooks():
     return jsonify({'bks':bookDB})

#get book by ID
@app.route('/bookdb/book/<bookId>',methods=['GET'])
def getBook(bookId):
     usr = [ bk for bk in bookDB if (bk['id'] == bookId) ]
     return jsonify({'bk':usr})

#update a book given its ID
@app.route('/bookdb/book/<bookId>',methods=['POST'])
def updateBook(bookId):
  
    em = [ bk for bk in bookDB if (bk['id'] == bookId) ]
    if 'name' in request.json:
        em[0]['name'] = request.json['name']
    if 'author' in request.json:
        em[0]['author'] = request.json['author']
    return jsonify({'bk':em[0]})

#create a new book object  
@app.route('/bookdb/book',methods=['PUT'])
def createBook():
    dat = {
    'id':request.json['id'],
    'name':request.json['name'],
    'author':request.json['author']
    }
    bookDB.append(dat)
    return jsonify(dat)
 
 #DELETE a book given its id 
@app.route('/bookdb/book/<bookId>',methods=['DELETE'])
def deleteBook(bookId):
    em = [ bk for bk in bookDB if (bk['id'] == bookId) ]
    if len(em) == 0:
       abort(404)
   
    bookDB.remove(em[0])
    return jsonify({'response':'Success'})

#run app 
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)