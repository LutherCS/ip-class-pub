import random
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, <strong>{}</strong>!'.format('CS330')

@app.route('/users/<username>')
def greet_user(username):
    return 'Hello, <strong>{}</strong>!'.format(username)

@app.route('/number/<int:number>')
def get_number(number):
    return 'The number is {}'.format(number)

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath {}'.format(':'.join(subpath.split('/')))

@app.route('/hello')
def hello_form():
    if 'firstname' in request.args:
        return sendPage(request.args['firstname'])
    else:
        return sendForm()

def sendForm():
    return '''
    <form method='get'>
        <label for='firstname'>Enter Your Name</label>
        <input id='firstname' type='text' name='firstname' placeholder='Alice' />
        <input type='submit'>
    </form>
    '''

def sendPage(name):
    return greet_user(name)