from flask import Flask, request, render_template, make_response, redirect, url_for

from itertools import permutations

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def greet_and_setup():
    letter_list = []
    if "dictionary" in request.args:
        if "letter1" in request.args:
            letter_list.append(request.args["letter1"])
        if "letter2" in request.args:
            letter_list.append(request.args["letter2"])
        if "letter3" in request.args:
            letter_list.append(request.args["letter3"])
        if "letter4" in request.args:
            letter_list.append(request.args["letter4"])
        if "letter5" in request.args:
            letter_list.append(request.args["letter5"])
        if "letter6" in request.args:
            letter_list.append(request.args["letter6"])
        if "letter7" in request.args:
            letter_list.append(request.args["letter7"])
        if "addLetters" in request.args:
            letter_list.append(request.args["addLetters"])

        wordDict = findValues(letter_list, request.args['dictionary'])
        sorted_wordDict = sorted(wordDict.items(), key=lambda x: x[1], reverse=True)
        return render_template("table.html", wordsAndValues = sorted_wordDict)    

    else:
        return render_template("index.html")

def findWords(letters, dictionary):
    combos = findCombos(letters)
    word_list = []
    if dictionary == "American":
        full_dict =  set(open("/usr/share/dict/american-english").read().split())

    if dictionary == "British":
        full_dict =  set(open("/usr/share/dict/british-english").read().split())

    for combo in combos:
        if combo in full_dict:
            word_list.append(combo)
        
    return word_list




def findCombos(letters):
    seperator = ''
    joined_letters = seperator.join(letters)

    possible_word_list = ([])

    possible_word_list = set((''.join(p) for i in range(1, len(joined_letters) +1) for p in permutations(joined_letters, i)))

    return possible_word_list




def findValues(words, dictionary):
        scrabble_dict = {
        "a" : 1,
        "b" : 2,
        "c" : 3,
        "d" : 2,
        "e" : 1,
        "f" : 4,
        "g" : 2,
        "h" : 4,
        "i" : 1,
        "j" : 8,
        "k" : 5,
        "l" : 1,
        "m" : 3,
        "n" : 1,
        "o" : 1,
        "p" : 3,
        "q" : 10,
        "r" : 1,
        "s" : 1,
        "t" : 1,
        "u" : 1,
        "v" : 4,
        "w" : 4,
        "x" : 8,
        "y" : 4,
        "z" : 10
        }
        word_list = findWords(words, dictionary)
        wordDict = {}

        for word in word_list:
            char_list = []
            for char in word:
                char_list.append(scrabble_dict[char])

            value = sum(char_list)
            wordDict.update({word:value})

        return wordDict


        
    # else:
    #     response = make_response(redirect(url_for("hello_user"), code=303))
    #     if request.form.get("logout"):
    #         response.set_cookie("username", "", expires=0)
    #     else:
    #         response.set_cookie("username", request.form.get("username"))
    #     return response

# @app.route("/hello/")
# @app.route("/hello/<username>")
# def hello(username=None):
#     return render_template("hello.html", name=username)