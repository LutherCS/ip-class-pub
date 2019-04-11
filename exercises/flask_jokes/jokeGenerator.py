from flask import Flask, request

import pyjokes

app = Flask(__name__)

@app.route('/jokeGenerator', methods=['GET', 'POST'])
def greetAndSetup():
   if 'jokeType' in request.args and 'jokeLanguage' in request.args:
        return joke(request.args['jokeType'], request.args['jokeLanguage'])
        
   else:
        return sendJokeForm()

def joke(jokeType, jokeLanguage):
    joke = pyjokes.get_joke(jokeLanguage, jokeType)
    return f"""
    <html>
        <head>
            <title>Your computer is funny too</title>  
        </head>
        <body>
            <h3> {joke} </h3>
            <a href="/jokeGenerator">Home</a>
        </body>
    </html>
    """

def sendJokeForm():
    return """
    <html>
        <head>
            <title>Your computer is funny too</title>  
        </head>
        <body>
            <h1> Wanna read a funny joke? </h1>
            <form method='get'>
                <select name='jokeType'> 
                    <option value="">Choose a joke type</option>
                    <option value="neutral">Neutral</option>
                    <option value="chuck">Chuck Norris (only available in English</option>
                </select>
                
                <select name='jokeLanguage'>
                    <option value="">Choose a language</option>
                    <option value="en">English</option>
                    <option value="es">Espanol</option>
                </select>

                <button type = 'submit'> Receive Joke </button>
            </form>
        </body>
    </html>
    """