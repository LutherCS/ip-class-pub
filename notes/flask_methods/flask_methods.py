from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from flask import redirect
from flask import make_response

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_user():
    print(request.args)
    if request.method == 'GET':
        user_name = request.cookies.get('username')
        if user_name:
            return render_template('index.html', username=user_name)
        else:
            return render_template('login.html')
    else:
        response = make_response(redirect(url_for('hello_user')))

        if request.form.get('logout'):
            response.set_cookie('username', '', expires=0)
        else:
            user_name = request.form.get('username')
            response.set_cookie('username', user_name)

        return response


if __name__ == '__main__':
    app.run()
