import flask
import os
import json
import hashlib
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

app = flask.Flask(__name__)
cors = CORS(app)
app.config['DEBUG'] = True
app.config['CORS_HEADERS'] = 'Content-Type'
#  DB config
username = os.getenv("DATABASE_USER")
password = os.getenv("DATABASE_PASS")
server = '127.0.0.1:3306/'
db_name = 'booksite'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + username + ':' + password +'@' + server + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

class user(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    username = db.Column(db.string(20))
    pass_hash = db.Column(db.string(64))
    salt = db.Column(db.string(16))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

@app.route('/get_user', methods=['GET'])
@cross_origin()
def query_user():
    try:
        query = user.query.all()
        res = []
        for elem in query:
            tmp = {
                    "":""
                    }
            
            res.append(tmp)
        res = json.dumps(res)
        return res
    except Exception as e:
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = "<h1>Something's wrong</h1>"
        return hed + error_text


@app.route('/add_user', methods=['POST'])
@cross_origin()
def add_user():
    try:
        username = request.args.get('username')
        password = request.args.get('password')

        salt = 
    except Exception as e:
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = "<h1>Something's wrong</h1>"
        return hed + error_text


@app.route('/login', methods=['GET'])
@cross_origin()
def login():
    try:
        pass
    except Exception as e:
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        head = "<h1>Something's wrong</h1>"
        return head + error_text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4242)
