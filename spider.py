import re, requests

class Problem:
	def __init__(self, problem_id, problem_name, status_list):
		self.problem_id = problem_id
		self.problem_name = problem_name
		self.status_list = status_list
	def __str__(self):
		result = '#{id}. {name} :'.format(
			name = self.problem_name,
			id = self.problem_id
		)
		for status in self.status_list:
			result += ' 1' if status else ' 0'
		return result

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

def compare(user_list):
	solved_set = {}
	merged_set = set()
	for user in user_list:
		solved_set[user] = set(getAcceptList(user))
		merged_set = merged_set | solved_set[user]
	result = []
	for problem in merged_set:
		status_list = [ (problem in solved_set[user]) for user in user_list ]
		result.append(Problem(problem, nameDict[problem], status_list))
	return result

if __name__ == '__main__':
	for problem in compare(['memset0', 'zx2003']):
		print(problem)