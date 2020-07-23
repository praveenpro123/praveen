import git
import subprocess

def git_rebase_operation(local_repo, branch_name1, branch_name2):
	command = 'git rebase ' + branch_name2
	try:
		repo = git.Repo(local_repo)
		branch = repo.branches[branch_name1]
		branch.checkout(force=True)
		pipe = subprocess.Popen(command, shell=True, cwd=local_repo, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		(out, error) = pipe.communicate()		
		pipe.wait()
		pipe.kill()
		return {'status': out.decode('utf-8'), 'error': error.decode('utf-8')}
                        
	except git.exc.NoSuchPathError as error:
		return {'status': 'Fail', 'error': str(error) + ', No such folder exists'}

	except git.exc.InvalidGitRepositoryError as error:
		return {'status': 'Fail', 'error': str(error) + ' is a Invalid git repository'}

	except AttributeError as error:
		return {'status': 'Fail', 'error': str(error)}

	except IndexError as error:
		return {'status': 'Fail', 'error': str(error)}

	except Exception as error:
		return {'status': 'Fail', 'error': str(error)}

local_repo = "c:\\testing"
branch_name1 = "local"
branch_name2 = 'branch'

print(git_rebase_operation(local_repo, branch_name1, branch_name2))
