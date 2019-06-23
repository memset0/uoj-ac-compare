from spider import compare

from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', mode="index")

@app.route('/<userA>/<userB>')
def query(userA, userB):
	return render_template('index.html', mode="compare", result=compare(userA, userB), user_a=userA, user_b=userB)

if __name__ == '__main__':
    app.run()