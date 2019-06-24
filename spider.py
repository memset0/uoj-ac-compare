import re, requests

class Problem:
	def __init__(self, problem_name, problem_id, status_a, status_b):
		self.problem_name = problem_name
		self.problem_id = problem_id
		self.status_a = status_a
		self.status_b = status_b
	def __str__(self):
		return '{name} {id} {A} {B}'.format(
			name = self.problem_name,
			id = self.problem_id,
			A = 'True' if self.status_a else 'False',
			B = 'True' if self.status_b else 'False'
		)

def request_get(url):
	while True:
		try:
			return requests.get(url)
		except:
			pass

def getAcceptList(user):
	base_result = re.findall(
		r'<a href="/problem/[0-9]*" style="display:inline-block; width:4em;">[0-9]*</a>',
		request_get('http://uoj.ac/user/profile/%s' % user).text
	)
	result = [ int(it.split('>')[1].split('<')[0]) for it in base_result ]
	return result

def getProblemNameFromText(text):
	base_result = re.findall(
		r'<td>#[0-9]*</td><td class="text-left"><a href="/problem/[0-9]*">[\s\S]*?</a></td>',
		text
	)
	result = {}
	for problem in base_result:
		problem_id = int(problem.split('>#')[1].split('<')[0])
		problem_name = problem.split('<')[-3].split('>')[-1]
		result[problem_id] = problem_name
	return result

def getProblemMaxPage(text):
	base_result = re.findall(r'/problems\?page=', text)
	result = len(base_result) // 2
	return result

def getProblemNameMap():
	req = request_get('http://uoj.ac/problems')
	req.encoding = 'utf8'
	result = getProblemNameFromText(req.text)
	max_page = getProblemMaxPage(req.text)
	for page in range(2, max_page + 1):
		req = request_get('http://uoj.ac/problems?page=%d' % page)
		req.encoding = 'utf8'
		result.update(getProblemNameFromText(req.text))
	return result

nameDict = getProblemNameMap()

def compare(userA, userB):
	setA = set(getAcceptList(userA))
	setB = set(getAcceptList(userB))
	result = []
	for problem in sorted(setA | setB):
		result.append(Problem(nameDict[problem], problem, problem in setA, problem in setB))
	return result

if __name__ == '__main__':
	for problem in compare('memset0', 'zx2003'):
		print(problem)