from flask import Flask, request, render_template, abort
from auth_blueprint import admin

app = Flask(__name__)
app.register_blueprint(admin, url_prefix='/admin')


@app.route('/', methods=['get', 'post'])
def index():
    return render_template('index.html')


@app.route('/profile', methods=['get', 'post'])
def profile():
    return render_template('profile.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
