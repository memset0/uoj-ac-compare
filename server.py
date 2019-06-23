from spider import compare

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '<p>UOJ 题目比较器 by memset0.</p><p>使用方式 &lt;GET&gt; <code>/<他的用户名>/<你的用户名></code> </p>'

@app.route('/<userA>/<userB>')
def query(userA, userB):
	result = ''
	problem_list = compare(userA, userB)
	for problem in problem_list:
		result += '<p>#{id}. {name} <code>{A}</code> <code>{B}</code></p>'.format(
			id = problem.problem_id,
			name = problem.problem_name,
			A = '[x]' if problem.status_a else '[ ]',
			B = '[x]' if problem.status_b else '[ ]'
		)
	return result;

if __name__ == '__main__':
    app.run()