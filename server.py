from spider import compare

from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', mode="index")

@app.route('/<userA>/<userB>')
def query(userA, userB, methods=['GET']):
    result = []
    base_result = compare(userA, userB)
    for problem in base_result:
        if 'begin' in request.args.keys() and problem.problem_id < int(request.args.get('begin')):
            continue
        if 'end' in request.args.keys() and problem.problem_id > int(request.args.get('end')):
            continue
        result.append(problem)
    return render_template('index.html', mode="compare", result=result, user_a=userA, user_b=userB)

if __name__ == '__main__':
    app.run()