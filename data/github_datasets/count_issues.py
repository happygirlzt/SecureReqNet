import os

if __name__ == '__main__':
	repo_count = 0
	github_issue = 0
	sr = 0
	nsr = 0

	directory = './organizations'
	for group in os.listdir(directory):
		group_folder = os.path.join(directory, group)
		if os.path.isdir(group_folder):
			for repo in os.listdir(group_folder):
				repo_folder = os.path.join(group_folder, repo)
				if os.path.isdir(repo_folder):
					repo_count += len(os.listdir(repo_folder)) - 1
				for r, d, f in os.walk(repo_folder):
					github_issue += len(f) - 1
					if r != repo_folder:
						ground_truth = os.path.join(r, 'ground_truth.txt')
						file = open(ground_truth, 'r')
						for line in file:
							temp = line.split(' ')[1]
							print(temp)
							if temp == '(1,0)\n':
								sr += 1
								continue
							if temp == '(0,1)\n':
								nsr += 1
								continue
	print("Repo count: {}".format(repo_count))  # repo count
	print("GitHub issue count: {}".format(github_issue))  # issue count
	print("sr count: {}".format(sr))  # sr count
	print("nsr count: {}".format(nsr))  # nsr count
