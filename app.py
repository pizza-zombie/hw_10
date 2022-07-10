import utils
from flask import Flask


app = Flask(__name__)

@app.route("/")
def main_page():
    return f"<pre>\n{utils.get_all(utils.candidates)}\n</pre>"


@app.route("/candidates/<int:x>")
def page_candidat(x):
    page = ''
    page += "<img src='https://picsum.photos/200'>\n"
    page += f"<pre>\n{utils.get_by_pk(x)}\n</pre>"
    return page


@app.route("/skills/<x>")
def search_by_skill(x):
    return f"<pre>\n{utils.get_by_skill(x.lower())}\n</pre>"


app.run()