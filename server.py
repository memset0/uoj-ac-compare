from spider import compare

from flask import Flask, request, render_template
app = Flask(__name__)

def error(message="Unknown"):
    return '403: ' + message

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def get(path):
    value = {}
    path_list = path.split('/')
    print(path_list)
    if len(path_list) % 2 == 1:
        return error('Wrong Path')
    for i in range(0, len(path_list) // 2):
        value[path_list[i * 2]] = path_list[i * 2 + 1]
    print(value)
        
    user_list = []
    if 'user' in value.keys():
        for user in value['user'].split(','):
            real = ''
            for ch in user:
                if '0' <= ch and ch <= '9' or 'a' <= ch and ch <= 'z' or 'A' <= ch and ch <= 'Z':
                    real += ch
            if real != '':
                user_list.append(real)

    except_list = []
    if 'except' in value.keys():
        for problem_id in value['except'].split(','):
            real = 0
            for ch in problem_id:
                if '0' <= ch and ch <= '9':
                    real = real * 10 + int(ch)
            if real != 0:
                except_list.append(real)
    print(except_list)

    result = []
    for problem in compare(user_list):
        if 'begin' in value.keys() and problem.problem_id < int(value['begin']):
            continue
        if 'end' in value.keys() and problem.problem_id > int(value['end']):
            continue
        if problem.problem_id in except_list:
            continue
        result.append(problem)
    return render_template('index.html', mode="compare", result=result, user_list=user_list)

if __name__ == '__main__':
    app.run()