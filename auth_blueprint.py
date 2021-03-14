from flask import Blueprint, render_template, request
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.mybase
posts = db.posts

admin = Blueprint('admin', __name__, static_folder='static', template_folder='templates')


@admin.route('/')
def index():
    return '<h1>Test Blueprint</h1>'


@admin.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print('method: post')
        # выводим все документы из коллекции coll
        username = request.form.get('username')
        password = request.form.get('password')
        type_sensor = request.form.get('type_sensor')
        # подсчет количества людей с именем Петр
        if posts.find_one({"username": username, "password": password}):
            return "<h2>AUTHORISATION SUCCESS!</h2>"
        else:
            return "<h2>USER INCORRECT!</h2>"
    return render_template('auth/login.html')


@admin.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        print('method: post')
        # выводим все документы из коллекции coll
        username = request.form.get('username')
        password = request.form.get('password')
        type_sensor = request.form.get('type_sensor')
        # подсчет количества людей с именем Петр
        if posts.count_documents({"username": username}) != 0:
            print('USER INCORRECT!')
            return render_template('index.html')
        else:
            print('ADD NEW USER!')
            print(username, password, type_sensor)
            post_data = {
                'username': username,
                'password': password,
                'type_sensor': type_sensor
            }
            result = posts.insert_one(post_data)
            print('One post: {0}'.format(result.inserted_id))
            print('write ok!')
        return '<h1>Write to db</h1>'
    print('GET')
    return render_template('auth/register.html')
